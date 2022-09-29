# CSCI 1100 Gateway to Computer Science
#
# Simple problems with lists.

# evens : int -> list int
def evens(n):
    answer = []
    i = 2
    while i <= n:
        answer.append(i)          # adds i to right end of answer
        i = i + 2
        print(answer)
    return answer

# evensComprehension : int -> list int
def evensComprehension(n):
    return [ i for i in range(2, n + 1) if i % 2 == 0 ]







