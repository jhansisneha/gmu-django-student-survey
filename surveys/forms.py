from django import forms
from .models import StudentSurvey

class StudentSurveyForm(forms.ModelForm):
    LIKED_CHOICES = [
        ('Students', 'Students'),
        ('Location', 'Location'),
        ('Campus', 'Campus'),
        ('Atmosphere', 'Atmosphere'),
        ('Dorm Rooms', 'Dorm Rooms'),
        ('Sports', 'Sports'),
    ]

    liked_most = forms.MultipleChoiceField(
        choices=LIKED_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = StudentSurvey
        fields = '__all__'
