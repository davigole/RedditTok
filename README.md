# RedditTok
Made by **Davi Golebiovski**

## Description 📰
If you have been around TikTok lately, you've probably noticed these videos where someone reads a Reddit post with a Minecraft gameplay behind it.

To make these videos, the creator needs to get a Minecraft gameplay, take screenshots of a Reddit post, and add a voice to the video.

Since all these tasks can be automated, I've decided to make a program that does them for me.

## Inspiration 🧠
I did **not** come up with this idea. Another user called [Lewis Menelaws](https://github.com/elebumm) has [done this program before](https://github.com/elebumm/RedditVideoMakerBot), and I used his work as an inspiration for mine.

## Installation 💾
 1. Clone this repository 🐱
 2. Run `pip install -r requirements.txt` 📄
 3. Run `python master/background.py` to install sample background 📷
 4. Enjoy! 😊

## Usage 💻
To use RedditTok, run:
```python main.py URL [--path] [--comments] [--background_path] [--background_start] /L /T```
where
 - `URL`: Reddit URL to get screenshots from
 - `--path`: Path to save final video (default: `output.mp4`)
 - `--comments`: Maximum number of comments in video (default: `5`)
 - `--background_path`: Path to background video (default: `assets/background.mp4`)
 - `--background_start`: Moment in seconds when background video should start (default: `-1` = random)
 - `/L`: Set Reddit to light mode
 - `/T`: Keep temporary files after execution at `temp`

## Improvements 🌟
 - [ ] Add music to video
 - [ ] Download YouTube videos for background automatically
 - [ ] Set delay between screenshots
 - [ ] Change voice