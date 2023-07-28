from django import forms
from .models import Car


input_css_class = "form-control"

class CarForm(forms.ModelForm):
    class Meta:
        model = Car 
        fields = ['name', 'handle', 'price']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for fields in self.fields:
            self.fields[fields].widget.attrs['class'] = input_css_class