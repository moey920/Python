# 클래스 입문

## 클래스에 대하여

### 클래스를 사용하는 이유 : 논리적인 프로그램을 설계하기 위해

### 클래스란? 나타내고자 하는 개념의 **설계도**

### 예시

| 저장해야 하는 **데이터** | 할 수 있는 **조작** |
|:---:|:---:|
| 작성자 | 리액션(좋아요) |
| 내용 | 댓글 달기 |
| 작성시간/날짜 | 내용 수정하기 |
| 이미지(없을 수도 있다) | 공유하기 |
| 링크(없을 수도 있다) | 사진 추가하기 |

### 클래스와 인스턴스

| 클래스 | 인스턴스 |
|:---:|:---:|
| 어떤 데이터가 있는지 | 그 클래스로 만든 실제 예시 |
| 어떤 조작을 할 수 있는지 | - |
| 어떤 제약조건들이 있는지 | - |
| 명시한 추상적인 설계도 | - |

| 게시물 클래스 | 게시물 인스턴스 |
|:---:|:---:|
| 게시물 하나에 최대 20장의 사진 | elice의 7월 17일 게시물 |
| 좋아요, 슬퍼요, 최고에요 | 최XX님의 1월 3일 게시물 |
| 댓글을 달 수 있음 | 리X왕 김X뷰의 7월 2일 게시물 |
| 작성자가 공유 여부를 설정 가능 | - |

### 클래스 선언

```
class Post:
    author = None # 속성들
    comments = []
    likes = 0
    content = "What are you doing?"
    ...
    def like(self, user): # 메소드(클래스 내의 함수, 메소드는 항상 첫 인자로 self를 받는다.)
        self.likes += 1
        user.liked_posts.append(self)
```

### 생성자

> 모든 클래스의 가장 기본이 되는 메소드, **인스턴스가 처음 만들어질 때 어떻게 세팅할 것인지** 결정

```
class Post:
    def __init__(self, author, content):
    self.author = author
    self.content = content
```

#### self

self : 클래스 내부의 속성/메소드에 접근할 때 ```self.author```
클래스이름 : 클래스 외부에서 속성/메소드에 접근할 때 ```post.author```

class Post:
    def __init__(**self**, author, content):
    **self**.author = author
    **self**.content = content 

### 생성자의 매개변수 vs.클래스의 속성

> 생성자의 매개변수 : 인스턴스 생성 시 입력 

> 클래스의 속성 : 실제로 데이터가 저장되는 이름

## 속성을 만들 때 주의할 점(모순 제거)

> 같은 내용을 나타내는 속성이 2개

```
class Post: 
    def __init__(self, author, content):
    self.likes = 0
    self.liked_users = []

my_post = Post("elice", "I love coding!")
my_post.likes += 1 # 좋아요 개수는 올라갔는데, liked_users에 리스트가 추가되지 않으면 버그가 생긴다.
```

> 메소드 만들기(해결 방법)
```
class Post:
    def like(self, user):
        self.liked_users.append(user) # 좋아요 한 유저 리스트 추가

    def num_likes(self): # 메소드를 속성처럼 사용
        return len(self.liked_users) # 좋아요 누른 유저 수 return
```

## 클래스 다듬기

### 원하지 않는 값 배제

```
class Post:
    def __init__(self, author, content):
        ...

my_post = Post("elice", 1457) # content에 문자를 받을 순 있어도 정수를 받으면 이상하기 때문에
my_post.like(["Hello", "World"]) # like 메소드는 user를 하나만 받는다.
```

```
class User:
    def __init__(self, year_of_birth):
        if type(year_of_birth) is not int: # 태어난 해의 타입이 정수가 아니라면
            return # 인스턴스 생성하지 않고 끝내겠다.
 ```

 ```
 class Post:
    def __init__(self, author, content):
        if not isinstance(author, User):
            return
        if type(content) is not str:
            return 
 ```

 ```
 class User:
    def __init__(self, year_of_birth):
        if year_of_birth > 2005:
            raise Exception("Too young") 
 ```
