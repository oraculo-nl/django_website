from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member

# Create your views here.
def hello_view(request):
    mymembers = Member.objects.all().values()
    print(type(mymembers))
    template = loader.get_template('members/myfirst.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('members/details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))