use std::env;
use std::fs;
use std::time::{Instant};
use rand::Rng;
use serde_json::{Value};
use image::{Rgb, ImageBuffer};

fn main() {
    let args: Vec<String> = env::args().collect();
    let config_file = &args[1];
    let text = fs::read_to_string(&config_file).expect("Where is that file?");
    let config: Value = serde_json::from_str(&text).expect("This is a bad file...");

    //We save width and height...
    let iterations = config["iterations"].as_u64().expect("This is not a valid number of iterations") as u32;
    let width = config["width"].as_u64().expect("This is not a valid width!") as u32;
    let height = config["height"].as_u64().expect("This is not a valid width!") as u32;

    println!("We are testing if we can create an image...");
    println!("We are ready to start...");

    for i in 1..iterations {
        let start = Instant::now();

        let w: u32 = width * (2_u32.pow(i+1));
        let h: u32 = height * (2_u32.pow(i+1));
        println!("Creating an image of {} x {} pixels...", &w, &h);
        create_image(w, h);

        println!("What a success!");
        println!("This took me {} seconds.", format_time(start.elapsed().as_millis()));
    }
}

fn create_image(width: u32, height: u32){
    let mut image: ImageBuffer<image::Rgb<u8>, _> = ImageBuffer::new(width, height);
    let mut r_number;
    let mut g_number;
    let mut b_number;
    let mut red: i64 = 0;
    let mut green: i64 = 0;
    let mut blue: i64 = 0;
    for c in 1..width {
        r_number = rand::thread_rng().gen_range(1..=64);
        g_number = rand::thread_rng().gen_range(1..=64);
        b_number = rand::thread_rng().gen_range(1..=64);
        red = (red + r_number)%255;
        green = (green + g_number)%255;
        blue = (blue + b_number)%255;
        for r in 1..height {
           image.put_pixel(c, r, Rgb([red as u8, green as u8, blue as u8]));
        }
    }
    image.save(format!("{}_{:04}.{}", "output/test", width, "jpg")).expect("I could not save this image!");
}

fn format_time(time: u128) -> String {
    let millis: u64 = (time%1000) as u64;
    let total_seconds: u64 = (time/1000) as u64;
    let minutes: u64 = total_seconds/60;
    let seconds: u64 = total_seconds%60;
    let msg: String = format!("{:02}:{:02}.{:03}", minutes, seconds, millis);
    msg
}