from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'login.html', context=None)

class inputUsername(TemplateView):

    def post(self, request, **kwargs):
        pass ## needs to post a new record to SQL database

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


    