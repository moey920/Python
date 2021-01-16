# 워드클라우드

## 워드클라우드란?

> 데이터에서 단어 빈도를 분석하여 시각화하는 기법

## 워드클라우드 준비

- 워드클라우드를 그리기 위해서 텍스트 데이터가 필요합니다.
- 네이버 뉴스 기사의 내용의 텍스트 데이터로 워드클라우드를 그려보도록 하겠습니다.

### 영어 문장 나누기

- 워드클라우드의 각 단어는 빈도에 따라 크기가 결정됩니다.
- 크기가 큰 단어일수록 빈도가 높습니다.
- 영어 문장의 경우, 공백을 기준으로 나누어 각각의 단어를 얻을 수 있습니다.

## [실습1] : 영어 문장 나누기
워드 클라우드는 텍스트 데이터에서 단어가 등장한 횟수를 기준으로 표현하는 그림이므로, 주어진 텍스트를 단어 단위로 나누어야 합니다.
text.py 파일에 준비된 문자열이 있습니다. 주어진 문자열을 공백 문자를 기준으로 나누고, 각 단어별 횟수를 센 결과를 반환하는 count_word_freq 함수를 구현해보세요.
count_word_freq 함수는 문자열을 입력받고, 문자열 내의 단어들이 몇 번 등장하는지 센 결과를 반환합니다.

> 지시사항
1. 필요한 모듈
```
from collections import Counter
from string import punctuation
```
count_word_freq 함수를 구현하기 위해서, collections와 string 모듈의 Counter, punctuation을 불러와야 합니다.
Counter는 주어진 리스트에서 특정 값이 몇 번 등장하는지 세는 역할을 하고,
pucntuation은 특수문자들이 담겨있는 문자열입니다. punctuation으로 문자열 데이터에서 특수문자를 제거하려고 합니다.

2. 전처리
```
_data = data.lower()
```
문자열들을 모두 소문자로 바꿉니다.
```
for p in punctuation :
    _data = _data.replace(p, "")
```
문자열에 들어있는 특수문자를 모두 제거합니다. **punctuation은 특수문자들이 담겨 있는 문자열 변수**입니다.

3. 단어 나누기
```
_data = _data.split()
```
split 함수를 이용하여 공백 문자를 기준으로 문자열을 나눕니다.

4. 단어 세기
```
counter = Counter(_data)
```
문자열을 나눈 리스트를 이용하여 Counter 객체를 만들어줍니다.
```
return counter
```

### 전체 코드
```
from collections import Counter # 단어 숫자 세기
from string import punctuation
from text import data # 문장 가져오기

def count_word_freq(data) :
    #--------------전처리 과정-------------------------#
    for p in punctuation :
        data = data.replace(p,"") # 모든 특수문자를 ""으로 대체
    data = data.replace('-', "")
        
    _data = data.lower() # 소문자로 변경
    #---------------공백 기준으로 단어 나누기---------#
    _data = data.split()
    
    counter = Counter(_data)
    
    
    
    return counter

if __name__ == "__main__" :
    print(count_word_freq(data))
```


## [실습2] : 워드클라우드 출력하기

> 지시사항 : 아래 지시사항에 적힌 예시 코드를 참고하여 워드클라우드를 출력하는 함수 create_word_cloud를 구현해보세요.
create_word_cloud 함수는 문자열 데이터를 입력받고, 해당 문자열의 워드클라우드를 출력합니다.
```
from wordcloud import WordCloud
```
워드클라우드를 그리기 위해서 WordCloud모듈이 필요합니다.
WordCloud의 fit_words라는 함수가 단어들의 빈도 수가 담긴 딕셔너리를 매개변수로 받아, 워드클라우드를 그리는 역할을 합니다.

1. 단어 빈도수 얻기
```
counter = count_word_freq(data)
```
문자열 data에 들어있는 단어들의 빈도수를 얻어 count에 저장합니다.

2. 워드클라우드 객체 생성하기
```
cloud = WordCloud(background_color='white')
```
배경색이 흰색인 WordCloud 객체를 생성합니다.

3. 워드클라우드 그리기
```
cloud.fit_words(counter)
```
단어들의 횟수를 기반으로 워드클라우드를 생성합니다.
```
cloud.to_file('cloud.png')
elice_utils.send_image('cloud.png')
```
생성한 워드클라우드를 그림 파일로 저장하고, 엘리스 플랫폼에서 출력합니다.

### 전체코드
```
from wordcloud import WordCloud # 워드 클라우드를 만드는 라이브러리
from wordcloud import STOPWORDS # 불의어가 모아져있는 리스트
from count import count_word_freq
from text import data

from elice_utils import EliceUtils
elice_utils = EliceUtils()


def create_word_cloud(data):
    counter = count_word_freq(data)
    #코드를 작성하세요.
    cloud = WordCloud(background_color = 'white', stopwords = STOPWORDS)
    cloud.fit_words(counter)
    cloud.to_file('cloud.png') # 결과를 '~'로 변환해라
    elice_utils.send_image('cloud.png')

if __name__ == "__main__":
    create_word_cloud(data)
```

## [실습3] :네이버 뉴스 기사 내용 크롤링하기

> 지시사항
main 함수의 url 변수에 네이버 뉴스 기사 url을 넣어 해당 기사의 내용을 크롤링하실 수 있습니다.

- Tip!
실행결과 화면이 뜨지 않을 때 앞서 배웠던 custom_header를 작성하고
```
custom_header = {
    'referer' : 'http://http://finance.daum.net/quotes/A048410#home',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'  }
```
requests객체의 get()에 적용해보세요!
```
req = requests.get(url, headers = custom_header)
```

### 전체 코드
```
import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    
    div = soup.find("div", class_='_article_body_contents').get_text().replace('\t','').replace('  ','').replace('\n','').replace('// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}','')
    return div


def main():
    custom_header = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=001&aid=0011575988"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    
    print(crawling(soup))


if __name__ == "__main__":
    main()
```

## [실습4] : 네이버 뉴스 기사 워드클라우드 출력하기

> 이전 실습에서 그렸던 워드클라우드의 문제점은 단어에 어미와 조사가 붙어 분석이 왜곡되는 것입니다.

- ‘대통령이’ 와 ‘대통령은’은 둘 다 대통령이라는 공통된 키워드로 집계되어야 합니다.
- 잘, 무척 등 의미를 도출하기 어려운 부사들이 있어 텍스트 내에서 의미를 도출하기 쉬운 명사만 추출하고자 합니다.
- 워드 클라우드는 키워드를 찾는 것이 중요하므로, 조사 등이 붙지 않은 형태소들 중 명사들을 결과로 워드클라우드를 그리려고 합니다.

> 형태소 추출

- 이를 추출하기 위해 한국어 단어에 붙는 어미와 조사를 제거하고, 단어의 어근만 집계되도록 하는 형태소 추출 과정이 필요합니다.
- 이 과정에서 한국어 자연어 처리 라이브러리인 mecab을 사용합니다.

> 지시 사항

1. mecab = MeCab() 으로 mecab 객체를 생성할 수 있습니다.

2. mecab.morphs(text) 함수는, 매개변수로 들어온 문장을 형태소별로 나누어 리스트로 반환합니다.

3. mecab.nouns(text) 함수는, 매개변수로 들어온 문장을 형태소별로 나누었을 때 명사만 추출하여 리스트로 반환합니다.

4. mecab.pos(text) 함수는, 매개변수로 들어온 문장을 형태소별로 나누고, 각 형태소별로 품사에 대한 정보까지 포함하여 반환합니다.

주어진 text 변수, 또는 자유롭게 text 변수의 값을 설정하여 mecab 모듈의 함수를 사용해보세요.

##[실습5]
형태소 추출하기

```
from mecab import MeCab
mecab = MeCab()


text = "광화문역 주변에 있는 맛집을 알고 싶어요. 정보를 얻을 수 있을까요?"

# 1. 형태소 별로 나눠 출력해보기
print(mecab.morphs(text))

# 2. 명사만 출력해보기
print(mecab.nouns(text))

# 3. 형태소 별로 나누고 품사 출력해보기
print(mecab.pos(text))
```

```
from collections import Counter
from string import punctuation
import mecab
mecab = mecab.MeCab()

def count_word_freq(data) :
    _data = data.lower()
    
    for p in punctuation :
        _data = _data.replace(p, "")
    
    # 명사를 추출하세요.
    # _data = mecab.morphs(_data)
    _data = mecab.nouns(_data)

    counter = Counter(_data)
    
    return counter
```

## [실습6, 7] : 여러 개의 기사 내용 크롤링하기
하나의 기사만으로는 단어의 빈도수를 파악하기 어려울 수 있습니다.
기사의 분량, 기자의 성향 등 여러 요인이 반영되기 때문입니다.

따라서 공통된 주제에 대한 여러 기사의 텍스트 데이터를 같이 분석하면
효과적인 워드클라우드를 출력할 수 있습니다.

네이버 뉴스 페이지는 관련된 주제의
여러 기사를 묶어서 보여주고 있습니다.

각각의 분야(정치, 경제, 사회, 생활, 세계, 과학)에 대해
페이지 최상단에 보이는 주제에 해당하는 기사들의
텍스트 데이터로 워드클라우드를 출력해봅시다.

> 지시사항
- 네이버 뉴스 페이지는 관련된 주제에 따라 여러 개의 기사를 묶어서 보여주고 있습니다.
- 이번에는 각 분야(예 : 정치, 경제 등) 별 페이지에서 가장 상단에 보이는 주제(예 : 트럼프, 알지만 말할 수 없어) 에 해당하는 기사들의 텍스트 데이터를 크롤링하세요.

```
import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # 기사에서 내용을 추출하고 반환하세요.
    div = soup.find('div', class_="_article_body_contents")
    
    result = div.get_text().replace('\n', '').replace('// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}', '').replace('\t', '')
    
    return result


def get_href(soup): # 4개의 본문을 가져오는 방법
    result = []
    
    cluster_body = soup.find("div", class_="cluster_body") # 안에 기사 4개존재
    cluster_texts = cluster_body.find_all("div", class_='cluster_text')
    
    for cluster_text in cluster_texts :
        a = cluster_text.find("a")
        result.append(a["href"])
    
    # print(result)
    return result


def get_request(section, custom_header):
    url = "https://news.naver.com/main/main.nhn"
    section_dict = { "정치" : 100,
                     "경제" : 101,
                     "사회" : 102,
                     "생활" : 103,
                     "세계" : 104,
                     "과학" : 105 }
    return requests.get(url, params={"sid1":section_dict[section]}, headers=custom_header) # url의 시드 값을 받는다. 1개의 리스트에 4개의 url


def main():
    custom_header = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    list_href = []
    result = []
    
    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')
    
    req = get_request(section, custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    
    list_href = get_href(soup)
    
    for href in list_href :
        href_req = requests.get(href, headers=custom_header)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))
    print(result)


if __name__ == "__main__":
    main()
```


## [실습8] : 여러 기사 크롤링 후 워드 클라우드 만들기
```
import requests
from bs4 import BeautifulSoup
from wc import create_word_cloud


def crawling(soup):
    # 기사에서 내용을 추출하고 반환하세요.
    div = soup.find('div', class_="_article_body_contents")
    
    result = div.get_text().replace('\n', '').replace('// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}', '').replace('\t', '')
    
    return result


def get_href(soup):
    result = []
    
    cluster_body = soup.find("div", class_ = "cluster_body")
    
    for cluster_text in cluster_body.find_all("div", class_ = "cluster_text") :
        result.append(cluster_text.find("a")["href"])
    
    return result


def get_request(section, custom_header):
    url = "https://news.naver.com/main/main.nhn"
    section_dict = { "정치" : 100,
                     "경제" : 101,
                     "사회" : 102,
                     "생활" : 103,
                     "세계" : 104,
                     "과학" : 105 }
    return requests.get(url, params={"sid1":section_dict[section]}, headers=custom_header)


def main():
    custom_header = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    list_href = []
    result = []
    
    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')
    
    req = get_request(section, custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    
    list_href = get_href(soup)
    
    for href in list_href :
        href_req = requests.get(href, headers=custom_header)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))
    
    text = " ".join(result)
    create_word_cloud(text)


if __name__ == "__main__":
    main()

```


## [실습9] : 여러 페이지를 url을 통해 이동해서 최종페이지로 이동하는 코드(link따라 들어가기)
```
import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # 기사에서 내용을 추출하고 반환하세요.
    div = soup.find('div', class_="_article_body_contents")
    
    result = div.get_text().replace('\n', '').replace('// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}', '').replace('\t', '')
    
    return result
    

def get_href(soup, custom_header): # url을 한번 타고 들어가서 상세 페이지의 n개의 기사를 크롤링 한다.
    result = []
    
    cluster_head = soup.find("h2", class_="cluster_head_topic")
    href = cluster_head.find("a")["href"]
    
    url = "https://news.naver.com" + href
    
    req = requests.get(url, headers = coutom_headers)
    new_soup = BeautifulSoup(req.text, "html.parser") # 새로운 url에서 정보를 가져오는 방법, 첫 soup로 뉴스 섹션별 홈페이지로 이동한거고, 두번째 soup로 해당 섹션의 메인 관련뉴스 url을 통해 들어온 것이다.
    
    
    return result


def get_request(section, custom_header):
    url = "https://news.naver.com/main/main.nhn"
    section_dict = { "정치" : 100,
                     "경제" : 101,
                     "사회" : 102,
                     "생활" : 103,
                     "세계" : 104,
                     "과학" : 105 }
    return requests.get(url, params={"sid1":section_dict[section]}, headers=custom_header)


def main():
    custom_header = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    list_href = []
    result = []
    
    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')
    
    req = get_request(section, custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    
    list_href = get_href(soup, custom_header)
    
    for href in list_href :
        href_req = requests.get(href, headers=custom_header)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))
    print(result)


if __name__ == "__main__":
    main()
```
[실습10]
더 많은 기사로
워드클라우드 출력하기
