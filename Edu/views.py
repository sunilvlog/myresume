from django.shortcuts import render

# Create your views here.
def skill(request):
    context = {'skills': 'active'}
    return render(request, 'Edu/skill.html', context)