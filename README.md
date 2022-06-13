# pdf_add_padding

## version 2추가  
pdf.py는 일단 급해서 어떻게든 되게 하려고 해본거고  
pdf2.py는 다른 방법으로 빈페이지 만들어 덮어쓰는 방식으로 직접 이해해서 구현함. 두번째꺼 이용하는 것을 추천!

아 그리고 onenote사용하는 사람들을 위해서 첫장은 빈 페이지

## PDF에 오른쪽과 아래에 padding을 추가하는 기능을 합니다.  
Padding size는 조절하수 있게 해놓았지만 특히 작은 padding의 경우 오류가 생길 수 있습니다.  
Default로는 300을 해 놓았는데 가장 이상적인 size이며 이는 변환하고자 하는 PDF의 사이즈에는 비례하지 않습니다.  
따라서 때때로 padding size를 변경하는 것이 필요할 수 있습니다.  

Padding의 위치를 변호나하고 싶다면 소스코드를 보고 구글링을 하시면 되는데 잘 안나와 있습니다.  
아마 이러한 기능을 거의 사용하지 않는것 같습니다.  

이러한 기능을 구현하는데 가장 쉬운 방법은 이미지로 변환하여 padding을 직접 만들어 concate할 수도 있습니다.  
하지만 이는 PDF이지만 text가 아닌 image이므로 불편할 뿐 아니라 추가적인 메모리도 필요하고 시간이 많이 소요 됩니다.  


# How to Implement?  
쉽습니다.  
우선 `PyPDF2` 만 설치하세요. 
나의 version은 '1.27.4'입니다.  

pdf.py를 변환하고자 하는 pdf가 있는 위치에 두면 directory안읽고 자연스럽게 가능합니다.  
사실 리눅스 쓰다 윈도우 쓰려니 directory를 잘 몰라 그냥 이렇게 했습니다. (오류나서 안했습니다)  
.py를 실행하면 해당 directory에 있는 모든 .pdf를 출력해줄겁니다.  
E.g)  
```
0 DL_lecture1_20220308.pdf
2 week2 basic machine learning.pdf
3 week6-1 Deep Feedforward Networks.pdf
4 week6-2 Sequence Modeling Recurrent and Recursive Nets.pdf
5 week6-3 Project.pdf
```
그럼 여기서 변환하고자 하는 파일의 번호를 입력하세요.  
예를들어 `0 3 4`  
두려워 하지 마세요 원본파일을 건들이지 않고 `_resize.pdf`로 새롭게 저장합니다.  

또한 `all`을 입력하면 printed all files will be padded and savee
