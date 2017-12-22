from django.shortcuts import render
from .forms import SnippetForm

data = []


def index(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            language = form.cleaned_data['language']
            code_snippet = form.cleaned_data['code_snippet']
            description = form.cleaned_data['description']
            data.append([title, language, code_snippet, description])

    form = SnippetForm()

    return render(request, 'snippet/index.html', {'form': form, 'data': data})
