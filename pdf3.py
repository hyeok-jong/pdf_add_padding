import PyPDF2
import argparse
import os
import pathlib
import sys
from tqdm import tqdm
import decimal
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

import sys
sys.setrecursionlimit(5000) 

def args():
    parser = argparse.ArgumentParser()
    #parser.add_argument("--pdf_dir", type = str, help = "PDF dir not file name")
    # parser.add_argument("--paper", type = str, default = True, help = "paper form")
    parser.add_argument('-wr', "--ratio_width", type = float, default = 1.8, help = "ratio to enlarged width")
    parser.add_argument('-hr', "--ratio_height", type = float, default = 1.2, help = "ratio to enlarged height")
    parser.add_argument('-d', '--directory', type = str, default = f'/Users/dl/Downloads/', help = 'dir to read pdfs.')
    return parser.parse_args()


def padding(pdf_file, ratio_width, ratio_height):
    
    output = PyPDF2.PdfWriter() 
    pdf = PyPDF2.PdfReader(pdf_file)
    for i in tqdm(range(len(pdf.pages))):

        page = pdf.pages[i]

        page.scale_by(1)  # 이거 건들면 전체 size가 바뀜
        page_blank = PyPDF2._page.PageObject.create_blank_page( 
                                                           width = decimal.Decimal(int(page.mediabox.width)*ratio_width),  
                                                           height = decimal.Decimal(int(page.mediabox.height)*ratio_height) 
                                                           )
        if i == 0: # add same sized black page at first
            output.add_page( 
                           PyPDF2._page.PageObject.create_blank_page( 
                                                                 width = decimal.Decimal(int(page.mediabox.width)*ratio_width),  
                                                                 height = decimal.Decimal(int(page.mediabox.height)*ratio_height) 
                                                                 ) 
                           )
            
        '''
        page_blank.mergeScaledTranslatedPage( 
                                             page, 
                                             tx=int(page.mediabox.width)*(ratio_width-1)//4,   # 0이면 왼쪽 정렬이고 커질수록 왼쪽의 margin이다. 즉, 나누는 숫자가 커지면 왼쪽으로 밀리고 작으면 오른쪽으로 밀린다.
                                             ty= int(page.mediabox.height)*(ratio_height-1), 
                                             scale=1 
                                             )    
        '''
        page_blank.merge_page(page)
        page_blank.add_transformation(PyPDF2.Transformation().translate(
            tx = int(page.mediabox.width)*(ratio_width-1)//4, 
            ty = int(page.mediabox.height)*(ratio_height-1)))
        #page_blank.merge_page(page)

        output.add_page(page_blank)
        
        # Eliminate some annoying rectangular box
        output.remove_links()
    dir = pdf_file.split('/')[:-1]
    pdf = pdf_file.split('/')[-1]
    new_dir = '/'.join(dir) + '/' + f"Resized_{pdf[:-4].replace(' ', '_')}_w{ratio_width}_h{ratio_height}.pdf"
    
    
    with open(new_dir, "wb+") as f:
        output.write(f)
    
    
    
    
    
if __name__=="__main__":
    args = args()
    #pdf_dir = args()
    #pdf_dir = pathlib.Path(pdf_dir)
    pdf_dir = f'/{args.directory}'
    print(f'PDF read directory : {pdf_dir}')
    pdf_list = [i for i in os.listdir(pdf_dir) if i.endswith('.pdf')]
    
    print("PDF만 읽었다. 전체 할꺼면 all. 몇개만 할꺼면 해당 숫자 입력하라. 여러개 입력하면 한번에 해줄꺼다.")
    for n,i in enumerate(pdf_list):
        print(n, ':', i)
    TODO = list(map(str,input().split()))
    
    if TODO[0] == "all":
        pdfs = []
        for i in pdf_list:
            if i[-4:] == ".pdf":
                pdfs.append(i)
    else:
        pdfs = [pdf_list[int(i)] for i in TODO]
        
    
    
    for pdf in tqdm(pdfs):
        print(f'processing {pdf} ...')
        padding(pdf_file = f'{pdf_dir}/{pdf}', ratio_width = args.ratio_width, ratio_height = args.ratio_height)
    print("끝났다.")
