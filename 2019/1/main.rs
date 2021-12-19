// Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

use std::io::prelude::*;
use std::fs::File;
use std::io::BufReader;

fn module_mass(v: f32) -> f32 {
	return (v / 3.0).floor() - 2.0
}


fn part1() {
	let file = File::open("input.txt").unwrap();
 	let reader = BufReader::new(file);

  	let r:f32 = reader.lines()
		.map(|v| v.unwrap().parse::<f32>().unwrap())
		.map(|v| module_mass(v))
		.sum();

	println!("Part 1: {:?}", r);
}

fn recursive_mass(v: f32) -> f32 {
	let additional = module_mass(v);
	if (additional > 0.0) {
		return v + recursive_mass(additional);
	} else {
		return v;
	}
}

fn part2() {
	let file = File::open("input.txt").unwrap();
 	let reader = BufReader::new(file);

  	let r:f32 = reader.lines()
		.map(|v| v.unwrap().parse::<f32>().unwrap())
		.map(|v| recursive_mass(v) - v)
		.sum();

	println!("Part 2: {:?}", r);
}

fn main() {
	part1();
	part2();
}
