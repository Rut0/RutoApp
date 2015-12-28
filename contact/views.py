from contact.forms import ContactForm
from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        # A POST request: Handle Form Upload
        form = ContactForm(request.POST)  # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            name = form.cleaned_data['name']
            return render(request, 'contact/index.html', {
                'form': form,
                'data': name
            })

    return render(request, 'contact/index.html', {
        'form': form
    })
