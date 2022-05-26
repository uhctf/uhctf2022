use rocket::State;
use rocket_contrib::json::Json;
use serde::{Deserialize, Serialize};

use chrono::NaiveDate;

use crate::CredentialsStore;

#[derive(Deserialize)]
pub struct RecoverAttempt {
    email: String,
    birthday: String,
    fav_square: Option<String>,
    highschool_nickname: Option<String>,
}

impl RecoverAttempt {
    fn is_valid(&self, db: &CredentialsStore) -> Result<RecoveryData, RecoverError> {
        if let Some(account) = db
            .credentials
            .iter()
            .find(|item| item.username == self.email)
        {
            match NaiveDate::parse_from_str(&self.birthday, "%Y-%m-%d") {
                Ok(parsed_birthday) => {
                    if account.birthday == parsed_birthday {
                        if let (Some(self_fav_square), Some(self_highschool_nickname)) =
                            (&self.fav_square, &self.highschool_nickname)
                        {
                            if self_highschool_nickname.to_lowercase() == account.highschool_nickname {
                                if self_fav_square.to_lowercase() == account.favorite_square {
                                    Ok(RecoveryData {
                                        password: account.password.clone(),
                                    })
                                } else {
                                    Err(RecoverError::InvalidSquare)
                                }
                            } else {
                                Err(RecoverError::InvalidNickName)
                            }
                        } else {
                            Err(RecoverError::MoreDataNeeded)
                        }
                    } else {
                        Err(RecoverError::InvalidBirthDate)
                    }
                }
                Err(_) => Err(RecoverError::InvalidBirthDate),
            }
        } else {
            Err(RecoverError::NoSuchMail)
        }
    }
}

#[derive(Serialize)]
pub enum RecoverError {
    NoSuchMail,
    InvalidBirthDate,
    MoreDataNeeded,
    InvalidNickName,
    InvalidSquare,
}

#[derive(Serialize)]
pub struct RecoveryData {
    pub password: String,
}

#[post("/recover", format = "json", data = "<recover>")]
pub(crate) fn recover(
    db: State<CredentialsStore>,
    recover: Json<RecoverAttempt>,
) -> Json<Result<RecoveryData, RecoverError>> {
    Json(recover.is_valid(&db))
}
