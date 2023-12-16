use md5::compute;

fn main() {
    let mut i = 0;

    while true {
        let mut input = String::from("bgvyzdsv");
        input.push_str(&i.to_string());
        let result = compute(input);
        if format!("{:x}", result).starts_with("00000") {
            println!("{i}");
            break;
        } else {
            i += 1;
        }

    }

}
