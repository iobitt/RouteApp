from django import forms


class RouteForm(forms.Form):
    """ Форма создания поездки """

    # Название поездки
    name = forms.CharField(label='Название', max_length=60)
    # Дата и время начала поездки
    start_date = forms.DateTimeField(label='Дата и время начала')
    # Дата и время окончания поездки
    end_date = forms.DateTimeField(label='Дата и время окончания')
    # Описание
    description = forms.CharField(label='Описание', required=False)


class WaypointForm(forms.Form):
    """ Форма добавления пункта маршрута """

    # Название поездки
    name = forms.CharField(label='Название', max_length=60)
    # Место добавления (до или после)
    place = forms.ChoiceField(label='Вставить', choices=((1, "до"), (2, "после")))
    # Соседнее значение
    neighbour = forms.ChoiceField(label='Пункт', required=False)

    def __init__(self, *args, **kwargs):
        self.neighbours = kwargs.pop('neighbours')
        super(WaypointForm, self).__init__(*args, **kwargs)
        self.fields['neighbour'].choices = self.neighbours + [("Выберите пункт маршрута", "0")]


class EventForm(forms.Form):
    """ Форма добавления мероприятия """

    # Название
    name = forms.CharField(label='Название', max_length=60, initial="")
    # Соседнее значение
    waypoint = forms.ChoiceField(label='Пункт маршрута')
    # Дата и время начала
    start_date = forms.DateTimeField(label='Дата и время начала')
    # Дата и время окончания
    end_date = forms.DateTimeField(label='Дата и время окончания')
    # Описание
    description = forms.CharField(label='Описание', initial="", required=False)

    def __init__(self, *args, **kwargs):
        self.waypoints = kwargs.pop('waypoints')
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['waypoint'].choices = self.waypoints


class MemberForm(forms.Form):
    """ Форма добавления участников в поездку """

    # Логин пользователя
    login = forms.CharField(label='Логин', max_length=60, initial="")
