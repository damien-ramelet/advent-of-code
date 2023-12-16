use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;

fn main() -> std::io::Result<()> {
    let mut file = File::open("input")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    let mut count = 0;
    let mut santa_coordinates_houses: HashMap<(i32, i32), i32> = HashMap::new();
    let mut rsanta_coordinates_houses: HashMap<(i32, i32), i32> = HashMap::new();

    let mut santa_coordinates: (i32, i32) = (0, 0);
    let mut rsanta_coordinates: (i32, i32) = (0, 0);
    santa_coordinates_houses.insert(santa_coordinates, 1);
    rsanta_coordinates_houses.insert(rsanta_coordinates, 1);

    let mut hash_map_coordinates: &mut HashMap<(i32, i32), i32>;
    let mut coordinates: &mut (i32, i32);

    for (i, char) in content.chars().enumerate() {

        if i % 2 != 0 {
            hash_map_coordinates = &mut rsanta_coordinates_houses;
            coordinates = &mut rsanta_coordinates;
        } else {
            hash_map_coordinates = &mut santa_coordinates_houses;
            coordinates = &mut santa_coordinates;
        }

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
        hash_map_coordinates.entry(*coordinates).and_modify(|coordinates| *coordinates += 1).or_insert(1);
    }

    for &gifts in santa_coordinates_houses.values() {
        if gifts > 0 {
            count += 1;
        }
    }

    for (coordinates, gifts) in rsanta_coordinates_houses {
        if gifts > 0 && !santa_coordinates_houses.contains_key(&coordinates) {
            count += 1;
        }
    }

    println!("{count}");

    Ok(())
}
