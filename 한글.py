# 입출력
def 입력():
    return input()

def 출력(값):
    print(값)

# 사칙연산
def 두수더하기(ㄱ, ㄴ):
    return ㄱ + ㄴ

def 두수빼기(ㄱ, ㄴ):
    return ㄱ - ㄴ

def 두수곱하기(ㄱ, ㄴ):
    return ㄱ * ㄴ

def 두수나누기(ㄱ, ㄴ):
    return ㄱ / ㄴ

# 참과 거짓
def 참():
    return True

def 거짓():
    return False

# 비교 연산자
def 같음(ㄱ, ㄴ):
    return ㄱ == ㄴ

def 다름(ㄱ, ㄴ):
    return ㄱ != ㄴ

def 그리고(ㄱ, ㄴ):
    return ㄱ and ㄴ

def 아니면(ㄱ, ㄴ):
    return ㄱ or ㄴ

def 반대(ㄱ):
    return not ㄱ

def 보다큰(ㄱ, ㄴ):
    return ㄱ < ㄴ

def 보다작은(ㄱ, ㄴ):
    return ㄱ > ㄴ

def 보다크거나같음(ㄱ, ㄴ):
    return ㄱ <= ㄴ

def 보다작거나같음(ㄱ, ㄴ):
    return ㄱ >= ㄴ

# 수학
def 절댓값(ㄱ):
    if (ㄱ > 0):
        return ㄱ
    return -ㄱ

def 큰값(ㄱ, ㄴ):
    if (ㄱ > ㄴ):
        return ㄱ
    return ㄴ

def 작은값(ㄱ, ㄴ):
    if (ㄱ < ㄴ):
        return ㄱ
    return ㄴ