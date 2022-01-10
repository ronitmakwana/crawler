from bs4 import BeautifulSoup
import requests
# from fpdf import FPDF
import pdfkit

# pdf = FPDF()
# html_text = requests.get('https://www.defenseworld.net/')
html_text = requests.get('https://idrw.org/')
soup = BeautifulSoup(html_text.text,"lxml")
jobs = soup.find_all('a')
print(jobs,"\n")
# titles = soup.find('div',class_="col-sm-16 col-md-16 col-lg-16 col-xs-16 mt-10").text.strip()
# titles = soup.find('div',class_="art-layout-cell art-content").text.strip()
for j in jobs:
    a = j.find('div',class_='art-postmetadataheader')
    print('jobs : ',j.text)
print(a)
#print(jobs)
# text = jobs.text
# print(text)
# print(jobs,"\n")
# print(titles)

# with open('worldnet.txt',"a") as f:
#     f.write(titles)
    


    # pdf.add_page()
    # pdf.set_font("Arial",size=12)
    # pdf.cell(200,10, txt=titles,ln=1,align='C') 
    # pdf.output("title.pdf")
print('save')
# def save_pdf(htmls, file_name):
    
htmls = "worldnet.txt"
file_name = "worldnet2.pdf"
options = {

    'page-size': 'Letter',

    'margin-top': '0.075in',

    'margin-right': '0.75in',

    'margin-bottom': '0.75in',

    'margin-left': '0.75in',

    'encoding': "UTF-8",

    'custom-header': [

        ('Accept-Encoding', 'gzip')

        ],

    'cookie': [

        ('cookie-name1', 'cookie-value1'),

        ('cookie-name2', 'cookie-value2'),

        ],

    'outline-depth': 10,

    }

pdfkit.from_file(htmls,file_name, options=options) 
print("pdf")

# for tit in titles:
#     a = tit.find('p')
#     print(f"title:{a}")

# print(a)


