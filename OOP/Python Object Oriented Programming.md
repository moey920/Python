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
```
def say_hello():
    return “Hello! elice”

print(say_hello())
```

### Arguments
```
def say_hello(name):
    print(“Hello! ” + name)

say_hello(“elice”)
```

### Arbitrary Arguments, *args
```
def say_hello(*name):
    print(“Hello! ” + name[0])

say_hello(“elice”, “kim”)
```

### Arbitrary Keyword Arguments, **kwargs
```
def say_hello(**name):
    print(“Hello! ” + name[“fname”])
say_hello(fname=“elice”, lname=“kim”)
```

## 클래스

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
