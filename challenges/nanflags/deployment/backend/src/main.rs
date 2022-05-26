#![feature(proc_macro_hygiene, decl_macro)]
#[macro_use]
extern crate rocket;

use rocket::fairing::{Fairing, Info, Kind};
use rocket::http::Header;
use rocket::{Request, Response};

pub struct CORS;

impl Fairing for CORS {
    fn info(&self) -> Info {
        Info {
            name: "Add CORS headers to responses",
            kind: Kind::Response,
        }
    }

    fn on_response(&self, _: &Request, response: &mut Response) {
        response.set_header(Header::new("Access-Control-Allow-Origin", "*"));
        response.set_header(Header::new(
            "Access-Control-Allow-Methods",
            "POST, GET, PATCH, OPTIONS",
        ));
    }
}

use chrono::NaiveDate;
use rocket_contrib::serve::StaticFiles;
use std::path::PathBuf;

struct Account {
    pub username: String,
    pub password: String,
    pub birthday: NaiveDate,
    pub highschool_nickname: String,
    pub favorite_square: String,
}

struct CredentialsStore {
    /// Username -> password
    pub credentials: Vec<Account>,
}

impl Default for CredentialsStore {
    fn default() -> Self {
        Self {
            credentials: vec![Account {
                username: "mansur.jalmifsud@nanflags.com".into(),
                password: "yK5kNVhcUHL8ED2HJUinfY6PJW5EsmV".into(),
                birthday: chrono::NaiveDate::from_ymd(1977, 5, 4),
                highschool_nickname: "bobby".into(),
                favorite_square: "vismarkt".into(),
            }],
        }
    }
}

pub mod login;
pub mod recovery;

fn main() {
    let path_to_static = {
        // from target folder to the static folder.
        //
        // Yeah, I know it looks ugly
        let mut path: PathBuf = std::env::current_exe().unwrap().parent().unwrap().into();
        path.push("static");
        path
    };

    rocket::ignite()
        .attach(CORS)
        .mount("/api", routes![recovery::recover, login::login])
        .mount("/", StaticFiles::from(&path_to_static).rank(1))
        .manage(CredentialsStore::default())
        .launch();
}
