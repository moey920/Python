# 데이터 크롤링

> 크롤링이란? 웹 페이지에서 필요한 데이터를 추출해내는 작업

- 크롤링을 하는 프로그램 : 크롤러
- 웹 페이지는 정보를 HTML 문서로 표현합니다
- 웹 페이지의 HTML을 얻기 위해 requests 라이브러리를,
- 가져온 HTML을 분석하기 위해 BeautifulSoup 라이브러리를 사용합니다.

## BeautifulSoup 라이브러리

> HTML, XML, JSON 등 파일의 구문을 분석하는 모듈, 웹 페이지를 표현하는 HTML을 분석하기 위해 사용합니다

```soup = BeautifulSoup(open("index.html"), "html.parser")```

- HTML 파일로 BeautifulSoup 객체를 만들 수 있습니다. 변수 이름은 관습적으로 soup 라고 짓습니다.
- “html.parser”의 의미는, BeautifulSoup 객체에게 “HTML을 분석해라” 라고 알려주는 의미입니다

```
soup.find("p") # 처음 등장하는 태그 찾기
soup.find_all("p") # 모든 태그 찾기
```

- find(), find_all() 메소드를 이용하여 HTML 태그를 추출할 수 있습니다
- find는 추출한 HTML 태그 하나를, find_all은 HTML 태그를 여러 개 담고 있는 리스트를 얻습니다.

- 출력 예시 : 
```
<p></p>
[<p></p>, <p></p>, ... , <p></p>]
```

### 사용 예시 : div 태그 중, 클래스가 elice인 것만 추출하려면 어떻게 해야 할까요?
```
<!DOCTYPE html>
...
<body>
    <div class="cheshire">
        <p>Don't crawl this.</p>
    </div>
    <div class="elice">
        <p>Hello, Python Crawling!</p>
    </div>
</body> 
```

> # class_ 매개변수에 값을 저장함으로써 특정 클래스를 가진 태그를 추출할 수 있습니다

```
soup.find("div")
soup.find("div", class_="elice")
````

- find로 얻은 결과도 BeautifulSoup 객체입니다. 따라서 find를 한 결과에 또 find를 적용할 수 있습니다. 아래 코드는 div 태그 안에 있는 p 태그를 추출합니다

```soup.find("div", class_="elice").find("p")```

- BeautifulSoup 객체에 get_text 메소드를 적용하면 태그가 갖고 있는 텍스트를 얻을 수 있습니다.

```soup.find("div", class_="elice").find("p").get_text()```

> 특정 id의 값을 추출하고자 하는 경우에는 id 매개변수의 값을 지정할 수 있습니다.

```
soup.find("div")
soup.find("div", id="elice")
```

## requests 라이브러리

> requests : Python에서 HTTP 요청을 보낼 수 있는 모듈

> HTTP 요청이란? 

- GET 요청 : 정보를 조회하기 위한 요청 (예 : 네이버 홈페이지에 접속한다. 구글에 키워드를 검색한다.)
- POST 요청 : 정보를 생성, 변경하기 위한 요청 (예 : 웹 사이트에 로그인한다. 메일을 삭제한다.)

- 예시 : 지정한 URL로 GET 요청을 보냈고, 서버에서는 요청을 받아 처리한 후 result 변수에 응답을 보냅니다.
```
url = "https://www.google.com"
result = requests.get(url)
```

> 
