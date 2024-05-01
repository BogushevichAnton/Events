from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from .models import *

class AddEventsForm(forms.ModelForm):
    date_start = forms.SplitDateTimeField(error_messages={'required': "Обязательные поля дата и время начала спортивного мероприятия"}, label="Дата и время проведения спортивного мероприятия", widget=AdminSplitDateTime())
    date_end = forms.SplitDateTimeField(error_messages={'required': "Обязательные поля дата и время окончания спортивного мероприятия"},label="Дата и время окончания спортивного мероприятия", widget=AdminSplitDateTime())

    class Meta:
        model = Events
        fields = ('city', 'address', 'description', 'date_start', 'date_end', 'type', 'budget')

        error_messages = {
            'address': {
                'max_length': "Максимальное количество символов - 255.",
                'required': "Обязательное поле адрес"
            },
        }




