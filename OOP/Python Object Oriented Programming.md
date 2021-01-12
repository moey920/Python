# 파이썬 객체지향 프로그래밍

## 함수

### A function is a block of code which only runs when it is called.
> 함수 호출이 발생할 때만 함수가 실행된다.
```
def say_hello():
    print(“Hello! elice”)
```

### Calling a Function
> 함수 호출하기
```
say_hello()
```

### Return Values
> 값을 리턴하는 함수
```
def say_hello():
    return “Hello! elice”

print(say_hello())
```

### Default values
> 기본 값을 설정하여 활용하는 함수
```
def cal_krw(dollar, currency=1100): # Default 값은 뒤쪽에 입력해줘야한다.
    return dollar*currency


krw = cal_krw(10, 1500)
print(krw)
```

### Arguments
```
def say_hello(name):
    print(“Hello! ” + name)

say_hello(“elice”)
```

### Arbitrary Arguments, *args 
> 임의 전달인자 함수(*)
```
def say_hello(*name):
    print(“Hello! ” + name[0])

say_hello(“elice”, “kim”)
```
```
def print_fname(*args): # *의 의미 : 여러개의 인자를 받을 것이다, 튜플(순서가 있는 리스트)로 받는다.
    print("fname : " + args[0]) # args가 100만개가 들어와도 첫번째 인덱스(first name)만 출력하겠다.

print_fname("John", "Kim")
print_fname("Hoonseok", "John", "Kim")
```

### Arbitrary Keyword Arguments, **kwargs
> 딕셔너리 형태로 받아오는 함수
```
def say_hello(**name):
    print(“Hello! ” + name[“fname”])
say_hello(fname=“elice”, lname=“kim”)
```
```
def print_fname(**kwargs):
    print("fname : " + kwargs['fname']) #Key와 Value를 활용할 수 있다.
    print(type(kwargs)) # Dictionary


print_fname(fname="John", mname="hoo") # 키-밸류, 키-밸류
```

### 함수 활용 실습
```
# 사용자의 핸드폰 번호가 유효한지 확인하는 함수를 만들어 봅시다.
# 유효한 핸드폰 번호는 010으로 시작하며, 010을 포함해서 11자리 숫자입니다.
# .split(""), list[0:3], True 활용

def is_valid_phone_number(phone_number):
    f_number = phone_number[0:3] # f_number == "010"
    split_number = phone_number.split("-") # ['010','1234','1234']
    pure_number = ''
    for i in range(len(split_number)) :
        pure_number += split_number[i]
    print(pure_number)
    if f_number == '010' and len(pure_number) == 11 :
        return True


phone_numbers = ["010-1234-1234", "0101234123",
                 "010-12341234", "017-123-1234",
                 "016-1231234", "010-123-1234",
                 "+82-1234-1234"]

for phone_number in phone_numbers:
    if is_valid_phone_number(phone_number):
        print("{} \tis valid number".format(phone_number))
```


## 클래스
- 클래스(Class) : 별모양 과자 틀
- 객체(Object) : 별모양 과자(틀을 이용한 다양한 별모양 과자들이 가능) 2단 케익 별과자 등
- 인스턴스(Instance) : 객체를 클래스의 인스턴스라고 한다. 
- 메소드(Method) : 클래스 안의 함수

    - 예시 :
    ```
    Class person :
        팔 다리 몸
        소화기관 등
        기능(method)
            걷는다
            말한다

    Class person를 이용하여 jone, jane 등을 만든다.

    Class person => John Kim(person) => jr.John kim(John kim) : 상속
    ```
- 상속

### Classes provide a means of bundling data and functionality together. 
```
Class Greeting:
    def say_hello():
        return ‘Hello! elice” 
```

### Class instantiation uses function notation
```
Class Greeting:
    def say_hello():
        return ‘Hello! elice”

greet = Greeting()
```

### When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance
```
Class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5) 
```

### Method vs Function

    - Method
    ```
    Class Greeting:
        def say_hello():
            return ‘Hello! elice” 
    ```

    - Function
    ```
    def say_hello():
        return ‘Hello! elice”
    ```


## 상속과 다형성

### Inheritance allows to define a class that inherits all the methods and properties from another class
```
Class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname 
```
```
Class Student(Person):
    pass
```

### Overriding is the property of a class to change the implementation of a method provided by one of its base classes
```
Class Person:
    def say_father():
        print(“Father”)
```
```
Class Baby(Person):
    def say_father():
        print(“Papa”)
```

## 모듈과 패키지

### A module is a file containing Python definitions and statements. 
```
#mod.py
def say_hello():
    print(“Hello! elice”)
```
```
#main.py
import mod
mod.say_hello()
```

### Packages are a way of structuring Python’s module namespace by using “dotted module names”
```
sound/
    __init__.py
    formats/
        __init__.py
        wavread.py
        …
```
```
import sound.formats.wavread
```
