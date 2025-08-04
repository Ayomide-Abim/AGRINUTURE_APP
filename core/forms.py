from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'required': True})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'required': True})
    )
    phone = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Phone Number',
            'pattern': '[0-9]*',
            'inputmode': 'numeric',
            'required': True
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'required': True})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 6, 'required': True})
    )
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 11:
            raise forms.ValidationError("Phone number must be exactly 11 digits.")
        return phone