from django import forms
from django.forms import widgets
from .models import User

class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model =User 
        fields =['name', 'email', 'password','conformpassword']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}), 
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True,  attrs={'class':'form-control'}),
            'conformpassword':forms.PasswordInput(render_value=True,attrs={'class':'form-control'},)
        }
        def clean(self):
          cleaned_data=super().clean()
          valpwd=self.cleaned_data['password']
          valrpwd=self.cleaned_data['ConfirmPassword']
          if valpwd!=valrpwd:
            raise forms.ValidationError('Password does not match')  