import requests
from bs4 import BeautifulSoup
from csv import writer

proxies = {
    'http': 'http://27.123.223.77:23500',
    'https': 'http://27.123.223.77:23500',
}

response = requests.get(
    'https://www.intellichoice.com.au/sitemap', proxies=proxies)

soup = BeautifulSoup(response.text, 'html.parser')

bodyWrapper = soup.find('body')

body = bodyWrapper.get_text()
print(body.encode('utf-8'))


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
