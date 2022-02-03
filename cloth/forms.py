from django import forms
from . import models

class StatusOrderForm(forms.ModelForm):
    class Meta:
        model = models.StatusOrderCL
        fields = "__all__"