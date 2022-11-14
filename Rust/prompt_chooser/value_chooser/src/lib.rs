use std::error::Error;
use std::fs;

use termsize;
use rand::Rng;

const SEP_CHAR: &str = "─";
const DEFAULT_MAX: u16 = 50;

pub fn get_output(message: &str, file_path: &str) -> String {
    match message {
        "separator" => get_separator(),
        "names" => make_choice(String::from(file_path)).unwrap(),
        _ => String::from("Incorrect message")
    }
}

fn make_choice(file_path: String) -> Result<String, Box<dyn Error>> {
    let contents = fs::read_to_string(file_path)?;
    let contents: Vec<&str> = contents.lines().collect();

    let choice = contents[rand::thread_rng().gen_range(0..contents.len())];

    return Ok(String::from(choice));
}

fn get_separator() -> String {
    let curr_width = termsize::get().unwrap().cols;
    let chosen = std::cmp::min(curr_width, DEFAULT_MAX);
    SEP_CHAR.repeat(chosen as usize)
}

#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn check_invalid_output() {
        let result = "not_valid";

        assert_eq!(get_output(result, ""), "Incorrect message");
    }

    #[test]
    fn check_correct_width() {
        let result = get_separator();

        assert!(result.contains("─"));
    }
    
    #[test]
    fn check_width_output() {
        let result = get_output("separator", "");

        assert!(result.contains("─"));
    }
}

