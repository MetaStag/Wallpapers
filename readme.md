## Here is a collection of wallpapers i use.
---

This repo also comes with a python script, `scraper.py`, this is just a simple program made with bs4 that fetches wallpapers from https://www.wallpaperflare.com, so you can view wallpapers inside your terminal.
Is there really any point to this script? Well, i guess not but it's still there if you want to use it.

#### Setup

As mentioned earlier, this script uses bs4 so make sure you have that installed.

    - Use `pip install BeautifulSoup4` to install it

The program by-default opens images in `feh`. If you don't have it, or want to open images in something else, just open `scraper.py` and change `image_viewing_command` to the corresponding command of your image viewer. For example, with gvenview you would do, `gvenview temp.jpg`
