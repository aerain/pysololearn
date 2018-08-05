print(1 + 1)
print('Hello \nWorld!')

'''
동작안하니까 주석으로 사용가능?
'''

x = input("아무 키나 입력해 주세요 :")
print(x)

'concat'

print('하나아' + ', ' + '두울')

'''int와 str 결합은 불가능
예를 들면 1 + '2' + 3 + '4'
'''

'''
문자열의 곱은 가능
그러나 문자열에 문자열의 곱을 가한 것은 불가능
'''

print('baam' * 5)

conversion = int("2" + "3")
print(conversion)

floatinput = float(input('실수를 입력해주세요')) + float(input('다른 실수를 입력해주세요'))
print(floatinput)