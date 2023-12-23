use std::fs::File;
use std::io::{prelude::*, BufReader};
use regex::Regex;

struct Grid {
    lights: [[i32; 1000]; 1000]
}

impl Grid {
    fn toggle(&mut self, line: usize, column: usize) {
        self.lights[line][column] += 2
    }

    fn turn_on(&mut self, line: usize, column: usize) {
        self.lights[line][column] += 1
    }

    fn turn_off(&mut self, line: usize, column: usize) {
        if self.lights[line][column] > 0 {
            self.lights[line][column] -= 1
        }
    }

    fn how_many_on(&self) -> i32 {
        let mut count: i32 = 0;
        for line in self.lights.iter() {
            for column in line.iter() {
                count += column;
            }
        }
        count
    }
}

fn main() -> std::io::Result<()> {
    let file = File::open("input")?;
    let reader = BufReader::new(file);

    let re = Regex::new(r"^(?<action>[\w ]+) (?<start_line>\d+),(?<start_column>\d+) through (?<end_line>\d+),(?<end_column>\d+)$").unwrap();

    let mut grid = Grid { lights: [[0; 1000]; 1000]};

    for line in reader.lines() {
        let ref_to_line = &line?;
        let caps = re.captures(ref_to_line).unwrap();
        let action = &caps["action"];
        let (start_line, start_column) = (*&caps["start_line"].parse::<usize>().unwrap(), *&caps["start_column"].parse::<usize>().unwrap());
        let (end_line, end_column) = (*&caps["end_line"].parse::<usize>().unwrap(),  *&caps["end_column"].parse::<usize>().unwrap());

        for line in start_line..=end_line {
            for column in start_column..=end_column {
                match action {
                    "toggle" => grid.toggle(line, column),
                    "turn on" => grid.turn_on(line, column),
                    "turn off" => grid.turn_off(line, column),
                    _ => panic!(),
                }
            }
        }

    }

    let how_many_on = grid.how_many_on();
    println!("{how_many_on}");

    Ok(())
}
