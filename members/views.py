from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member

# Create your views here.
@login_required
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

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def hello_form(request):
    message = None
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            message = f"Hallo, {name}!"
        else:
            message = "Vul een naam in."
    return render(request, "members/hello_form.html", {"message": message})