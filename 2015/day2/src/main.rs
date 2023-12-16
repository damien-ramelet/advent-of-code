use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("input")?;
    let mut content = String::new();
    let mut total_surface: i64 = 0;
    file.read_to_string(&mut content)?;

    let mut current_line = String::new();
    for char in content.chars() {
        if char == '\n' {
            println!("line: {current_line}");
            let mut smallest_surface: i64 = 0;
            let dimensions: Vec<&str> = current_line.split('x').collect();
            let side_1 = (dimensions[0].parse().unwrap_or(0) * dimensions[1].parse().unwrap_or(0));
            let side_2 = (dimensions[1].parse().unwrap_or(0) * dimensions[2].parse().unwrap_or(0));
            let side_3 = (dimensions[0].parse().unwrap_or(0) * dimensions[2].parse().unwrap_or(0));
            total_surface += 2 * side_1 + 2 * side_2 + 2 * side_3;
            for &dim in [side_1, side_2, side_3].iter() {
                if dim < smallest_surface || smallest_surface == 0 {
                    smallest_surface = dim
                }
            }
            total_surface += smallest_surface;
            println!("smallest_surface: {smallest_surface}");
            println!("current total_surface: {total_surface}");

            current_line = String::new();
        } else {
            current_line.push(char);
        }
    }

    println!("Surface {total_surface}");

    Ok(())
}
