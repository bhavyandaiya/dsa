# print from 1 -> N using Tail - Backtracking

def func(N):
    if N == 0:
        return
    func(N-1)
    print(N)

func(4)