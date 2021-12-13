from django.shortcuts import render
from .models import Alumni
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        branch = request.POST['branch']
        l = request.POST['l']
        n = Alumni(username=username, password=password, email=email, branch=branch, l=l)
        n.save()
        return render(request, 'register.html')
    return render(request, 'register.html')

def about(request):
    al = Alumni.objects.all()
    all = []
    if request.method == 'POST':
        interest = request.POST['name']
        branch = request.POST['branch']
        print(branch)
        for a in al:
            print(str(a.branch))
            if(str(a.branch) == str(branch)):
                all.append(a)
        print(all)
        return render(request, 'about.html', {'all': all})
    return render(request, 'about.html')

def index(request):
    return render(request, 'iindex.html')