# MODULES
from bs4 import BeautifulSoup # Web scraper
from requests import get # To get website content and download the image
from os import system # To clear the screen and call feh
import platform # To determine image_viewing_command

# Replace this with your command to open images
if platform.system() == "Darwin":
    image_viewing_command = 'open temp.jpg'
elif platform.system() == "Linux":
    image_viewing_command = 'xdg-open temp.jpg'
elif platform.system() == "Windows":
    image_viewing_command = 'start temp.jpg'
    clear_command = 'cls'
else:
    image_viewing_command = ''

# FUNCTIONS
def view_images(images): # View images
    for i in images:
        image = i.contents[1].get('data-src') # Get image link
        print(f'URL | {i.get("href")}') # Print corresponding webpage link

        response = get(image, stream=True) # Download Image
        with open('temp.jpg', 'wb') as file: # Save to external file
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        system(image_viewing_command) # Display Image

        # Prompt to move to next image or stop
        while True: 
            choice = input('> (N)ext | (S)top seeing images: ').lower()

            if choice == 's': # Stop seeing images
                system('rm temp.jpg')
                return
            elif choice in ['', 'n', 'next']: # Next image
                break
            else:
                print('Invalid response, write either `N` or `S`')

    system('rm temp.jpg') # Remove temp file

def clear(): # Clear the Screen
    system('clear')
    print('Wallpaper Scraper')
    print('********')
    print('COMMANDS')
    print('s - Search for Wallpaper')
    print('clear - Clear the Screen')
    print('q/exit - Exit the program')
    print('********')

# MAIN LOOP
clear()
while True:
    choice = input('> ').lower()

    if choice[:2] == 's ': # Search
        query = choice[2:]
        if query == '':
            print('Write something...')
            continue

        # Make the beautiful soup object
        sauce = get(f'https://www.wallpaperflare.com/search?wallpaper={query}').text
        soup = BeautifulSoup(sauce, 'lxml')

        # Get all the links on the page
        links = soup.find_all('a')
        if len(links) == 2: # No image links were found, i.e, 0 results
            print('No results were found...')
            continue

        # Filter image urls from the rest
        images = []
        for i in links:
            if i.get('itemprop') == 'url':
                images.append(i)
        images.pop(0)

        view_images(images)

    elif choice == 'clear': # Clear the Screen
        clear()
    elif choice in ['q', 'exit']: # Exit the program
        exit()
    else:
        print('Invalid Command...')
