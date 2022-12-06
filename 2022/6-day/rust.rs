use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::VecDeque;

fn main() {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

    let line = reader.lines().next().unwrap().unwrap();

    let mut i = 0;
    let mut window: VecDeque<char> = VecDeque::new();
    let mut four_unique_chars = false;

    while !four_unique_chars {
        if i > 0 {
            window.pop_front();
            window.push_back(line.chars().nth(i).unwrap());
        } else {
            window.extend(line[0..4].chars());
        }
        
        four_unique_chars = window.iter().collect::<std::collections::HashSet<_>>().len() == 4;
        i += 1;
    }

    println!("{}", i);
}