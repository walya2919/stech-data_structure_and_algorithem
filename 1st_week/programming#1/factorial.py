import sys
import time
sys.setrecursionlimit(10002)

class InputValueError(Exception):
    def __str__(self):
        return '입력값이 정수가 아닙니다.'

def factorial(n:int) -> int:
    if n==1:
        return 1
    
    return factorial(n-1) * n

user_input = input('숫자를 입력해 주세요: ')
if not user_input.isdigit():
    raise InputValueError

user_input = int(user_input)
start = time.time()
res = factorial(user_input)
end = time.time()

try:
    print(f'\n입력 값에 대한 계승값: {res}')
except:
    print('출력값 과다로 출력이 제한되었습니다.')
print(f'걸린 시간: {end-start:.5f}초')
