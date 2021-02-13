from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def project(request, project_id):
    proj = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/portfolio-details.html', {'proj': proj,})