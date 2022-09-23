from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.


class Index(View):
    def get(self, request):
        featured_projects = Project.objects.all()
        recent_projects = Project.objects.all()[:2]
        blogs = Blog.objects.all()
        return render(request, "core/index.html", {
            "featured_projects": featured_projects,
            "recent_projects": recent_projects,
        })
