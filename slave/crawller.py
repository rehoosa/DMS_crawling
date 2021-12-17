from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os


def createFolder(directory):  # 이미지 저장할 폴더를 생성하는 함수
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error:Creating directory. ' + directory)


def downloadPic():  # 이미지를 다운받는 함수
    n = 1
    for img in bsObject.find_all(name="img", limit=50):  # 이미지를 50개 저장하기 위한 반복문
        imgUrl = img['src']
        imgUrl = imgUrl.replace('&type=f54_54', '')
        with urlopen(imgUrl) as f:
            with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:  # 이미지 + 사진번호 + 확장자는 jpg
                img = f.read()  # 이미지 읽기
                h.write(img)  # 이미지 저장
                if (n % 10 == 0):
                    print('%i Done' % n)
        n += 1
    print('Download Complete')


def showListImageSrc():
    for img in bsObject.find_all(name="img", limit=10):
        print(img['src'])  # 이미지의 src를 출력하는 부분


def saveURLtoFile():
    n = 1
    with open('./' + 'urlList' + '.txt', 'w') as f:
        for img in bsObject.find_all(name="img", limit=50):  # 이미지를 50개 저장하기 위한 반복문
            imgUrl = img['src']
            imgUrl = imgUrl.replace('&type=f54_54', '')
            f.write(imgUrl + "\n")
            if (n % 10 == 0):
                print('%i Done' % n)
            n += 1


baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='  # 네이버 검색url

while (1):
    # 현재는 네이버만 가능
    plusUrl = input('Input searchword : ')  # 검색어 질문
    url = baseUrl + quote_plus(plusUrl)  # url로 이동하기위한 쿼리문자열 만들기

    print(url)
    html = urlopen(url)  # url 열기
    bsObject = BeautifulSoup(html, 'html.parser')

    # print(os.getcwd()) # os에서 현재 주소를 가져옴

    ifDownload = input('Do you want to download it? y or n')
    if ifDownload == 'y':
        createFolder('img')
        downloadPic()

    ifShowList = input('Do you want to see URL? y or n')
    if ifShowList == 'y':
        showListImageSrc()

    ifSaveList = input('Do you want to save URL? y or n')
    if ifSaveList == 'y':
        saveURLtoFile()

    ifExit = input('Are you exit? y or n')
    if ifExit == 'y':
        break
