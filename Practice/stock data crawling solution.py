import requests
from bs4 import BeautifulSoup

# 기업에 대한 정보를 크롤링하는 함수입니다.
def crawling(soup):
    stock = []
    data = {}
    
    
    table = soup.find("table", class_="type_5").find("tbody") # 종목 정보가 담긴 표를 find
    rows = table.find_all("tr") # 표의 데이터를 row 단위로 갖고 있는 리스트
    
    # 각각의 row 하나에 대해 처리하기 위한 반복문을 실행함
    for tr in rows:
        td = ["" for i in range(4)] # 표에 나타난 기업의 정보를 담기 위한 임시 배열
        
        td_list = tr.find_all("td") # row속에 있는 데이터들을 갖고 있음
        
        if(len(td_list) < 5) : continue # row의 구성 요소가 5개 미만인 경우 기업 정보가 아닌 것으로 간주함
        
        for i in range(4):
            td[i] = td_list[i].get_text().replace("\n", "").replace("\t", "").replace("*", "")
        stock.append(td)
        
        if '+' in td[3]: # 등락률이 +이면 data 딕셔너리에 추가
            data[td[0]] = int(td[1].replace(",", ""))
    
    # 기업명, 현재가, 전일비, 등락률이 담긴 리스트 stock을 만들어 출력하세요.
    print(stock)
    return data


def main() :
    # 주어진 url을 크롤링하세요.
    url = "https://finance.naver.com/sise/sise_group_detail.nhn?type=upjong&no=235"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    
    data = crawling(soup)
    # 현재가가 오름차순이 되도록 data 딕셔너리를 출력하세요.
    print(sorted(data.items(), key=lambda x: x[1]))

if __name__ == "__main__" :
    main()

