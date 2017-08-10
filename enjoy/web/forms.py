from django import forms
from django.forms import ModelForm

from datetime import date

from .models import Plan

class PlanForm(ModelForm):
    date_start = forms.DateField(
    	label='start date', 
    	widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',),
    	initial=date.today
    	)
    date_end = forms.DateField(
    	label='end date', 
    	widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',),
    	initial=date.today
    	)
    class Meta:
        model = Plan
        fields = '__all__'