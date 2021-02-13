from django.shortcuts import render
from .models import Certificate, Detail, Contact
from blog.models import BlogPage
from .forms import ContactForm
from projects.models import Project


# Create your views here.
def index(request):
    infor = Detail.objects.first()
    blogp = BlogPage.objects.order_by('-pub_date')[:6]
    context = {}
    try:
        skills = infor.skill.split(",")
        services = [i.split(":") for i in infor.services.split("|")]
        # Projects Section

        proj = Project.objects.order_by('-project_date')
        
        # contactSection

        new_message = None
        if request.method == 'POST':
            contact_form = ContactForm(data=request.POST)
            if contact_form.is_valid():
                new_message = contact_form.save(commit=False)
                new_message.save()
        else:
            contact_form = ContactForm()
                

        # contactEnd
        context = {
            'infor': infor,
            'skills': skills,
            'services': services,
            'blog': blogp,
            'new_message': new_message,
            'contact_form': contact_form,
            'proj': proj,
        }
    except AttributeError:
        pass
    return render(request, 'mainpage/index.html', context)

def certificates(request):
    certi = Certificate.objects.all()
    return render(request, 'mainpage/certificates.html', {'certificate': certi,})
    