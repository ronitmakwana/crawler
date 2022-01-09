from bs4 import BeautifulSoup
import requests
from fpdf import FPDF


html_text = requests.get('https://idrw.org/')
soup = BeautifulSoup(html_text.text,"lxml")
jobs = soup.find('title').text
titles = soup.find('div',class_="art-layout-cell art-content").text.strip()
# print(jobs)
# text = jobs.text
# print(text)
print(jobs,"\n")
print(titles)

with open('test12.txt',"a") as f:
    f.write(titles)
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial",size=12)
# pdf.cell(200,10, txt=titles,ln=1,align='C')
# pdf.output("title.pdf")
print('save')
# for tit in titles:
#     a = tit.find('p')
#     print(f"title:{a}")

# print(a)



