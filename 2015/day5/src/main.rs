use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("input")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    let mut count = 0;
    let mut vowels_count = 0;
    let vowels = "aeiou";
    let mut twice_in_a_row = String::new();
    let nasty_strings = vec!["ab", "cd", "pq", "xy"];

    let mut has_twice_in_a_row: bool = false;
    let mut has_nasty_string: bool = false;

    for char in content.chars() {
        if vowels.contains(char) {
            vowels_count += 1;
        }
        if twice_in_a_row.len() == 2 {
            println!("{twice_in_a_row}");
            let vec: Vec<char> = twice_in_a_row.chars().collect();
            if vec[0] == vec[1] {
                has_twice_in_a_row = true;
            } else if nasty_strings.iter().any(|&i| i==twice_in_a_row) {
                println!("{:?}", twice_in_a_row);
                has_nasty_string = true;
            }
            twice_in_a_row = String::from(vec[1]);
        } 

        if twice_in_a_row.len() < 2 {
            twice_in_a_row.push(char);
        }
        if char == '\n' {
            if vowels_count >= 3 && has_twice_in_a_row && !has_nasty_string {
                println!("not nasty, {:?}, {:?}, {:?}", vowels_count, has_twice_in_a_row, has_nasty_string);
                count += 1;
            } else {
                println!("nasty, {:?}, {:?}, {:?}", vowels_count, has_twice_in_a_row, has_nasty_string);
            }
            vowels_count = 0;
            twice_in_a_row = String::new();
            has_twice_in_a_row = false;
            has_nasty_string = false;
            continue
        }

    }

    println!("{count}");

    Ok(())
}
