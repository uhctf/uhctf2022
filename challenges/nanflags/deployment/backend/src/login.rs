use rocket::State;
use rocket_contrib::json::Json;
use serde::{Deserialize, Serialize};

use crate::CredentialsStore;

#[derive(Serialize)]
pub struct CorrectLogin {
    flag: String,
}

impl Default for CorrectLogin {
    fn default() -> Self {
        Self {
            flag: "uhctf{no-six-flags-here-only-this-1-c6aadda}".into(),
        }
    }
}

#[derive(Deserialize)]
pub struct LoginAttempt {
    username: String,
    password: String,
}

#[derive(Serialize)]
pub(crate) enum LoginError {
    UsernameNotFound,
    InvalidPassword,
}

impl LoginAttempt {
    pub(crate) fn verify(&self, db: &CredentialsStore) -> Result<(), LoginError> {
        match db
            .credentials
            .iter()
            .find(|item| item.username == self.username)
        {
            Some(account) => {
                if account.password == self.password {
                    Ok(())
                } else {
                    Err(LoginError::InvalidPassword)
                }
            }
            None => Err(LoginError::UsernameNotFound),
        }
    }
}

#[post("/login", format = "json", data = "<provided_data>")]
pub(crate) fn login(
    db: State<crate::CredentialsStore>,
    provided_data: Json<LoginAttempt>,
) -> Json<Result<CorrectLogin, LoginError>> {
    Json(provided_data.verify(&db).map(|_| CorrectLogin::default()))
}
