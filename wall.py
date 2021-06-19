# A simple cli over wallhaven api

# MODULES
from requests import get
import os
import platform


# VARIABLES
resolution = '1920x1080'
clear_command = 'clear'
if platform.system() == 'Linux':
    image_viewing_command = 'xdg-open temp.jpg'
elif platform.system() == 'Darwin':
    image_viewing_command = 'open temp.jpg'
elif platform.system() == 'Windows':
    image_viewing_command = 'start temp.jpg'
    clear_command = 'cls'

# FUNCTIONS
def view_images(images):
    for i in images:
        response = get(i['path'], stream=True) # Download Image
        with open('temp.jpg', 'wb') as file: # Save to external file temporarily
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        os.system(image_viewing_command) # Display Image

        while True:
            choice = input('[N]ext | [S]ave | [Q]uit: ').lower()

            if choice in ['', 'n', 'next']:
                break
            elif choice in ['s', 'save']:
                number = 1 
                while True:
                    if os.path.exists(f'{number}.jpg'):
                        number += 1
                    else:
                        break

                os.system(f'cp temp.jpg {number}.jpg')
                print('Successfully saved image!')
                break

            elif choice in ['q', 'quit']:
                return
            else:
                print('Invalid Command...')

def page_browser(query):
    page = 1
    while True:
        search_results = get(f'https://wallhaven.cc/api/v1/search?q={query}&page={page}').json()
        search_results = search_results['data']

        if search_results == []:
            print('Page not available. If this is the first page you\'re visiting, then your query returned no results, and if it\'s not, then the last page was the last page of the results')
        else:
            view_images(search_results)

        choice = input(f'Current: {page} | (N)ext page | (P)revious page | (Q)quit: ').lower()

        if choice in ['n', 'next']:
            page += 1

        elif choice in ['p', 'previous']:
            if page < 2:
                print(f'Can\'t go to the previous page, you\'re already at the page {page}!')
            else:
                page -= 1
        elif choice in ['q', 'quit']:
            return
        else:
            print('Invalid Command, relooping current page...')

def clear():
    os.system(clear_command)
    print('Wallhaven API')
    print('*******')
    print('s - Search')
    print('sr - Search with resolution')
    print('r - Set resolution')
    print('clear - Clear Screen')
    print('q/exit - Exit')
    print('*******')

clear()

# MAIN LOOP
while True:
    choice = input('> ').lower()

    if choice == 's': # Search by name
        query = input('Enter search query: ')
        query = query.replace(' ', '%20')
        page_browser(query)

    elif choice == 'sr': # Search with resolution
        query = input('Enter search query: ')
        query = query.replace(' ', '%20')
        search_results = get(f'https://wallhaven.cc/api/v1/search?q={query}&resolutions={resolution}').json()
        search_results = search_results['data']

        if search_results == []:
            print('Your search query returned no results, try something else...')
        else:
            view_images(search_results)

    elif choice == 'r': # Set resoluton
        new = input(f'The current resolution is {resolution}, enter the new resolution: ')

        if new.find('x') == -1 or not (new[:new.index('x')].isnumeric() and new[new.index('x')+1:].isnumeric()):
            print('Invalid syntax, it should be `<int>x<int>`')
        else:
            resolution = new
            print(f'Your resolution has now been updated to {resolution}!')

    elif choice == 'clear': # Clear screen
        clear()
    elif choice in ['q', 'exit']: # Quit
        exit()
    else:
        print('Invalid Command...')
