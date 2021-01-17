import requests
import re
from bs4 import BeautifulSoup
import operator

# 기업에 대한 정보를 크롤링하는 함수입니다.
def crawling(soup):
    
    td_name = []
    td_number = []
    td_before = []
    td_updown = []
    #contentarea > div:nth-child(5) > table > tbody > tr:nth-child(1) > td:nth-child(2)
    #contentarea > div:nth-child(5) > table > tbody > tr:nth-child(1) > td:nth-child(3)
    
    tbody = soup.find("tbody")
    
    for tr in tbody.find_all("tr") :
        for td in tr.find_all("td", class_="name") :
            td_name.append(td.get_text().replace('\t', '').replace('\n', '').replace('*', ''))
            # ['베스파 ', '액션스퀘어 ', 'SNK ', '썸에이지 ', '드래곤플라이 ', '조이맥스 ', '컴투스 ' ....]
        for td in tr.select("td:nth-child(2)") :
            td_number.append(td.get_text().replace('\t', '').replace('\n', '').replace('*', ''))
            # ['18,650', '1,640', '21,700', '1,415', '2,470', '2,710', '169,000'.......]
        for td in tr.select("td:nth-child(3)") :
            td_before.append(td.get_text().replace('\t', '').replace('\n', '').replace('*', ''))
            # ['2,600', '60', '500', '10', '15', '5', '0', '0', '0', '100', '800' ....]
        for td in tr.select("td:nth-child(4)") :
            td_updown.append(td.get_text().replace('\t', '').replace('\n', '').replace('*', ''))
            # ['+16.20%', '+3.80%', '+2.36%', '+0.71%', '+0.61%', '+0.18%', '0.00%', '0.00%', '0.00%', '-0.26%', '-0.30%', '-0.33%' ....]
    
    stock = []
    for i in range(len(td_name)) : # 종목 당 종목명, 현재가, 전일비, 등락률을 포함한 리스트의 집합을 2차원 리스트로 생성(stock)
        stock.append([td_name[i], td_number[i], td_before[i], td_updown[i]])
    
    data = {}
    for i in range(len(td_name)) :
        if re.match('\+', td_updown[i]) : # 등략률이 +인 종목만 찾아
            td_number[i] = td_number[i].replace(',', '')
            data[td_name[i]] = int(td_number[i])
    data = sorted(data.items(), key=operator.itemgetter(1))
    
    print(stock)
    print(data)
    #return stock, data


def main() :
    # 주어진 url을 크롤링하세요.
    custom_header = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    url = "https://finance.naver.com/sise/sise_group_detail.nhn?type=upjong&no=235"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    
    # 현재가가 오름차순이 되도록 data 딕셔너리를 출력하세요.
    print(crawling(soup))


if __name__ == "__main__" :
    main()

