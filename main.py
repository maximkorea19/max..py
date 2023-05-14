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