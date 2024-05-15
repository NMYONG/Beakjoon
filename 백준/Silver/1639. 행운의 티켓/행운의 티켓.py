# 리스트의 좌우 합이 같은지 확인
def isSame(lst):
    mid = len(lst) // 2
    left = sum(lst[:mid])
    right = sum(lst[mid:])

    return True if left == right else False

def solution(lst):
    if len(lst) % 2 == 0: # 짝수이면
        length = len(lst)
    else:
        length = len(lst) - 1

    while length > 0:
        i = 0
        ans = 0
        while i + length <= len(lst):
            if isSame(lst[i:i+length]):
                ans = length
                return ans
            i += 1
        length -= 2
    return 0


S = list(map(int, list(input())))
print(solution(S))
