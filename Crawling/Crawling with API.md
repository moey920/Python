# APII(Application Programming Interface)

## API란?
- API(Application Programming Interface)는 어떤 **프로그램**과 또 다른 **프로그램**을 **연결해주는 매개체**입니다.
- 컴퓨터를 다루기 위해 **마우스와 키보드**를 이용하는 것처럼 API는 프로그램 사이를 연결해주는 역할을 합니다.

### 예를 들어 **지도 데이터**를 이용하여 맛집 찾기 **웹 서비스**를 제작하려면 어떻게 해야 할까요?

        - 보통의 일반인들에게는 지도 데이터를 갖고 있지 않고, 이를 수집하는 것도 매우 어렵습니다.
        - 그렇다고 공개된 데이터를 그대로 사용하는 것도 어렵습니다.
        - Google이 갖고 있는 지도 데이터를 공개하였다고 가정해봅시다.
        - 그러나 원본 데이터는 너무 방대하기도 하고, 호환성 등의 문제도 있어 쉽게 사용할 수 없습니다. 마치 키보드와 마우스가 없는 컴퓨터를 사용하는 것과 같습니다.
        - 그래서 Google은 지도 데이터를 응용하여 사용할 수 있도록 Google Map API라는 매개체를 사용자들에게 제공합니다.

### 다음은 daum 증권 사이트입니다.

        - 여러 기업들의 주가 정보를 API를 거쳐 받아온 후 표시하고 있습니다.
        - daum 증권 사이트와 같이 API를 이용해 정보를 가져오는 웹 사이트가 꽤 있습니다.
        - 이런 경우 정보가 HTML에 **처음부터 존재하지 않고**, 정보를 **API로부터 불러오고 나서** HTML에 존재하게 됩니다.
        - 따라서 daum 증권 사이트에서는 BeautifulSoup를 이용하여 주가 데이터를 크롤링할 수 없습니다.
        - 웹 사이트를 처음 로드할 때 HTML 문서에는 주가 데이터가 존재하지 않기 때문입니다.

### 보통 API를 이용하여 데이터를 불러오는 경우는 데이터가 ‘동적’으로 변화하는 일이 많아 실시간으로 값을 불러와야 하는 경우입니다.

    - 기업의 주가도 하나의 예시입니다.
    - 이럴 땐 daum 증권 사이트에서 주가 정보를 요청하는 API에 접근하여 어떤 정보를 전달해주고 있는지 접근하면 됩니다.
    - 크롬 개발자 도구의 **Network 탭**에서 웹사이트가 데이터를 요청하는 API를 볼 수 있습니다.
    - **API의 URL에** GET 요청을 보내면 **JSON 데이터**를 얻을 수 있습니다.
    - JSON은 key와 value를 저장하는, **딕셔너리 꼴**의 데이터 형식입니다.
    ```
    url = "http://finance.daum.net/api/search/ranks?limit=10"
    req = requests.get(url) # JSON 데이터
    ```

### 몇몇 웹 사이트들은 크롤러 등을 통한 기계적인 접근을 막고 있습니다. 

    - 이를 우회하기 위해 requests.get 메소드에 "headers" 매개변수를 지정해주셔야 합니다.
    - ‘헤더’란 HTTP 상에서 클라이언트와 서버가 요청 또는 응답을 보낼 때 전송하는 부가적인 정보를 의미합니다.
    - 실습에서 headers에 사용할 옵션을 제공하고 있습니다.

### 헤더의 옵션
- referer와 user-agent 옵션을 지정하고 있는데, referer는 이전 웹 페이지의 주소를 의미하고 user-agent는 이용자의 여러 가지 사양을 의미합니다.
```
custom_header = {
'referer’ : ...
'user-agent’ : ... }
```

### API를 이용한 데이터 크롤링 예시(네이버 실시간 검색어, 망고플레이트 검색 상위권 리뷰)
```
import requests
import json            #json import하기

#custom_header을 통해 아닌 것 처럼 위장하기
custom_header = {
    'referer' : 'https://www.naver.com/',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'  }


def get_keyword_ranking() : 
    result = []
    url = "https://apis.naver.com/mobile_main/srchrank/srchrank?frm=main&ag=20s&gr=0&ma=-2&si=-2&en=-2&sp=-2"
    req = requests.get(url, headers = custom_header)
    
    
    if req.status_code == requests.codes.ok:
        print("접속 성공")
        data = json.loads(req.text)
        data = data["data"]
        
        for d in data :
            if len(d["keyword_synonyms"]) == 0 :
                result.append([d["keyword"], None])
            else :
                result.append([d["keyowrd"], d["keyword_synonyms"]])
        
    else:
        print("Error code")
    
    
    return result

def main() :
    result = get_keyword_ranking()
    i = 1
    for keyword, synonyms in result :
        if synonyms :
            print(f"{i}번째 검색어 : {keyword}, 연관검색어 : {synonyms}")
        else :
            print(f"{i}번째 검색어 : {keyword}")
        i += 1
    
if __name__ == "__main__" :
    main()
```

```
from bs4 import BeautifulSoup
import requests
import json            #json import하기

custom_header = {
    'referer' : 'https://www.mangoplate.com/',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' }

def get_reviews(code) :
    comments = []
    

    url = f"https://stage.mangoplate.com/api/v5{code}/reviews.json?language=kor&device_uuid=V3QHS15862342340433605ldDed&device_type=web&start_index=0&request_count=5&sort_by=2"
    req = requests.get(url, headers = custom_header)

    if req.status_code == requests.codes.ok:    
        print("접속 성공")
        reviews = json.loads(req.text)

        for review in reviews :
            comment = review["comment"]
            text = comment["comment"]
            comments.append(text)

    else:
        print("Error code")

        
    return comments
    
    # req에 데이터를 불러온 결과가 저장되어 있습니다.
    # JSON으로 저장된 데이터에서 댓글을 추출하여 comments에 저장하고 반환하세요.
    
    
    

def get_restaurants(name) :
    # 검색어 name이 들어왔을 때 검색 결과로 나타나는 식당들을 리스트에 담아 반환하세요.
    restaurant_list = []
    
    url = "https://www.mangoplate.com/search/" + name
    req = requests.get(url, headers = custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    
    restaurants = soup.find_all("div", class_="list-restaurant-item")
    
    for rest in restaurants :
        info = rest.find("div", class_="info")
        href = info.find("a")["href"]
        title = info.find("h2").get_text().replace("\n", "").replace(" ", "")
        restaurant_list.append([title, href])
    
    return restaurant_list
    
    # soup에는 특정 키워드로 검색한 결과의 HTML이 담겨 있습니다.
    # 특정 키워드와 관련된 음식점의 이름과 href를 튜플로 저장하고,
    # 이름과 href를 담은 튜플들이 담긴 리스트를 반환하세요.
    
    

def main() :
    name = input("검색어를 입력하세요 : ")
    
    restuarant_list = get_restaurants(name)
    
    for r in restuarant_list :
        print(r[0])
        print(get_reviews(r[1]))
        print("="*30)
        print("\n"*2)

if __name__ == "__main__" :
    main()
```
