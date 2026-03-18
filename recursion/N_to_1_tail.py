# print N -> 1 - Tail - Backtracking

def func(i, N):
    if i > N:
        return
    func(i, N + 1)
    print(i)

func(1, 4)