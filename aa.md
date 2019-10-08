```python
for tc in range(1, 1+1):
    N = int(input())
    code = list(map(int, input().split()))
    m = int(input())
    m_code = list(input().split())

    new = []
    idx = 0
    while len(m_code) > idx:
        if m_code[idx] == 'I':
            idx += 1
            x = m_code[idx]
            idx += 1
            y = m_code[idx]
            print(x, y)
            for yy in range(int(y)):
                code.insert(int(x)+yy, m_code[idx+yy])
        idx += int(y) + 1
        print(code)
```

