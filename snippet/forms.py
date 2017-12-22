from django import forms

class SnippetForm(forms.Form):
    error_css_class = 'error'
    # required_css_class = 'required'

    title = forms.CharField(label='Title', max_length=100)
    language = forms.CharField(label='Language', max_length=100)
    code_snippet = forms.CharField(label='Snippet', widget=forms.Textarea)
    description = forms.CharField(label='Description', widget=forms.Textarea)
