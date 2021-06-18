// Инициализация карты
function init()
{
    let wayPoints = [];
    // Добавляем пункты маршрута в массив
    $(".way-point").each(function( index ) {
        wayPoints.push($( this ).text());
    });

    let multiRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: wayPoints
    }, {
        // Тип промежуточных точек, которые могут быть добавлены при редактировании.
        editorMidPointsType: "via",
        // В режиме добавления новых путевых точек запрещаем ставить точки поверх объектов карты.
        editorDrawOver: false
    });

    // Прослушивание события обновления мультимаршрута
    // Один раз, когда маршрут загрузился
    multiRoute.events.once('update', function () {
        let multiRoutePaths = multiRoute.getActiveRoute().getPaths().toArray();
        let tbody = $('#timing-tbody');
        for (let i = 0; i < multiRoutePaths.length; i++)
        {
            // Получаем расстояние и время на каждом участке маршрута
            let distance = multiRoutePaths[i].properties.get("distance");
            let duration = multiRoutePaths[i].properties.get("duration");

            // Добавляем запись в секцию "Расчёт времени"
            tbody.append('<tr><td>' + wayPoints[i] + '-' + wayPoints[i + 1] + '</td><td>Поездка</td><td>' + duration.text + '</td><td>' + distance.text + '</td></tr>')
        }

        // Добавляем в таблицу информацию о суммарном времени и расстоянии
        tbody.append(`<tr>
            <td colspan="2">Общее время и расстояние в пути</td>
            <td>${multiRoute.getActiveRoute().properties.get("duration").text}</td>
            <td>${multiRoute.getActiveRoute().properties.get("distance").text}</td>
           </tr>
        `)
    });

    myMap = new ymaps.Map('map', {
        center: [56.139791, 47.248733],
        zoom: 11,
        controls: []
    }, {
        buttonMaxWidth: 300
    });

    // Добавляем мультимаршрут на карту
    myMap.geoObjects.add(multiRoute);
}

ymaps.ready(init);
