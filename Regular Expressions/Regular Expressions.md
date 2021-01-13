# 정규표현식

- 복잡한 문자열을 처리할 때 사용하는 도구
- 특정 프로그래밍 언어에 종속된 문법을 가진 것이 아니라 문자열을 처리하는 곳이라면 폭넓게 사용 가능한 도구
- 파이썬의 기본 모듈 중 re모듈이 정규표현식을 지원

### 정규표현식이 없다면?

> 보안을 위해 고객 정보 중 전화번호 가운데 자리의 숫자는 * 문자로 변경하세요
```
text = '''
Elice 123456-1234567 010-1234-5678
Cheshire 345678-678901 01098765432
'''
```
    이 문제를 정규식을 사용하지 않고 풀려면 매우 복잡하게 풀어야 합니다.

    - 전체 텍스트를 공백 문자를 기준으로 나눈다.
    - 나누어진 문자열이 전화번호 형식인지 점검한다.
    - 전화번호를 다시 나누어 가운데 자리의 숫자를 *로 변환한다.
    - 나눈 문자열을 다시 합쳐 전화번호를 완성한다.

### 정규표현식을 이용한다면?

> 원하는 형식의 문자열을 검색할 때 메타문자와 수량자 등 다양한 패턴을 사용하여 매치하고, 
그룹핑을 이용하여 원하는 부분만 골라내고 re모듈의 메서드로 문자열을 수정할 수도 있다.