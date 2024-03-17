import bs4, requests

result = requests.get('https://www.videoschool.com/')

print(result, type(result))
print(result.text)

soup = bs4.BeautifulSoup(result.text, 'html.parser')

print(soup.select('title'))
print(soup.select('title')[0].getText())
print(soup.select('p'), len(soup.select('p')))
print(soup.select('h1'))
print(soup.select('p')[6].getText())

# soup.select('div') -- all elements with div label
# soup.select('#style4') -- all elements with id = 'style4'
# soup.select('.right_class') -- all elements with class = 'right_class'
# soup.select('div span') -- all elements called span and inside div
# soup.select('div>span')  -- any element called span directly inside div with nothing in between.

central_block = soup.select('.fusion-text.fusion-text-1 h5')

for h in central_block:
    #print(h)
    print(h.getText())
    
# get image

result = requests.get('https://www.videoschool.com/photography/')

soup = bs4.BeautifulSoup(result.text, 'html.parser')

image = soup.select('.img-responsive')[0]['src']

image1 = requests.get(image)

f = open('python1/Day11/image1.jpg', 'wb')
f.write(image1.content)
f.close()

# get 5 star books title from toscrape.com

Books_Titles = []
for i in range(1, 51):
    result = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    books = soup.select('.product_pod')
    for book in books:
        rating = book.p['class'][1]
        if rating == 'Five':
            Books_Titles.append(book.h3.a['title'])
        
print(Books_Titles)
print(len(Books_Titles))