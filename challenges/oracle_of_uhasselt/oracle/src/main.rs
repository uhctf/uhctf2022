use dotenv::dotenv;
use openssl::symm::{self, Cipher};
use std::{
    env,
    io::{self, Write},
    process::exit,
};

fn array_concat(left: &[u8], right: &[u8]) -> Vec<u8> {
    left.iter().copied().chain(right.iter().copied()).collect()
}

fn encrypt(key: &[u8], iv: &[u8], plaintext: &[u8]) -> Vec<u8> {
    let iv_plus_plaintext = array_concat(iv, plaintext);
    symm::encrypt(Cipher::aes_128_cbc(), key, Some(iv), &iv_plus_plaintext).unwrap()
}

fn decrypt(key: &[u8], iv: &[u8], cyphertext: &[u8]) -> Result<Vec<u8>, String> {
    symm::decrypt(Cipher::aes_128_cbc(), key, Some(iv), cyphertext)
        .map_err(|_| "Padding is incorrect.".to_string())
}

fn handle_failure(error_message: &str, flag: &[u8]) {
    println!("The oracle has spoken: {}", error_message);
    println!("Maybe this will lead you? {}", hex::encode(flag));
    exit(-1);
}

// Otherwise we crash under socat
#[cfg(unix)]
fn reset_sigpipe() {
    unsafe {
        libc::signal(libc::SIGPIPE, libc::SIG_DFL);
    }
}

fn main() {
    reset_sigpipe();

    dotenv().ok();
    let flag = env::var("FLAG").unwrap();
    let key = env::var("KEY").unwrap();
    let iv = env::var("IV").unwrap();
    let encrypted_flag = encrypt(key.as_bytes(), iv.as_bytes(), flag.as_bytes());

    println!("Welcome to the oracle of Hasselt University!");
    println!("Speak your troubles, student.");

    let mut message = String::new();
    while message.is_empty() {
        print!(">>> ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut message).unwrap();
    }
    println!();

    let cyphertext = match hex::decode(message.trim()) {
        Ok(c) => c,
        Err(_) => {
            handle_failure("Data must be hex encoded.", &encrypted_flag);
            vec![]
        }
    };

    match decrypt(key.as_bytes(), iv.as_bytes(), &cyphertext) {
        Ok(_) => println!("The oracle understands your struggles..."),
        Err(e) => handle_failure(&e, &encrypted_flag),
    }
}
