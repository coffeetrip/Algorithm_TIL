# 입력 값을 변수 두 개에 저장하기(input, map)

- **변수1, 변수2 = input().split()**
- **변수1, 변수2 = input().split('기준문자열')**
- **변수1, 변수2 = input('문자열').split()**
- **변수1, 변수2 = input('문자열').split('기준문자열')**

```python
a , b  = input('문자열 두 개를 입력하세요: ').split()
```

```python
a, b = input('문자열 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
 
print(a)
print(b)
```

```
문자열 두 개를 입력하세요: Hello Python (입력)
Hello
Python
```

input에 `split`을 사용하면 `입력받은 값을 공백을 기준으로 분리`하여 변수에 차례대로 저장합니다.

(split은 분리하다, 나누다라는 뜻)

<br>



```python
a , b  = input('숫자 두 개를 입력하세요: ').split()
```

```python
a, b = input('숫자 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
 
print(a + b)
```

```
숫자 두 개를 입력하세요: 10 20 (입력)
1020
```

`input에서 입력받은 값은 문자열`이고, 이 문자열은 split으로 분리해도 문자열이기 때문

<br>





```python
a, b = input('숫자 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
a = int(a)    # 변수를 정수로 변환한 뒤 다시 저장
b = int(b)    # 변수를 정수로 변환한 뒤 다시 저장
 
print(a + b)
```

```
숫자 두 개를 입력하세요: 10 20 (입력)
30
```

a = int(a)와 같이 int에 변수를 넣은 뒤 다시 변수에 저장해주면 변수가 정수 자료형으로 변환됩니다. 이때 int(a)처럼 int만 사용하고 결과를 변수에 저장하지 않으면 정수로 변환되지 않습니다. 

<br>



split의 결과를 매번 int로 변환해주려니 귀찮습니다. 이때는 `map`을 함께 사용하면 됩니다. map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환해줍니다(실수로 변환할 때는 int 대신 float를 넣습니다.).

- **변수1, 변수2 = map(int, input().split())**
- **변수1, 변수2 = map(int, input().split('기준문자열'))**
- **변수1, 변수2 = map(int, input('문자열').split())**
- **변수1, 변수2 = map(int, input('문자열').split('기준문자열'))**

```python
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
 
print(a + b)
```

```
숫자 두 개를 입력하세요: 10 20 (입력)
30
```

<br>



```python
a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) # 입력받은 값을 콤마를 기준으로 분리
 
print(a + b)
```

```
숫자 두 개를 입력하세요: 10,20 (입력)
30
```

split(',')과 같이 분리할 기준 문자열을 콤마로 지정하였으므로 '10,20'에서 10은 a, 20은 b에 저장됩니다.





 input과 split의 결과가 문자열


