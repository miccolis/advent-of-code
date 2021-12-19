
use std::io::prelude::*;
use std::fs::File;
use std::io::BufReader;

fn load_traces() -> Vec<Vec<(char, u32)>> {

	let file = File::open("input.txt").unwrap();
 	let mut reader = BufReader::new(file);

    let mut wires:Vec<Vec<(char, u32)>> = Vec::new();

    for _i in 0..2 {
  	    let mut s = String::new();
        reader.read_line(&mut s).expect("'Failed to read buffer");
        let data:Vec<_> = s.replace("\n", "").split(',')
            .map(|v| {
                let mut chars = v.chars();
                return (
                    chars.next().unwrap(),
                    chars.collect::<String>().parse().unwrap()
                );
            })
            .collect();

        wires.push(data);
    }

    return wires;
}

#[derive(Debug)]
struct Position {
    x: i32,
    y: i32,
    steps: i32
}

fn next_location(prev: &Position, delta: &(char, u32)) -> Position {
    let mut next = Position { x: prev.x, y: prev.y, steps: prev.steps };
    let distance = delta.1 as i32;

    if delta.0 == 'R' {
        next.x = prev.x + distance;
    } else if delta.0 == 'L' {
        next.x = prev.x - distance;
    } else if delta.0 == 'U' {
        next.y = prev.y + distance;
    } else if delta.0 == 'D' {
        next.y = prev.y - distance;
    }
    next.steps = next.steps + distance;
    return next;
}

fn crosses(v0: &Position, v1: &Position, h0: &Position, h1: &Position, delay: bool) -> Option<i32> {
    // Check X range first
    if (v0.x > h0.x && v0.x < h1.x) || (v0.x < h0.x && v0.x > h1.x) {
        // Check Y range next
        if (h0.y > v0.y && h0.y < v1.y) || (h0.y < v0.y && h0.y > v1.y) {
            // The X value from the vertical wire and the Y value from the 
            // horizontal wire IS the intersection
            if delay {
                let x_add = v0.x - h0.x;
                let y_add = h0.y - v0.y;
                return Some(v0.steps + h0.steps + x_add.abs() + y_add.abs());
            } else {
                return Some(v0.x.abs() + h0.y.abs());
            }
        }
    }
    return None;
}

fn find(delay: bool) {
    let wires = load_traces();

    let mut pathA:Vec<Position> = vec![Position { x: 0, y:0, steps: 0}];
    wires[0].iter().for_each(|v| {
        pathA.push(next_location(&pathA[pathA.len() - 1], v));
    });

    let mut pathB:Vec<Position> = vec![Position { x: 0, y:0, steps: 0}];
    wires[1].iter().for_each(|v| {
        pathB.push(next_location(&pathB[pathB.len() - 1], v));
    });

    let mut results: Vec<i32> = Vec::new();

    for i in 0..(pathA.len() - 1) {
        for j in 0..(pathB.len() - 1) {
            if pathA[i].x == pathA[i+1].x && pathB[j].y == pathB[j+1].y {
                // A is vertical, B is horizontal
                let r = crosses(&pathA[i], &pathA[i+1], &pathB[j], &pathB[j+1], delay);
                match r {
                    Some(v) => results.push(v),
                    None => ()
                };
            }
            else if pathA[i].y == pathA[i+1].y && pathB[j].x == pathB[j+1].x {
                // A is horizontal, B is vertical 
                let r = crosses(&pathB[j], &pathB[j+1], &pathA[i], &pathA[i+1], delay);
                match r {
                    Some(v) => results.push(v),
                    None => ()
                };
            }
        }
    }
    results.sort();
    println!("Result {:?}", results[0]);
}

fn main() {
    find(false);
    find(true);
}
