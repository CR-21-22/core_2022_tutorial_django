from django.forms import ModelForm
from .models import Amigo

class AmigoForm(ModelForm):
    class Meta:
        model = Amigo

        fields = '__all__'

