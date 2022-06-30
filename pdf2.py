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
    parser.add_argument("--paper", type = str, default = True, help = "paper form")
    parser.add_argument("--ratio_width", type = float, default = 1.3, help = "ratio to enlarged width")
    parser.add_argument("--ratio_height", type = float, default = 1.3, help = "ratio to enlarged height")
    return parser.parse_args()


def padding(pdf_file, ratio_width = 1.3, ratio_height = 1.3):
    
    output = PyPDF2.PdfFileWriter() 
    pdf = PyPDF2.PdfFileReader(pdf_file)
    for i in tqdm(range(pdf.numPages)):

        page = pdf.getPage(i)
        page.scaleBy(1)  # 이거 건들면 전체 size가 바뀜
        page_blank = PyPDF2.pdf.PageObject.createBlankPage( 
                                                           width = decimal.Decimal(int(page.mediaBox.getWidth())*ratio_width),  
                                                           height = decimal.Decimal(int(page.mediaBox.getHeight())*ratio_height) 
                                                           )

        if i == 0: # add same sized black page at first
            output.addPage( 
                           PyPDF2.pdf.PageObject.createBlankPage( 
                                                                 width = decimal.Decimal(int(page.mediaBox.getWidth())*ratio_width),  
                                                                 height = decimal.Decimal(int(page.mediaBox.getHeight())*ratio_height) 
                                                                 ) 
                           )

        page_blank.mergeScaledTranslatedPage( 
                                             page, 
                                             tx=int(page.mediaBox.getWidth())*(ratio_width-1)//5,   # 0이면 왼쪽 정렬이고 커질수록 왼쪽의 margin이다. 
                                             ty= int(page.mediaBox.getHeight())*(ratio_height-1), 
                                             scale=1 
                                             )    
        
        
        output.addPage(page_blank)
        
        # Eliminate some annoying rectangular box
        output.removeLinks()
        
    with open(f"resized_{pdf_file[:-4]}_w{ratio_width}_h{ratio_height}.pdf", "wb+") as f:
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
        
    if args.paper:
            args.ratio_width = 1.7
            args.ratio_height = 1.05
            
    
    
    for pdf in tqdm(pdfs):
        if isinstance(pdf, str):
            padding(pdf_file = pdf, ratio_width = args.ratio_width, ratio_height = args.ratio_height)
        else:
            padding(pdf_file = pdf_list[pdf], ratio_width = args.ratio_width, ratio_height = args.ratio_height)
    print("끝났다.")
