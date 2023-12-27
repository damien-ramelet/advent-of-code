use std::io::{prelude::*, BufReader};
use std::collections::HashMap;
use std::fs::File;
use regex::Regex;


fn compute_gate_value(gate_repr: &str, inputs: Option<&String>, map_to_value: &mut HashMap<String, i64>, map_to_inputs: &HashMap<String, String>) -> i64 {
    let re = Regex::new(r"^(?<left_input>[a-z0-9]*)\s?(?<operator>[A-Z]*)\s?(?<right_input>[\w\d]*)").unwrap();

    let captures = re.captures(inputs.unwrap()).unwrap();
    let left_input = &captures["left_input"];
    let right_input = &captures["right_input"];
    let operator = &captures["operator"];
    let result: i64;

    match operator {
        "AND" => {
            let left_value = match left_input.parse::<i64>() {
                Ok(value) => value,
                Err(_) => match map_to_value.get(left_input) {
                    Some(value) => *value,
                    None => {
                        let value = compute_gate_value(left_input, map_to_inputs.get(left_input), map_to_value, map_to_inputs);
                        map_to_value.insert(String::from(left_input), value);
                        value
                    },
                }
            };
            let right_value = match right_input.parse::<i64>() {
                Ok(value) => value,
                Err(_) => match map_to_value.get(right_input) {
                    Some(value) => *value,
                    None => {
                        let value = compute_gate_value(right_input, map_to_inputs.get(right_input), map_to_value, map_to_inputs);
                        map_to_value.insert(String::from(right_input), value);
                        value
                    }
                }
            };
            result = left_value & right_value;
        }
        "OR" => {
            let left_value = match left_input.parse::<i64>() {
                Ok(value) => value,
                Err(_) => match map_to_value.get(left_input) {
                    Some(value) => *value,
                    None => {
                        let value = compute_gate_value(left_input, map_to_inputs.get(left_input), map_to_value, map_to_inputs);
                        map_to_value.insert(String::from(left_input), value);
                        value
                    }
                }
            };
            let right_value = match right_input.parse::<i64>() {
                Ok(value) => value,
                Err(_) => match map_to_value.get(right_input) {
                    Some(value) => *value,
                    None => {
                        let value = compute_gate_value(right_input, map_to_inputs.get(right_input), map_to_value, map_to_inputs);
                        map_to_value.insert(String::from(right_input), value);
                        value
                    }
                }
            };
            result = left_value | right_value;
        }
        "LSHIFT" => {
            let left_value = match map_to_value.get(left_input) {
                Some(value) => *value,
                None => {
                    let value = compute_gate_value(left_input, map_to_inputs.get(left_input), map_to_value, map_to_inputs);
                    map_to_value.insert(String::from(left_input), value);
                    value
                }
            };
            let right_value = right_input.parse::<i64>().unwrap();
            result = left_value << right_value;
        }
        "RSHIFT" => {
            let left_value = match map_to_value.get(left_input) {
                Some(value) => *value,
                None => {
                    let value = compute_gate_value(left_input, map_to_inputs.get(left_input), map_to_value, map_to_inputs);
                    map_to_value.insert(String::from(left_input), value);
                    value
                }
            };
            let right_value = right_input.parse::<i64>().unwrap();
            result = left_value >> right_value;
        }
        "NOT" => {
            let right_value = match map_to_value.get(right_input) {
                Some(value) => *value,
                None => {
                    let value = compute_gate_value(right_input, map_to_inputs.get(right_input), map_to_value, map_to_inputs);
                    map_to_value.insert(String::from(right_input), value);
                    value
                }
            };
            result = !right_value;
        }
        _ => {
            result = match left_input.parse::<i64>() {
                Ok(value) => value,
                Err(e) => match map_to_value.get(left_input) {
                    Some(value) => *value,
                    None => {
                        let value = compute_gate_value(left_input, map_to_inputs.get(left_input), map_to_value, map_to_inputs);
                        map_to_value.insert(String::from(left_input), value);
                        value
                    }
                }
            }
        }
    }
    result
}


fn main() -> std::io::Result<()> {
    let file = File::open("input")?;
    let reader = BufReader::new(file);
    let mut representation_gates: HashMap<String, String> = HashMap::new();
    let mut gates_to_values: HashMap<String, i64> = HashMap::new();

    gates_to_values.insert(String::from("b"), 3176);

    for line in reader.lines() {
        let ref_to_line = &line?;
        let parts: Vec<&str> = ref_to_line.split(" -> ").collect();
        representation_gates.insert(String::from(parts[1]), String::from(parts[0])); 
    }

    for (gate_repr, inputs) in representation_gates.iter() {
        let value = gates_to_values.get(gate_repr);

        match value {
            Some(_) => continue,
            None => {
                let value = compute_gate_value(gate_repr, Some(inputs), &mut gates_to_values, &representation_gates);
                gates_to_values.insert(String::from(gate_repr), value);
            }
        }
    }

    let value = gates_to_values.get("a").unwrap();
    println!("a: {value}");
        
    Ok(())
}
