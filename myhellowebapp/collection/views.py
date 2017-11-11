from django.shortcuts import render
from collection.models import Profile

def index(request):
    profiles = Profile.objects.all()
    return render(request, 'index.html', {
        'profiles': profiles,
})
