# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 기본 명령어들!
# ## 실행
#     Ctrl  + Enter : 현재 셀 실행
#     Shift + Enter : 현재 셀 실행 후 아래 셀 추가
#     Alt   + Enter  : 아래 셀 추가
#     
#     a : 위로 셀 추가
#     b : 아래로 셀 추가
#     dd : 현재 셀 삭제
#     
# ## 셀 편집 ( 복사 , 자르기 , 등)
#     m : 마크다운으로 변경
#     y : 코드로 변경
#     C : 복사
#     X : 자르기
#     v : 아래로 붙여넣기
#     z : 셀 삭제 및 자르기 되돌리기 ( 윈도우의 "Ctrl + Z" )
#     Shift + v : 위로 붙여넣기
#     Shift + m : 아래 셀과 합치기 ( merge)
#     
# ## 보이는 것들
#     o : 실행 결과 창 숨기기 및 펼치기
#     Shift + l : 셀라인 표시
#     
# ## 코드모드
#     esc : 선택모드로 변경 ( 셀 나오기 )
#     ctrl + / : 주석
#     ctrl + shift + - : 셀 나누기
#

c = 1+3
print(c)


def xx( c ):
    c = c * 2
    return c


print(xx(c))


def yy( x,y ):
    return x-y


yy(10,4) >= 5

print(type(7/7))

# # 튜플(Tuple) , 리스트(List), 셋(Set) , 딕셔너리(Dict)    

# ## 튜플 ( Tuple )  
#
# ### 기본 개념
#     iterable한 변수 ( 반복 가능한 객체 ) 
#     - 요소의 삽입삭제를 하지 못 한다 --> Immutable ( 불변성 ) 
#     - Append,Remove와 같은 메소드가 없다.
#     - Tupple + Tupple형식으로 추가할 수 있지만, 억지로 하는 것 이기 때문에 권장하지는 않는다.
#     - 만약 하고 싶다면 " T3 = T1 + T2 "를 하여 새로 할당하는 방식으로 만들 수 있다.
#     - 서로 다른 Data Type을 담을 수 있다.
#         Ex) ('one' ,1,3)
#     
# ### 사용방법
#     - "()" 을 이용하여 묶어준다!

# 튜플 예시
t1 = (1,2,3,4,5)
print(type(t1))

# ## 리스트 ( List )
#
# ### 기본 개념
#     iterable한 변수 ( 반복 가능한 객체 ) 
#     - 튜플과 유사하다 하지만, 요소의 삽입 삭제가 가능하다 --> 가변성 ( Mutable)
#     - append , remove 메소드를 이용하여 삽입삭제를 할 수 있따.
#     - List + List 형식으로 요소를 추가할 수 있다.
#     - 서로 다른 Data Type을 담을 수 있다.
#         Ex) ['One' , 1 ]
#         
# ### 사용방법
#     - " [] "로 묶어준다!   

l1 = [1,2,3,4,5]
print(type(l1))

# ## 셋 ( Set )
# ### 기본 개념
#     - 순서가 없고, 중복이 불가한 Collection 자료형
#     - 요소의 삽입 삭제가 가능하다 --> 가변성 ( Mutable)
#     - add (값추가) ,update ( 여러요소 추가 ) ,remove (삭제 ) ,pop (값 리턴 후 삭제) ,clear (전체삭제) ,등
#     
# ### 사용 방법
#     -" { } " 로 묶어준다.

s1 = {1,2,3,4,5}
print(type(s1))

# ## 딕셔너리 ( Dict )
# ### 기본 개념
#     - 셋 (Set) 클래스를 이용하여 구현함.
#     - 그럼으로 Set과 동일하게 중복이 불가한 Collection 자료형이다. Mutable하다
#     - 모양 : Key : value로 구성되어있다.
#     - Key값은 중복이 불가하다!!
#     
# ### 사용 방법
#     -{'one' : 1 } --> 1:1 맵핑!
#

d1 = {'one' : 1 }
print(type(d1))

# # 조건문 ( if ... elif .... else)
#
# ### 기본 개념
#     - 연산중 조건을 판별하기 위해 사용한다. ( 만약에... 아니면..  그 외에.. )
#     - 조건식에 and 혹은 or 을 삽입하여 조건식을 만들 수 있다
#         if a and b :       if a or b :
#     
# ### 사용방법
#     - 형식은 아래와 같다
#     if 조건1  :
#         연산
#     elif 조건 :
#         연산
#     else :
#         연산

    i = 80
    
    if i >=90 :
        print('A')
    elif i >= 80 and i < 90 :
        print('B')
    elif i >= 70 and i < 80 :
        print('C')
    elif i >= 60 and i < 70 :
        print('D')
    else:
        print('F')

# # 반복문

# ## Range
# ### 기본 개념
#     -범위를 지정하여 순차적으로 값을 반환해주는 메소드
#
# ### 사용 방법
#     - range ( 시작 , 끝 , 등차 )  이 때 등차는 생략 할 수 있다.

# +
print('등차가 없는 range 예시')
a = []
for i in range(1 , 10):
    a.append(i)
print (a)    

a = []
print('등차가 있는 range 예시')
for i in range(1 , 10 , 2):
   a.append(i)
print (a)   
# -

# ## for문
# ### 기본 개념
#     -대표적인 반복문이다.
#     -일반적으로 끝나는 지점을 알 때 사용한다.
#     
# ### 사용 방법
# #### 방법1
#     for i in x:
#         연산
# #### 방법2
#     for i in range(5) : 
#         연산        
# #### 방법3
#     for i in range(len(x):
#         연산
#     

# + code_folding=[]
ss= 0
for i in range ( 1, 10001):
    ss += i
print(ss)

# + active=""
# 쉬어가는 문제!
#
# 90 80 60 70 99 를 가진 리스트가 있다.
# 위 리스트중 90점을 넘으면 A, 80 점을 넘으면 B , 70점을 넘으면 C, 60점을 넘으면 D , 나머지는 F를 주는 코드를 구현하여라.    

# +
s = [90,80,60,70,99]

for i in s:
    if i >=90 :
        print('A')
    elif i >= 80 and i < 90 :
        print('B')
    elif i >= 70 and i < 80 :
        print('C')
    elif i >= 60 and i < 70 :
        print('D')
    else:
        print('F')
        
# -

# 문제 2 
# 범위 : range (0, 10001)
# 문제 : 3의 배수이면서 2의 배수인 값의 합을 구하여라

# +
sum = 0

for i in range(0,10001):
    if i % 3 == 0 and i % 2 ==0:
        sum += i        
print(sum)
# -

# 문제 3
# 1~1000 까지 숫자에서 3의 배수를 가져오고
#  가져온 3의 배수의 3번째 자리들만 가져와서 각각 제곱한
#  튜플을 만드세요

a = []
for i in range(1,1001):
    if i%3 == 0 :
        a.append(i)
b = []
for i in range(len(a)):
    if i %3 == 0:
        b.append([a[i],a[i]**2])
print(b)
    

# +
a = []
for i in range(3,1001 , 9):
    a.append((i,i**2))
c = tuple(a)
print(c)
type(c)

## 딕셔너리로 구현
dic1 = {}
for i in range(3,1001 , 9):
    dic1[i] = i**2
print(dic1)

# -

# 구구단을 만들어보자~!~!~@~~~~

for i in range(2,10):    
    for j in range(1,10):
        print(i,'*',j,'=',i*j)
        

import random
# from randomn import randint

# 무작위 int 값 출력 (시작, 끝)
random.randint(1,100)

#보유한 요소중 랜덤하게 1개 추출
x = [2,3,4,5]
random.choice(x)

#  1~100 숫자 중 랜덤하게 100개의 수를 입력받아라

# +
ans = []

for i in range(1,1000):
    x = random.randint(1,100)
    if (x in ans) == False:
        ans.append(x)
print(len(ans))
print(ans)

# -

print("    /\ \n )  ( ')\n(  /  )\n \(__)|")
