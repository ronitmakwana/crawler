from typing import Sized
import scrapy
from fpdf import FPDF
import re




class crls(scrapy.Spider):
    name = "page"
    start_urls =[
        'https://idrw.org/'
    ]

    def parse(self, response):
        # title = response.css('article.art-post art-article  post-273498 post type-post status-publish format-standard hentry category-india')
        p = response.css('p::text').extract()
        print(p)
        yield {'ptext':p
        }
        print('saved')
        pd = str(p)
        print(pd)
        pd = pd.lower()
        # file=open('text1.pdf',"wb")
        # reader = PyPDF2.pdffile
        

        # pdf = FPDF()
        # pdf.add_page()
        # pdf.setfont("Arial",Size=12)
        # pdf.cell(200,10, txt=pd,ln=1,align='C')
        # pdf.output("text21.pdf")
        # print('save')


        with open("test1.txt",'a') as f:
            f.write(pd)
            print("saved")
  

