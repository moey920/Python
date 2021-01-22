import requests
import re
from bs4 import BeautifulSoup


def crawling(soup):
    
    table = soup.find("table", id="main_table_countries_today").find("tbody") # 확진자 데이터를 담고 있는 표를 가져온다.
    rows = table.find_all("tr") # 확진자 데이터를 담고 있는 표의 각각의 row를 리스트로 저장하고 있다.
    
    world_data = {}

    # 하나의 row에 대한 작업을 하기 위해 반복문을 실행한다.
    for row in rows : 
        if "class" in row.attrs :
            if "row_continent" in row["class"] : # 대륙 데이터인 경우 데이터 처리를 하지 않는다.
                continue
                
        td_list = row.find_all("td") # 한 row안에 있는 데이터들을 리스트 형태로 저장한다.
        
        one_country = {"확진자" : 0, "사망자" : 0, "완치" : 0}
        
        country_name = td_list[1].get_text()
        total_causes = td_list[2].get_text().replace(",", "").strip()
        total_deaths = td_list[4].get_text().replace(",", "").strip()
        total_recovered = td_list[6].get_text().replace(",", "").strip()
        
        # 각 값들이 숫자로 변환 가능한 경우에는 변환하고 그렇지 않으면 "N/A"값을 넣는다.
        total_causes = int(total_causes) if total_causes.isdigit() else "N/A"
        total_deaths = int(total_deaths) if total_deaths.isdigit() else "N/A"
        total_recovered = int(total_recovered) if total_recovered.isdigit() else "N/A"
        
        # 딕셔너리 형태로 저장한다.
        one_country["확진자"] = total_causes
        one_country["사망자"] = total_deaths
        one_country["완치"] = total_recovered
        
        world_data[country_name] = one_country
        
    return world_data
    

def main() :
    html = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(html.text, "html.parser")

    # crawling 함수의 결과를 출력합니다.
    data = crawling(soup)
    
    for a, b in data.items() :
        print(a, b)


if __name__ == "__main__" :
    main()

