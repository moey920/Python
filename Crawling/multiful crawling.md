# 여러 페이지 크롤링하기

## Query

> 동아일보 뉴스 웹사이트는 각 페이지의 URL에서 p=(숫자) 부분이 20씩 증가하고 있는 규칙이 있습니다. 이 사이트에서 여러 페이지를 크롤링하려면 어떻게 해야 할까요? 

- 쉬운 방법으로는 URL을 문자열 연산으로 처리하여 새로운 URL을 얻는 것입니다.
```
for i in range(0, 5) :
url = "http://sports.donga.com/Enter?p="+str((i*20+1))
...
```

- 하지만, URL의 query(쿼리)를 이용하면 이 작업을 더 효과적으로 할 수 있습니다.

> Query : 웹 서버에 **GET 요청을 보낼 때 조건에 맞는 정보를 표현**하기 위한 변수
- 예) 
    1. 번호가 1번인 학생을 보여줘라
    2. 전체 기사 중 페이지가 21인 기사들을 보여줘라
    3. ```google.com/search?q=elice```
        google에 ‘elice’를 검색한 결과입니다. q라는 변수에 elice라는 값이 담겨, 전체 데이터 중 elice라는 키워드로 검색한 결과만을 보여줍니다.
    4. 네이버 영화 서비스에서 특정 영화를 클릭하면, code라는 변수에 영화 코드가 담겨 해당 영화에 대한 정보를 보여줍니다.

## requests 라이브러리

> requests의 get 메소드로 GET 요청을 보낼 때 params 매개변수에 딕셔너리를 전달함으로서 쿼리를 지정할 수 있습니다.
```
url = "https://www.google.com/search"
result = requests.get(url, params = {'q':'elice'})
```

> 전체 영화 데이터에서 영화 코드에 대한 정보를 찾고, 다시 requests를 이용하여 특정 영화에 대한 정보를 얻는 요청을 할 수 있습니다.
```
code = ... # 영화 코드에 대한 정보를 얻는다.
result = requests.get(url, params = {'movie':code})
```

## Tag Attribute

### 태그와 속성
> HTML에는 여러 종류의 태그와, 태그에 특정 기능이나 유형을 적용하는 속성이 있습니다.
```<div(태그) class(속성)=“elice” id(속성)=“title”>제목</div>```

> 어떤 태그의 속성이 무엇이 있는지 확인할 때는 attrs 멤버변수를 출력합니다.
```
div = soup.find("div")
print(div.attrs)
```

> attrs 딕셔너리의 키로 인덱싱하여, 태그의 속성에 접근할 수 있습니다.
```print(div['class'])```

> href 속성 : a 태그는 하이퍼링크를 걸어주는 태그로써 이동할 URL을 href 속성에 담고 있습니다.
```<a href=“https...”>기사 제목</a>```

- 위와 같이 href 속성을 이용하여 웹 페이지에 존재하는 하이퍼링크의 URL을 얻을 수 있습니다.
```
a = soup.find("a")
href_url = a["href"]
```

## Children, Name

### Children, Name
- 웹 사이트의 구조가 복잡한 경우 다양한 옵션을 적용해야 할 수도 있습니다.
- children은 **어떤 태그가 포함하고 있는 태그**를, name은 **어떤 태그의 이름**을 의미하는 속성입니다.
> Children
```
<div> # children : span, span, p, img
    <span>span1</span> #name : span
    <span>span2</span>
    <p>p tag</p>
    <img ... />
</div>
```

- beautifulsoup의 children 속성으로 어떤 태그가 포함하고 있는 태그들도 조회할 수 있습니다.

- 아래 코드는 어떤 div 태그를 찾고, 그 div 태그에 포함된 태그들의 리스트를 얻는 코드입니다.
```soup.find("div").children # span, p, img 태그를 갖는 리스트를 얻습니다.```

> Name : 어떤 태그의 이름을 알고 싶다면 name 속성을 이용할 수 있습니다. 태그가 존재하지 않는 경우 None 값을 얻습니다.
```
children = soup.find("div").children
for child in children :
print(child.name)
# span, span, p, img가 각각 출력됩니다.
```

## 실전 크롤링

> 여러 페이지의 기사 제목 수집하기

- 동아스포츠의 연예부 기사의 제목 부분을 크롤링해보려고 합니다.

    1. 사이트의 하단에서 버튼을 눌러 페이지를 이동할 수 있습니다.
        - 1페이지부터 5페이지까지의 기사 제목을 크롤링하려고 합니다.
        - 이 사이트는 URL의 쿼리 부분에서 p의 값에 따라 페이지가 결정됩니다.
        - 한 페이지에 기사가 20개씩 존재하므로 p=1이면 1페이지, p=21이면 2페이지와 같은 식입니다.
        - https://sports.donga.com/ent?p=1
        - URL을 문자열의 덧셈 연산으로 만드실 수도 있지만,
        - requests.get 함수의 params 매개변수로 쿼리 변수를 추가할 수 있습니다

    2. 각 기사의 href 수집
        - href는 a 태그의 속성으로 존재하며 크롤링된 a 태그에 접근하여 얻을 수 있습니다.

> 네이트 최신뉴스 href 수집하기

-  위와 마찬가지로 a태그의 href 속성을 크롤링합니다.

> sbs 뉴스 최신 기사 목록의 내용 수집하기

- sbs 뉴스의 최신 기사 목록의 href를 추출하고 href로 접근할 수 있는 기사들의 내용을 추출해봅니다.
- 각 기사의 href 주소를 얻는 get_href 함수와 기사의 내용을 얻는 crawling 함수를 각각 올바르게 구현해주세요.

>  네이버 뉴스 다양한 섹션의 속보 기사 href 추출하기

- URL의 쿼리 부분에서 sid1의 값에 따라 섹션이 결정됩니다. 어떤 섹션을 크롤링할지는 input 함수로 입력하세요.
https://news.naver.com/main/list.nhn?sid1=100

    1.  쿼리와 함께 get 요청을 담고 있는 requests 객체를 반환하는 get_request 함수와,
    2. 섹션별로 나뉘어진 목록에 있는 기사들의 href를 추출하는 get_href 함수를 올바르게 구현하세요.

> 다양한 섹션의 속보 기사 내용 추출하기

- 기사의 href에서 내용을 추출할 때, 본문 영역은 태그가 없습니다.
- 따라서, 기사 본문을 싸고 있는 div 태그의 children을 얻고,  각 children의 name이 None인 요소만 추출해야 합니다.
- 그 뿐만 아니라 HTML 문서에 적혀있는 주석도 걸림돌이 될 수 있으므로 어려울 수 있는 실습입니다.

```
import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    # 기사에서 내용을 추출하고 반환하세요.
    div = soup.find('div', class_="_article_body_contents")
    
    result = div.get_text().replace('\n', '').replace('flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}', '').replace('\t', '')
    
    return result

def get_href(soup) :
    # 각 분야별 속보 기사에 접근할 수 있는 href를 리스트로 반환하세요.
    result = []
    ul = soup.find("ul", class_="type06_headline")
    for a in ul.find_all("a", class_="nclicks(fls.list)") :
        result.append(a["href"])
        
    return result
    

def get_request(section) :
    # 입력된 분야에 맞는 request 객체를 반환하세요.
    # 아래 url에 쿼리를 적용한 것을 반환합니다.
    custom_header = {
        'referer' : 'https://www.naver.com/',
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    
    url = "https://news.naver.com/main/list.nhn"
    
    sections = {
        "정치" : 100,
        "경제" : 101,
        "사회" : 102,
        "생활" : 103,
        "세계" : 104,
        "과학" : 105
    }
    
    req = requests.get(url, headers = custom_header, params = {"sid1" : sections[section]}) # params 매개변수를 올바르게 설정하세요.
    
    return req

    

def main() :
    custom_header = {
        'referer' : 'https://www.naver.com/',
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    
    list_href = []
    result = []
    
    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')
    
    req = get_request(section)
    soup = BeautifulSoup(req.text, "html.parser")
    
    list_href = get_href(soup)
    
    for href in list_href :
        href_req = requests.get(href, headers = custom_header)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))
    print(result)


if __name__ == "__main__" :
    main()
```

> 네이버 영화 페이지 특정 영화 리뷰 추출하기

- 이번에는 정보를 얻고자 하는 영화의 제목이 입력으로 주어지고, 해당 영화에 대한 리뷰 결과를 보여주어야 합니다.
- 이를 위해 get_url, get_href, crawling 세 개의 함수를 올바르게 구현해주셔야 합니다.

    1 .get_url은 영화 제목을 입력받고, 해당 제목을 검색하였을 때 나오는 URL을 반환해야 합니다.
        - requests.get 메소드의 params 매개변수를 이용해도 되지만,이번에는 문자열의 결합을 이용하는 편이 더 간편하기 때문에 get_url은 문자열의 결합을 이용하여 URL을 만듭니다.
    2. get_href는 검색 결과, 가장 위에 있는 영화의 href를 반환합니다.
    3. 마지막으로 crawling 함수를 구현하여 get_href에서 얻은 영화의 href로 접근하고, 해당 영화의 리뷰 목록을 크롤링하세요.
```
import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    # 1장 실습의 영화 리뷰 추출 방식과 동일합니다.
    result = []
    ul = soup.find("ul", class_="rvw_list_area")
    
    for li in ul.find_all("li") :
        result.append(li.find("strong").get_text())
        
    return result
    
def get_href(soup) :
    # 검색 결과, 가장 위에 있는 영화로 접근할 수 있는 href를 반환하세요.
    ul = soup.find("ul", class_="search_list_1")
    
    a = ul.find("a")
    
    href = a["href"].replace("basic", "review")
    
    return "https://movie.naver.com/" + href

def get_url(movie) :
    # 입력된 영화를 검색한 결과의 url을 반환하세요.
    return f"https://movie.naver.com/movie/search/result.nhn?query={movie}&section=all&ie=utf8"
    
def main() :
    list_href = []
    
    custom_header = {
        'referer' : 'https://www.naver.com/',
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    
    # 섹션을 입력하세요.
    movie = input('영화 제목을 입력하세요. \n  > ')
    
    url = get_url(movie)
    print(url)
    req = requests.get(url, headers = custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    
    movie_url = get_href(soup)
    print(movie_url)
    
    href_req = requests.get(movie_url)
    href_soup = BeautifulSoup(href_req.text, "html.parser")
    
    list_href = crawling(href_soup)
    print(list_href)
    


if __name__ == "__main__" :
    main()
```
