### [S/W 문제해결 응용] 3일차 - 공통조상 

```python
(1) 자식을 인덱스로 부모 저장
(2) N1의 조상 i를 빈 배열 a에 표시 a[i] = 1
(3) N2의 조상 j를 배열 a에서 확인 a[j] == 1인 경우
(4) a[j] == 1인 최초의 경우가 N1, N2에서 가장 가까운 공통 조상


c = N1
while par[c]!=0:
    a[par[c]] = 1
    c = par[c]

c = N2
while a[c] == 0:
    c = par[c]
print(c)
```

