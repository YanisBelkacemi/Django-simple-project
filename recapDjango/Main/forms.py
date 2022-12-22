from django import forms

class CreatNewlist(forms.Form):
	name = forms.CharField(label="name")
	check = forms.BooleanField(required = False)
class Delete(forms.Form):
	name = forms.CharField(label="List name")
	