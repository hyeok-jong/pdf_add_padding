import PyPDF2
import argparse
import os
import pathlib
import sys
from tqdm import tqdm
import decimal
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


def args():
    parser = argparse.ArgumentParser()
    #parser.add_argument("--pdf_dir", type = str, help = "PDF dir not file name")
    parser.add_argument("--margin", type = int, default = "200", help = "Do not change if u want change probabily u have to change line 24 also")
    return parser.parse_args()


def padding(pdf_file, margin = 200):
    
    output = PyPDF2.PdfFileWriter() 
    pdf = PyPDF2.PdfFileReader(pdf_file)
    for i in range(pdf.numPages):
        page = pdf.getPage(i)
        page.scaleBy(1)  # 이거 건들면 전체 size가 바뀜
        page_blank = PyPDF2.pdf.PageObject.createBlankPage( width = decimal.Decimal(int(page.mediaBox.getWidth())*1.3),  height = decimal.Decimal(int(page.mediaBox.getHeight())*1.3) )

        page_blank.mergeScaledTranslatedPage( page, tx=0, ty= int(page.mediaBox.getHeight())*0.3, scale=1 )    
        output.addPage(page_blank)
    with open(f"resized_{pdf_file[:-4]}.pdf", "wb+") as f:
        output.write(f)
    
if __name__=="__main__":
    args = args()
    #pdf_dir = args()
    #pdf_dir = pathlib.Path(pdf_dir)
    pdf_dir = os.getcwd()
    pdf_list = os.listdir(pdf_dir)
    
    print("PDF만 읽었다. 전체 할꺼면 all. 몇개만 할꺼면 해당 숫자 입력하라. 여러개 입력하면 한번에 해줄꺼다.")
    for n,i in enumerate(pdf_list):
        if i[-4:]==".pdf":
            print(n,i)
    pdfs = list(map(str,input().split()))
    
    if pdfs[0] == "all":
        pdfs = []
        for i in pdf_list:
            if i[-4:] == ".pdf":
                pdfs.append(i)
    else:
        pdfs = list(map(int,pdfs))
        
    for pdf in tqdm(pdfs):
        if isinstance(pdf, str):
            padding(pdf_file = pdf, margin = args.margin)
        else:
            padding(pdf_file = pdf_list[pdf], margin = args.margin)
    print("끝났다.")
    
