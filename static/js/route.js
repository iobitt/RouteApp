wayPoints = [];


// Сохранить пункты маршрута
$("#update-route-btn").click(function()
{
    wayPoints.length = 0;

    $(".way-point").each(function( index ) {
        wayPoints.push($( this ).val());
    });
    addMultiRoute();
});

function showAddNodeWindow()
{
    $('#exampleModal').modal('show');
}

$("#add-row-btn").click(function() {
    $("#add-row-btn-tr").before("<tr><td><input class='form-control way-point' type='text'></td>" +
        "<td>" +
        "<a href='#'><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"32\" height=\"32\" fill=\"currentColor\" class=\"bi bi-trash\" viewBox=\"0 0 16 16\">\n" +
        "  <path d=\"M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z\"/>\n" +
        "  <path fill-rule=\"evenodd\" d=\"M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z\"/>\n" +
        "</svg></a>" +
        "</td></tr>");
});

function addNode()
{
    name = $('#recipient-name').val();
    $('#recipient-name').val("");

    wayPoints.push(name);

    $(".nodes").append("<li style='list-style-type: none;'>" + name + "</li>");
    $('#exampleModal').modal('hide');

    addMultiRoute();
}

function init () {
    /**
     * Создание мультимаршрута.
     * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/multiRouter.MultiRoute.xml
     */
    multiRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: wayPoints
    }, {
        // Тип промежуточных точек, которые могут быть добавлены при редактировании.
        editorMidPointsType: "via",
        // В режиме добавления новых путевых точек запрещаем ставить точки поверх объектов карты.
        editorDrawOver: false
    });

    var buttonEditor = new ymaps.control.Button({
        data: { content: "Режим редактирования" }
    });

    buttonEditor.events.add("select", function () {
        /**
         * Включение режима редактирования.
         * В качестве опций может быть передан объект с полями:
         * addWayPoints - разрешает добавление новых путевых точек при клике на карту. Значение по умолчанию: false.
         * dragWayPoints - разрешает перетаскивание уже существующих путевых точек. Значение по умолчанию: true.
         * removeWayPoints - разрешает удаление путевых точек при двойном клике по ним. Значение по умолчанию: false.
         * dragViaPoints - разрешает перетаскивание уже существующих транзитных точек. Значение по умолчанию: true.
         * removeViaPoints - разрешает удаление транзитных точек при двойном клике по ним. Значение по умолчанию: true.
         * addMidPoints - разрешает добавление промежуточных транзитных или путевых точек посредством перетаскивания маркера, появляющегося при наведении курсора мыши на активный маршрут. Тип добавляемых точек задается опцией midPointsType. Значение по умолчанию: true
         * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/multiRouter.MultiRoute.xml#editor
         */
        multiRoute.editor.start({
            addWayPoints: true,
            removeWayPoints: true
        });
    });

    buttonEditor.events.add("deselect", function () {
        // Выключение режима редактирования.
        multiRoute.editor.stop();

        points = multiRoute.model.getAllPoints();
        console.log(points);

        points.forEach(function(item, i, arr)
        {
            addNode(item._referencePoint);
        });

        });

    // Создаем карту с добавленной на нее кнопкой.
    myMap = new ymaps.Map('map', {
        center: [56.399625, 36.71120],
        zoom: 7,
        controls: [buttonEditor]
    }, {
        buttonMaxWidth: 300
    });

    // Добавляем мультимаршрут на карту.
    myMap.geoObjects.add(multiRoute);

    $("#update-route-btn").click();
}

function addMultiRoute()
{
    myMap.geoObjects.remove(multiRoute);

    multiRoute = new ymaps.multiRouter.MultiRoute({
    referencePoints: wayPoints
    }, {
        // Тип промежуточных точек, которые могут быть добавлены при редактировании.
        editorMidPointsType: "via",
        // В режиме добавления новых путевых точек запрещаем ставить точки поверх объектов карты.
        editorDrawOver: false
    });

    // Добавляем мультимаршрут на карту.
    myMap.geoObjects.add(multiRoute);
}

ymaps.ready(init);