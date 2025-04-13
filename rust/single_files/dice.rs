use std::io;
use std::time::{Instant};

fn main() {
    let start_time = Instant::now();
    println!("I am ready to throw dice for you...");
    loop {
        println!("How many faces this imaginary dice have?");
        let mut user_input = String::new();
        io::stdin()
            .read_line(&mut user_input)
            .expect("That was a strange input!");
        if user_input.trim().eq("exit"){
            println!("I am killing myself now...");
            break
        } else {
            let faces: u32 = match user_input.trim().parse(){
                Ok(n) => n,
                Err(_) => {
                    println!("Imposible to get a number from that input!");
                    continue;
                }
            };
            let result: u32 = throw_dice(start_time.elapsed().as_millis() as u32, faces);
            println!("I got a: {}", result.to_string());
        }
    }
}

fn throw_dice(time: u32, faces: u32) -> u32{
    let dice: u32 = (time%faces)+1; 
    dice
}
