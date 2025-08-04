from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentSurvey
from .forms import StudentSurveyForm
#from .models import Survey

def home(request):
    return render(request, 'surveys/home.html')

def create_survey(request):
    if request.method == 'POST':
        form = StudentSurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.liked_most = request.POST.getlist('liked_most')
            survey.save()
            return redirect('list_surveys')
    else:
        form = StudentSurveyForm()
    return render(request, 'surveys/create_survey.html', {'form': form})

def list_surveys(request):
    surveys = StudentSurvey.objects.all()
    return render(request, 'surveys/list_surveys.html', {'surveys': surveys})

##def update_survey(request, id):
##    survey = get_object_or_404(StudentSurvey, id=id)
##    if request.method == 'POST':
##        form = StudentSurveyForm(request.POST, instance=survey)
##        if form.is_valid():
##            form.save()
##            return redirect('list_surveys')
##    else:
##        form = StudentSurveyForm(instance=survey)
##    return render(request, 'surveys/update_survey.html', {'form': form})
    
def update_survey(request, id):
    survey = get_object_or_404(StudentSurvey, id=id)

    context = {
        'survey': survey,
        'liked_options': ['Students', 'Location', 'Campus', 'Atmosphere', 'Dorm Rooms', 'Sports'],
        'source_options': ['Friends', 'Television', 'Internet', 'Other'],
        'likelihood_choices': ['Very Likely', 'Likely', 'Unlikely']
    }

    if request.method == 'POST':
        form = StudentSurveyForm(request.POST, instance=survey)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.liked_most = request.POST.getlist('liked_most')
            survey.save()
            #form.save()
            return redirect('list_surveys')
        else:
            form = StudentSurveyForm(instance=survey)
    return render(request, 'surveys/update_survey.html', context)


def delete_survey(request, id):
    survey = get_object_or_404(StudentSurvey, id=id)
    survey.delete()
    return redirect('list_surveys')
