$(document).ready(function() {
    $("#id_Status").on("change", function (e) {
    var status = $('#id_Status option:selected').text();
    // https://stackoverflow.com/questions/10613873/get-the-jquery-index-of-td-element
    console.log('id_Status:' + status)
    //console.log('FT DEP VIP'==transfer)

    switch(status) {
        case "Missing Detils":
//            $('th').css('color', 'rgb(0,0,0)');
            $('#input_table').find('th:nth-child(4),th:nth-child(5),th:nth-child(6),th:nth-child(7),th:nth-child(8),th:nth-child(9),th:nth-child(10),th:nth-child(11),th:nth-child(12),th:nth-child(13)').css('background-color', 'yellow');
            break;
        case "Missing provider":
//            $('th').css('color', 'rgb(0,0,0)');
            $('#input_table').find('th:nth-child(14)').css('background-color', 'yellow');
            break;
            }
    });
});


$("#id_KM").on("change", function (e) {
    var km = $('#id_KM').val();
    var km200 = km -200;
    if (km200 < 0){
        km200 = 0;
    }
    $("#id_Extra_KM_client").val(km200);
    $("#id_Extra_KM_provider").val(km200);
});