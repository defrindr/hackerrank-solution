def solve(s):
    temp = []
    temp+=(_.capitalize() for _ in s.split(" "))
    print(" ".join(_ for _ in temp))
solve("defri indra mahardika")