def solution(x, n):
    answer = []
    for i in range(x, x*(n+1), x):
        answer.append(i)
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))