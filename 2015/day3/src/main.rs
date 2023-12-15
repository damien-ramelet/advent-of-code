use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;

fn main() -> std::io::Result<()> {
    let mut file = File::open("input")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    let mut count = 0;
    let mut coordinates_houses: HashMap<(i32, i32), i32> = HashMap::new();

    let mut coordinates: (i32, i32) = (0, 0);
    coordinates_houses.insert(coordinates, 1);

    for char in content.chars() {
        match char {
            '>' => {
                coordinates.1 += 1;
            },
            '^' => {
                coordinates.0 -= 1;
            },
            '<' => {
                coordinates.1 -= 1;
            },
            'v' => {
                coordinates.0 += 1;
            },
            '\n' => {
                ();
            },
            _ => {
                panic!();
            },
        }
        coordinates_houses.entry(coordinates).and_modify(|coordinates| *coordinates += 1).or_insert(1);
    }

    for &gifts in coordinates_houses.values() {
        if gifts > 0 {
            count += 1;
        }
    }

    println!("{count}");

    Ok(())
}
