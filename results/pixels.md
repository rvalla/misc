# Working with pixels directly

## Comparing python and rust

I have different projects in which I need to edit images pixel by pixel (see
[pixelative](https://gitlab.com/azarte/pixelative) or
[chessportraits](https://gitlab.com/azarte/chessportraits) as examples). I noted in
the past that my python implementation is a bit slow. I am starting to write code
in rust so I gave it a try.  
To test both codes I made a little program that creates a series of images of 
random color bands. Both programs double the size of the image at each iteration.
Images look like these:  

![randombands](https://gitlab.com/rodrigovalla/misc/-/raw/master/results/assets/img/randombands.jpg)

The programs check the elapsed time for each image and print it on terminal. Here are
the results in seconds:  

| Image size | Python | Rust | % difference |
| :--------: | :----: | :--: | :----------: |
| 256x256 | 0.07 | 0.06 | 14% less |
| 512x512 | 0.22 | 0.16 | 27% less |
| 1024x1024 | 0.97 | 0.58 | 40% less |
| 2048x2048 | 3.90 | 2.52 | 35% less |
| 4096x4096 | 15.30 | 10.29 | 33% less |
| 8192x8192 | 65.99 | 40.11 | 39% less |

Feel free to contact me by [mail](mailto:rodrigovalla@protonmail.ch) or reach me in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).