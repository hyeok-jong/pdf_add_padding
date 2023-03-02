
for 'pdf.py' and 'pdf2.py' version은 '1.27.4'입니다. 

And since there are lagerly updated 2022  

use version 3.0.1 for 'pdf3.py' which is latest version

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
그리고 원본 유지를 위해 `_resize.pdf`로 새롭게 저장합니다.  

또한 `all`을 입력하면 printed all files will be padded and savee
