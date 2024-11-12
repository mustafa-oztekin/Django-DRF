from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    slug = forms.SlugField()

class UploadFrom(forms.Form):
    image = forms.ImageField()