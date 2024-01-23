from .models import Contact

def data(request):
    contact_info = Contact.objects.first()
    return locals()