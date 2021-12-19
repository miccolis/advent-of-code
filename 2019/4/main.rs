use std::collections::HashMap;
// It is a six-digit number.
// The value is within the range given in your puzzle input.
// Two adjacent digits are the same (like 22 in 122345).
// Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

fn potentials() -> Vec<i32> {
    let range = (240298, 784956);
    //let range = (240298, 250000);

    let mut results: Vec<i32> = Vec::new();
    let mut i = range.0;

    'outer: while i < range.1 {
        let mut prev = None;
        let mut has_dupe = false;
        for j in (0..6).rev() {
            let v = i/10_i32.pow(j) % 10;
            if prev != None {
                let p = prev.unwrap();
                if v < p {
                    //let diff = 10_i32.pow(j) * (p - v);
                    //println!("In {:?} {:?} is less than {:?}, adding {:?}", i, v, p, diff);
                    //i = i + diff;
                    i = i + 1;
                    continue 'outer;
                }
                if !has_dupe && v == p {
                    has_dupe = true;
                }
            }
            // check prev, if Some che
            prev = Some(v);
        }
        if has_dupe {
            results.push(i);
        }
        i = i + 1;
    }
    return results;
}

fn main() {
    let part1_results = potentials();
    println!("Part 1: {:?} potential passwords", part1_results.len());

    let part2_results: Vec<i32> = part1_results.into_iter().filter(|v| {
        let mut map = HashMap::new();
        for c in v.to_string().chars() {
            let counter = map.entry(c).or_insert(0);
            *counter += 1;
        }
        for count in map.values() {
            if *count == 2{
                //println!("True {:?}", map.values());
                return true;
            }
        }
        //println!("False {:?}", map.values());

        return false;
    }).collect();

    println!("Part 2: {:?} potential passwords", part2_results.len());
}
