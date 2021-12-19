use std::io::prelude::*;
use std::fs::File;
use std::io::BufReader;


fn compute(data: &mut Vec<usize>) -> usize {
    // Run program
    let mut done = false;
    let mut op = 0;

    while !done {
        let operation = data[op];
        let val1 = data[op + 1];
        let val2 = data[op + 2];
        let dest = data[op + 3];
        
        match operation {
            1 => data[dest] = data[val1] + data[val2],
            2 => data[dest] = data[val1] * data[val2],
            99 => done = true,
            _ => done = true
        }
        op = op + 4;
    }

    return data[0];
}

fn load_program() -> Vec<usize> {

	let file = File::open("input.txt").unwrap();
 	let mut reader = BufReader::new(file);

  	let mut s = String::new();
    reader.read_line(&mut s).expect("'Failed to read buffer");

    let data:Vec<usize> = s.replace("\n", "").split(',')
        .map(|v| v.parse::<usize>().unwrap())
        .collect();

    return data;
}

fn part1() {

    let mut data = load_program();

    // Seed program
    data[1] = 12;
    data[2] = 2;

	println!("Part 1: {:?}", compute(&mut data));
}

fn part2() {
    let data = load_program();

    for noun in 0..100 {
        for verb in 0..100 {
            let mut local = data.clone();
            local[1] = noun;
            local[2] = verb;
            let r = compute(&mut local);
	        //println!("Result {:?}", r);
            if r == 19690720 {
	            //println!("Noun: {:?}, Verb: {:?}", noun, verb);
                let output = 100 * noun + verb;
	            println!("Part 2: {:?}", output);
                return;
            }
        }
    }

	println!("Failure");

}


fn main() {
    part1();
	part2();
}
