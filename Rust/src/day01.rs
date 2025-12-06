use std::{fs};

fn part1(data: &Box<[(i64, i64)]>) -> u64 {
    let mut zeros: u64 = 0;
    data.into_iter().fold(50i64, |acc, case| {
        let (dir, diff) = case;
        let result = (acc + diff * dir).rem_euclid(100);
        if result == 0 {zeros += 1}
        return result;
    });
    return zeros;
}

fn part2(data: &Box<[(i64, i64)]>) -> i64 {
    let mut zeros: i64 = 0;
    data.into_iter().fold(50i64, |acc, case| {
        let &(ref dir, mut diff) = case;
        let full_cycles = diff / 100;

        zeros += full_cycles;
        diff -= full_cycles * 100;

        let intermediate = acc + diff * dir;
        if acc != 0 && (intermediate < 0 || intermediate > 100) {zeros += 1}

        let result = (intermediate).rem_euclid(100);
        if result == 0 {zeros += 1}
        return result;
    });
    return zeros;
}

fn parse(input: &str) -> Box<[(i64, i64)]> {
    return input.lines().map(|line| {
        let mut chars = line.chars();
        let dir: i64 = if chars.next() == Some('R') {1} else {-1};
        let diff: i64 = chars.as_str().parse().expect("number");
        return (dir, diff);
    }).collect();
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("input.txt file exists");
    let data = parse(&input);
    let p1 = part1(&data);
    let p2 = part2(&data);
    println!("{p1}\n{p2}");
}