from random import *

print('''
Password Maker
나만의 비밀번호를 만들어보세요.

원하는 문자를 입력해주세요. (10자리 이상)
''')

doorja = input()
slicemoonja = str(len(doorja)) + doorja.upper()
random = randrange(1, 1356)

print('생성된 비밀번호는 ' + doorja[1:5] + slicemoonja[5:9] + str(random) + ' 입니다.')