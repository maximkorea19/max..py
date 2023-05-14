# """ "Hello world" """
# ''' 'Hello worls' '''

################################################
#여러줄의 문자열을 출력하고싶을때\n
#mutilline''' or """
#Life is too short
#You need python
#''' or """
#print(mutilline)

#문자열 길이 구하기(len)
# a = 'You need pyrhon'
# print(len(a))

##############################################################
#문자열 인덱싱(indexing)=가르키다,슬라이싱(Slicing)=잘라낸다
#문자열 인덱싱(indexing)
# a = 'Life is too short, You need python'
#      0         1         2         3
#      0123456789012345678901234567890123
#a = 'Life is too short, you need python'
# (예)print(a[3])=e
#print(a[-3])마이너스는 뒤에서부터
############## 인덱싱은 원하는 곳을 가르켜 골라온다

#문자열 슬라이싱(slicing)
# a = 'Life is too short, You need python'
# b = a[0] + a[1] + a[2] + a[3]
# print(a)='Life'

### 슬라이싱 기법을 간단하게
# a = 'Life is too short, You need python'
# a[:] 괄호 안에 원하는 열 지정해서 출력 가능
##############슬라이싱은 원하는 부분을 잘라내서 가져온다

### 슬라이싱으로 문자열 나누기
#a = '20010331Rainy'
#      0         1
#      0123456789012
#date = a[:8]
#weather = a[8:]
#print(a[:8] + a[8:])

#문자열 바꾸기
#a = 'pithon' ===i를 y 로 바꿔야 되는 상황
#print(a[:1] + 'y' + a[2:])
#########################################################

#문자열 포매팅(formatting)
#문자열 포매팅은이란:문자열 안에 어떤 값을 삽입하는 방법!
#1. 숫자 바로 대입
#print("I eat %d apples." % 3)

##2.문자열 바로 대입
#print("I eat %s apples." % "five")

###3.숫자 값을 나타내는 변수로 대입
# number = 3 <변수>
# print("I eat %d apples." % number)

####4.2개 이상의 값 넣기
# number = 10
# day ="three"
# print("I ate %d apples. so I was sick for %s days" % (number, day))

########문자열 포맷 코드
#  %s=문자열(string)     %d=정수(Integer)    %f=부동소수(floating-point)
#   %s=문자열 이지만 어떤 형태의 값이든 변환해 넣을 수 있음

##### 포매팅 연산자 %d와 % 같이 쓸 때는 %%를 쓴다
# print("Error is %d%%." % 98)

#####포맷 코드와 숫자 함께 사용하기
#1.정렬과 공백
# print("%10s" % "Hi")
# %10s는 갈아거 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 
# 나머지는 공백으로 남겨 두라는 의미이다
# %10s 가 오른쪽 정렬이니까 왼쪽으로 정렬하기 위해서는 -를 붙인다 %-10s

##2.소수점 표현하기
#print("%0.4f" % 3.123456789) 
# 소수점 앞에 0은 공백을 의미하고 뒤에 4는 소수점의 4자리까지만 
#출력하겠다는 의미이다
########################################################################

#format 함수를 사용한 포매팅
# print("I eat {0} apples" .format(3))
##### 문자열 {0}에 숫자 3을 대입

#문자열 바로 대입하기
# print("I eat {0} apples".format("five"))
##### 문자열 {0}에 문자five를 대입

#숫자 값을 가진 변수로 대입하기
# number = 3
#print("I eat {0} apples.".format(number))
##### number라는 변수를 만들어 {0}에 numberfmf 대입

#2개 이상의 값 넣기
# number = 10
# day = "three"
# print("I ate {0} apples. so I was sick for {1} days".format(number, day))

#이름으로 넣기
#print("I ate {number} apples. so I was sick for {day} days" .format(number=10, day="three"))


#인덱스와 이름을 혼용해서 널기
#왼쪽 정렬 "{0:<10}".format("hi")
#오른쪽 정렬 "{0:>10}".format("hi")
#가운데 정렬 "{0:^10}".format("hi")
#공백 채우기 "{0:=^10}".format("hi")
#소수점 표현하기 y = 3.123456789      "{0:^10.4f}".format(y)
##################################################################################################

#f 문자열 포매팅
#name = "김효민"
#age = 23
#print(f"나의 이름은 {name} 입니다. 나이는 {age} 입니다.")

#문자열 관련 합수
#문자 개수 세기(count)
# a = "hobby"
# a.count("b")
### 문자열 중 문자 b의 개수를 리턴한다

#위치 알려주기1(find)
#a = "Python is the best choice"
#a.find("b")=14
#a.find("k")=-1
###문자나 문자열이 존재하지 않는다면 -1을 반환한다

#위치 알려주기2(index)
#index라는 함수는 문자열 중 찾는 문자가 맨 처름으로 나온 위치를 반환한다
#a = "Life is too short"
#a.index("t")=8
#a.index("k")=Error
###find 함수랑 다르게 찾는 문자가 없으면 오류가 발생한다

#문자열 삽입(join)
#넣고싶은 기호나 문자를 ,로 지정했을때
#print("넣고싶은 기호나 문자".join('abcd))=a,b,c,d

#소문자를 대문자로 바꾸기(upper)
#a = "hi"
#a.upper()=HI
###upper라는 함수는 소문자를 대문자로 바꿔준다 만약 이미 대문자면 아무런 변화도 일어나지 않는다

#대문자를 소문자로 바꾸기(lower)
#a = "HI"
#a.lower()=hi

#왼쪽 공백 지우기(lstrip)
#a = "hi"
#a.lstrip()='hi '
###문자열 중 가장 왼쪽에있는 공백들을 모두 지운다
###lstrip에서 l은 left를 의미한다

#오른쪽 공백 지우기(rstrip)
#a = "hi"
#a.rstrip()=' hi'
###문자열 중 오른쪽에 있는 공백을 모두 지운다
###rstrip 에서 r은 right를 의미한다

#양쪽 공백 지우기(strip)
#a = "hi"
#a.strip()='hi'
###문자열 양쪽에 있는 공백을 모두 지운다

#문자열 바꾸기(replace)
#a = "Life is too short"
#print(a.replace('Life', 'your leg'))
###replace(바뀌게 될 문자열, 바꿀 문자열)처럼 특정한 값을  다른 값으로 바꿔준다

#문자열 나누기(split)
#a = "Life is too short"
#a.split()=Life, is, too, short
###split함수는 a.split처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백을 기준으로 나눈다
#b = "a:b:c:d"
#b.split(':')=a,b,c,d
###b.split처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분하여 문자열을 나눈다