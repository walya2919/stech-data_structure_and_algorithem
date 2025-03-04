class InputError(Exception):
    def __str__(self):
        return '입력값이 정수가 아닙니다.'

def factorial(n:int) -> int:
    if n==1:
        return 1
    
    return factorial(n-1) * n

user_input = input('숫자를 입력해 주세요: ')
if not user_input.isdigit():
    raise InputError

user_input = int(user_input)
res = factorial(user_input)

print('\n입력 값에 대한 계승값: {}'.format(str(res)))
