from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Please Enter your Name'}, label='Full Name')
    email = forms.EmailField(error_messages={'required':'Please Enter your Email'})


    # for single field
    # def clean_name(self):
    #     validate_name =self.cleaned_data['name']

    #     if len(validate_name)>5:
    #         raise forms.ValidationError('Enter the Name Less than 5 words')

    # for multiple field.

    def clean(self):
        cleaned_data = super().clean()

        validate_name =cleaned_data['name']

        validate_email =cleaned_data['email']

        if len(validate_name)<5:
            raise forms.ValidationError('Enter the greater than 5 word')
        
        if len(validate_email)<5:
            raise forms.ValidationError('Enter the mail')