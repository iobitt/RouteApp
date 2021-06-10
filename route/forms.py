from django import forms


class RouteForm(forms.Form):
    """ Форма создания поездки """

    # Название поездки
    name = forms.CharField(label='Название', max_length=60)
    # Дата начала поездки
    start_date = forms.DateField(label='Дата начала')
    # Дата окончания поездки
    end_date = forms.DateField(label='Дата окончания')
