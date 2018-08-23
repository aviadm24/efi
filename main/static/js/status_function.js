$(document).ready(function() {
//     var status_val = $(".Status").val()
    $(".Provider").each(function(e){
    var status_val = $(this).html();
    if (status_val=='—'){
//        console.log('status_val: '+status_val)
        $(this).css('background-color', 'yellow');
    }
    });

    $('#mainlist').find('tbody tr td:nth-child(5),td:nth-child(6),td:nth-child(7),td:nth-child(8),td:nth-child(9),td:nth-child(10),td:nth-child(11),td:nth-child(12),td:nth-child(13), td:nth-child(14)').each(function () {
        var tag = $(this).html();
//        var tag = $('input', this).val();
//        console.log('tag '+ tag)
        if (tag == '—'){
//            console.log('tag passed: '+ tag)
            $(this).css('background-color', 'yellow');
        }
    });

//    console.log('status_val '+status_val)
});

//$(document).ready(function() {
//    $("#id_Status").on("change", function (e) {
//    var status = $('#id_Status option:selected').text();
//    // https://stackoverflow.com/questions/10613873/get-the-jquery-index-of-td-element
//    console.log('id_Status:' + status)
//    //console.log('FT DEP VIP'==transfer)
//
//    switch(status) {
//        case "Missing Detils":
////            $('#input_table').find('th:nth-child(4),th:nth-child(5),th:nth-child(6),th:nth-child(7),th:nth-child(8),th:nth-child(9),th:nth-child(10),th:nth-child(11),th:nth-child(12),th:nth-child(13)').css('background-color', 'yellow');
//
//            $('#input_table').find('tbody tr td:nth-child(4),td:nth-child(5),td:nth-child(6),td:nth-child(7),td:nth-child(8),td:nth-child(9),td:nth-child(10),td:nth-child(11),td:nth-child(12),td:nth-child(13)').each(function () {
////                var tag = $(this).val();
//                var tag = $('input', this).val();
//                console.log('tag '+ tag)
//                if (tag == '' || tag == '---------' || tag == undefined){
//                    console.log('tag passed: '+ tag)
//                    $(this).css('background-color', 'yellow');
//                }
//            });
//
//            break;
//        case "Missing provider":
//            $('#input_table').find('th:nth-child(14)').css('background-color', 'yellow');
//            break;
//            }
//    });
//});


$("#id_KM").on("change", function (e) {
    var km = $('#id_KM').val();
    var km200 = km -200;
    if (km200 < 0){
        km200 = 0;
    }
    $("#id_Extra_KM_client").val(km200);
    $("#id_Extra_KM_provider").val(km200);
});