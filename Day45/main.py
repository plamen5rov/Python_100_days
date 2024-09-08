from bs4 import BeautifulSoup

with open('website.html') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.title.string)

# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")

#print(all_anchor_tags)

for tag in all_anchor_tags:
    #print(tag.getText())
    print(tag.get('href'))
    
section_heading = soup.find(name='h3', class_='heading')
print(section_heading.get('class'))

