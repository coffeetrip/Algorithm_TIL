# django-form

앱 안에 forms.py 파일을 만든다.



forms.py

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):   # 폼 이름(폼은 ModelForm)

    class Meta:    # 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 알려주기
        model = Post
        fields = ('title', 'text',)  # 보여주고 싶은 폼
```

forms model을 import

model import



- [required](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#required): `True` 로 설정되면, 필드를 빈칸으로 두거나 `None` 값을 줄 수 없게된다. 보통필드는 required는 True로 기본 설정되므로, 폼에서 빈 칸을 허용하기 위해서는`required=False` 로 설정해야 한다. 
- [label](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#label): HTML에서 필드를 렌더링할때 사용하는 레이블이다. [label](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#label) 이 지정되지 않으면,  Django는 필드 이름에서 첫번째 문자를 대문자로, 밑줄을 공백으로 변형한 레이블을 새로 생성할 것이다. (예를 들면, renewal_date  --> *Renewal date*).
- [label_suffix](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#label-suffix): 기본적으로, 콜론(:)이 레이블 다음에 표시된다. (예를 들면, Renewal date**:**). 이 인자는 다른 문자(들)를 포함한 접미사를 지정할 수 있도록 해준다.
- [initial](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#initial): 폼이 나타날 때 해당 필드의 초기 값.
- [widget](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#widget): 사용할 디스플레이 위젯.
- [help_text](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#help-text) (위의 예에서 봤듯이): 필드 사용법을 보여주는 추가적인 문구.
- [error_messages](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#error-messages): 해당 필드의 에러 메시지 목록. 필요하면 문구를 수정할 수 있다.
- [validators](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#validators): 해당 필드가 유효한 값을 가질 때 호출되는 함수의 목록.
- [localize](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#localize): 폼 데이타 입력의 현지화(localisation)를 허용함 (자세한 정보는 해당 링크 참조).
- [disabled](https://docs.djangoproject.com/en/2.0/ref/forms/fields/#disabled): 이 옵션이 `True` 일때 해당 필드를 볼 수는 있지만 편집이 안됨. 기본 값은 `False`.