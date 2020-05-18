use std::env;
// use std::fs::File;
// use std::io::{self, BufRead, BufReader};

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

fn main() {
// fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    println!("filename: {}", filename);

    // let file = File::open(filename)?;
    // let reader = BufReader::new(file);
    // let mut total = 0;
    // for line in reader.lines() {
    //     println!("line: {}", line?);
    //     let foo = line?;
    //     let n: i32 = match foo.parse() {
    //         Ok(num) => num,
    //         Err(_) => continue,
    //     };
        
    //     total += fuel_req(n);
    // }

    // println!("part 1: {}", total);

    for x in 10..20 {
        println!("{}: {}", x, fuel_req(x));
    }

//     Ok(())
}
