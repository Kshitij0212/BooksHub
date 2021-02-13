from django.contrib.auth import get_user_model
from django.contrib.auth import forms
from .models import User

class UserCreateForm(forms.UserCreationForm):

    class Meta:
        fields = ('username','first_name','last_name','email','password1','password2')
        model = User

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
          #  self.fields['username'].widget.attrs.update({'class' : 'username'})
            self.fields['username'].widget.attrs['class'] = 'username'
            
