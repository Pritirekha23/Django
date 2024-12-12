from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RedgForm(UserCreationForm):
    class Meta:
        model=User
        # fields='__all__'
        fields=('username','password1','password2','email','first_name','last_name')
