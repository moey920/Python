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
