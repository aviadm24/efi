var fd_arr = ['To', 'Cost_transfer_client', 'Cost_transfer_provider', 'Cost_VIP_client', 'Cost_VIP_provider']
var trn_arr = ['End_time', 'Extra_hours_client', 'Based_on_client', 'Extra_hours_provider', 'Based_on_provider', 'KM', 'Extra_KM_client', 'Extra_KM_provider', 'Cost_per_client', 'Cost_per_provider', 'Cost_VIP_client', 'Cost_VIP_provider']
var ft_vip_arr = ['Type_of_car', 'From', 'To', 'End_time', 'Extra_hours_client', 'Based_on_client', 'Extra_hours_provider', 'Based_on_provider', 'KM', 'Extra_KM_client', 'Extra_KM_provider', 'Cost_per_client', 'Cost_per_provider', 'Cost_transfer_client', 'Cost_transfer_provider', 'Cost_extra_hour_client', 'Cost_extra_hour_provider']
var parking_arr = ['From', 'To', 'Luggage', 'Extra_hours_client', 'Based_on_client', 'Extra_hours_provider', 'Based_on_provider', 'KM', 'Extra_KM_client', 'Extra_KM_provider', 'Cost_per_client', 'Cost_per_provider', 'Cost_transfer_client', 'Cost_transfer_provider', 'Cost_extra_hour_client', 'Cost_extra_hour_provider', 'Cost_VIP_client', 'Cost_VIP_provider']

function hide_for_transfer() {
    var transfer = $('#id_Type_of_service option:selected').text();
    // https://stackoverflow.com/questions/10613873/get-the-jquery-index-of-td-element
    console.log('Type_of_service:' + transfer)
    //console.log('FT DEP VIP'==transfer)

    switch(transfer) {
        case "FD":
            $('#input_table').find('th, td').not('.Color').show();
            $.each(fd_arr, function (index, value) {
//                $('#input_table .'+value).val('');
                $('#input_table .'+value).hide();
            });
            break;
//            $('#input_table tr:nth-child(2)').find('th').css('color', 'rgb(0,0,0)');
//            $('#input_table tr:nth-child(2)').find('th:nth-child(1),th:nth-child(2),th:nth-child(3),th:nth-child(4),th:nth-child(6),th:nth-child(7),th:nth-child(8),th:nth-child(9),th:nth-child(10),th:nth-child(12),th:nth-child(13),th:nth-child(14),th:nth-child(15),th:nth-child(16),th:nth-child(18),th:nth-child(27),th:nth-child(28)').css('color', 'rgb(34,200,200)');
        case "TRN":
        case "TRN ARR":
        case "TRN DEP":
            $('#input_table').find('th, td').not('.Color').show();
            $.each(trn_arr, function (index, value) {
//                $('#input_table .'+value).val('');
                $('#input_table .'+value).hide();
            });
            break;
        case "FT ARR VIP":
        case "FT DEP VIP":
            $('#input_table').find('th, td').not('.Color').show();
            $.each(ft_vip_arr, function (index, value) {
                $('#input_table .'+value).hide();
            });
            break;
        case "Parking":
            $('#input_table').find('th, td').not('.Color').show();
            $.each(parking_arr, function (index, value) {
                $('#input_table .'+value).hide();
            });
            break;
        default:
            $('#input_table').find('th, td').not('.Color').show();
            break;
        }
}

$('#id_Type_of_service').on("change", function (e) {
    //console.log('id_Type_of_service change')
    hide_for_transfer();
});


//$("#mainlist td.KM").on("click", function () {
//    alert("The paragraph was clicked.");
//});


$("#id_KM").on("change", function (e) {
    console.log(this.name)
    var km = $('#id_KM').val();
    var km200 = km -200;
    if (km200 < 0){
        km200 = 0;
    }
    $("#id_Extra_KM_client").val(km200);
    $("#id_Extra_KM_provider").val(km200);
});