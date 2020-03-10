from django import forms


class ExportImagierForm(forms.Form):
	required_css_class = 'img-form-list-row'
	imagier_title = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Titre de l\'imagier', 'class': 'form-font'}))
	file_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nom du PDF', 'class': 'form-font'}))