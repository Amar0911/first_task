from django import forms
from . models import Marvel

# class MarvelForm(forms.Form):
#     name = forms.CharField()
#     heroic_name = forms.CharField()

class MarvelForm(forms.ModelForm):
    # name = forms.CharField(max_length=30)
    
    
    
    class Meta:
        model = Marvel
        fields = ['name', 'heroic_name']
        labels = {'name':'Full Name'}
        error_messages = {
            'name':{'required': 'Write your full name as per your Adhaarcard'},
            'heroic_name':{'required': 'Write your heroic name'}
        }

        widgets = {
            # 'name': forms.PasswordInput(),
            'heroic_name': forms.TextInput(attrs={'class':'form-control'})
        }

