import requests
from bs4 import BeautifulSoup
from csv import writer
from selenium import webdriver
import pyautogui
import platform
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = r'C:\Users\jmvse\AppData\Local\Google\Chrome SxS\Application\chrome.exe'
# chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"),
                          options=chrome_options)

driver.get("https://www.intellichoice.com.au/sitemap")
source = driver.page_source.encode('utf-8')
print(source)
driver.quit()


# driver.get("https://www.duo.com")
# driver.get("https://www.intellichoice.com.au/find-owner-builder-home-loans")

# source = driver.page_source.encode('utf-8')

# soup = BeautifulSoup(source, 'html.parser')

# bodyWrapper = soup.find('body')

# body = bodyWrapper.get_text()
# print(body.encode('utf-8'))


# soup = BeautifulSoup(text.encode('utf-8'), 'html.parser')
# posts = soup.find_all(class_='page_item')

# with open('pages.csv', 'w', newline='') as csv_file:
#     csv_writer = writer(csv_file)
#     headers = ['id', 'title', 'body', 'author', 'slug']
#     csv_writer.writerow(headers)

#     id = 0
#     for post in posts:
#         title = post.get_text().replace('\n', '')
#         # title = post.get_text()
#         link = post.find('a')['href']
#         link_split = link.split('/')
#         url = link_split[-1]
#         body = ''
#         author = 'Darin Hindmarsh'
#         rows = [id, title, body, author, url]
#         id += 1
#         csv_writer.writerow(rows)
