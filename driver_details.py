#   formula 1 driver points
import requests
from bs4 import BeautifulSoup
url = "https://www.formula1.com/en/drivers"
response = requests.get(url)
html_content = response.content
#print(page.read())
soup = BeautifulSoup(html_content,'html.parser')
print("first_name"+"\t"+"second_name"+"\t\t\t"+"points")
print
for r in range(21):

    first_name = soup.find_all('p',class_="f1-heading tracking-normal text-fs-12px leading-tight uppercase font-normal non-italic f1-heading__body font-formulaOne")
    second_name = soup.find_all('p',class_="f1-heading tracking-normal text-fs-18px leading-tight uppercase font-bold non-italic f1-heading__body font-formulaOne")
    points = soup.find_all('p',class_="f1-heading-wide font-formulaOneWide tracking-normal font-normal non-italic text-fs-18px leading-none normal-case")
    print(r+1,")",end='')
    print(first_name[r].get_text(),sep=' ',end='\t')
    print(second_name[r].get_text(),sep=' ',end='\t\t')
    print(points[r].get_text(),end='\n')