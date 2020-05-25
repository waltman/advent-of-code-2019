use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::error::Error;

fn fuel_req(n: i32) -> i32 {
    n/3 - 2
}

fn fuel_req_tot(n: i32) -> i32 {
    let res = fuel_req(n);
    if res <= 0 {
        0
    } else {
        res + fuel_req_tot(res)
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let file = File::open(filename)?;
    let reader = BufReader::new(file);
    let mut total = 0;
    let mut total2 = 0;
    for line in reader.lines() {
        let n: i32 = line?.parse()?;
        total += fuel_req(n);
        total2 += fuel_req_tot(n);
    }

    println!("part 1: {}", total);
    println!("part 2: {}", total2);

    Ok(())
}
