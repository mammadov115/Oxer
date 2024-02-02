from .models import Contact, InfoSection

def data(request):
    contact_info = Contact.objects.first()
    info = InfoSection.objects.first()
    return locals()