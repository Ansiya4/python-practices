a = ['{', '[', '}','(','{',')','}',']']
d = {
    '(': ')',
    '{': '}',
    '[': ']',
}
s=[]
# print(d.values())
# print(d.keys())

for i in a:
    if i in d:
        s.append(i)
        # print(s)
    elif i in d.values():
        if not s:
            print("false")
            break
        else:
            top = s.pop()
            print(d[top])
            if d[top] != i:
                print("false")
                break
    else:
        print("false")
        break



