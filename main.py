import requests
from bs4 import BeautifulSoup

selected = input('[] Enter Website Address in Full e.g https://google.com : ')
requests = requests.get(selected)

src = requests.content
code = requests.status_code

if code >= 200 and code <=306:
    print('Connection Successful')
elif code >= 400 and code <= 499:
    print('Client Problem Detected by Server!')
elif code >= 500 and code <= 599:
    print('Server is not availible or Under maintainence.')
else:
    print('Unknown error occurred!')

soup = BeautifulSoup(src, 'lxml')

while(True):
    option = input('[] What do you want to do? (enter \"help\" for help) : ')
    option.lower()

    if option == 'help':
        print('f - Find all tags \ns - show specific tag \nexit - exit the program')
        continue
    elif option == 'f':
        tag = input('[] What tag do you want to find? e.g h1, a, div : ')
        str_soup = str(soup.find_all(tag))
        file = open('output.txt', 'wb')
        file.write(str_soup.encode('utf-8'))
        file.close()
        print('Success!')
    elif option == 's':
        tag = input('[] What tag do you want to find? e.g h1, a, div : ')
        classVar = input('[] What class do you want to find? : ')
        str_soup = str(soup.find_all(tag, classVar))
        file = open('output.txt', 'wb')
        file.write(str_soup.encode('utf-8'))
        file.close()
        print('Success!')
    elif option == 'exit':
        exit()
    else:
        print('exit')
        exit()