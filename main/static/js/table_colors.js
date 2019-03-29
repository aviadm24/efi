
$(document).ready(function() {
    $('.Color').hide();
    $('#id_Color').hide();
    $('table#mainlist tbody tr').each(function () {
        var color_string = $(this).find(".Color").text();
        //console.log('color_string: '+color_string)
        if (color_string != '—'){
            //console.log(color_string=='—')
            var obj = JSON.parse(color_string);
        }

        //var color_list = color_string.split("^");
        var row  = $(this);
        $.each(obj, function(key,val){
            //console.log("key : "+key+" ; value : "+val);
//            var color_list_split =  val.split("-")
//               if (color_list_split.length > 1){
               if (key.endsWith('_text')){
                   //console.log('ends with text! '+key)
                   var new_key =  key.split("_")[0]
                   //console.log('new_key: '+new_key)
                   var td = row.find("."+new_key);
                   //console.log('td: '+td)
                   td.css('color', val);
               }else{
//                   var td_class = key;
//                   var color = color_list_split[0];
//                   console.log('td_class: '+td_class)
                   var td = row.find("."+key);
                   //console.log('td: '+td.text())
                   td.css('background', val);
               }

        });
    });
});
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
//    if(transfer == "TRN") {
//        $('th').css('color', 'rgb(0,0,0)');
//        $('th:nth-child(4),th:nth-child(5),th:nth-child(6),th:nth-child(7),th:nth-child(8),th:nth-child(10),th:nth-child(12),th:nth-child(13),th:nth-child(22),th:nth-child(23),th:nth-child(24),th:nth-child(31),th:nth-child(32)').css('color', 'rgb(34,200,200)');
//    }
//    if(transfer == "ARR" || transfer == "DEP") {
//        $('th:nth-child(2),th:nth-child(3),th:nth-child(4),th:nth-child(5),th:nth-child(6),th:nth-child(7),th:nth-child(8),th:nth-child(9),th:nth-child(10),th:nth-child(12),th:nth-child(13),th:nth-child(22),th:nth-child(23),th:nth-child(24),th:nth-child(31),th:nth-child(32)').css('color', 'rgb(34,200,200)');
//    }
//    if(transfer == "FT ARR" || transfer == "FT DEP") {
//        $('th').css('color', 'rgb(0,0,0)');
//        $('th:nth-child(2),th:nth-child(3),th:nth-child(4),th:nth-child(8),th:nth-child(9),th:nth-child(10),th:nth-child(21),th:nth-child(23),th:nth-child(24),th:nth-child(31)').css('color', 'rgb(34,200,200)');
//    }
//
//    if(transfer == "---------") {
//        $('th').css('color', 'rgb(0,0,0)');
//    }
}

$('#id_Type_of_service').on("change", function (e) {
    //console.log('id_Type_of_service change')
    hide_for_transfer();
});


$(document).ready(function () {

    $('table#mainlist tbody tr td').click(function () {
        //console.log('main list tr')
        var color = $('#custom').val();
        var color_method = $('#color_method').prop('checked')
//        console.log('color_method: '+color_method)
        var id = $(this).closest('tr').find('.id').text();
        var td_id = $(this).attr('class');
        //$('#id_Color').val(color);
        if (color_method == false){
                //console.log('color_method false')
                $.ajax({
                url: '/ajax/add_color/',
                data: {
                  'id': id,
                  'color': color,
                  'td_id': td_id,
                  'text_color': color_method,
                },
                dataType: 'json',
//                success: function (data) {
//                  if (data) {
//                    alert("Success");
//                  }
//                }
                });
                $(this).css('background', color);

            }else{
                //console.log('color_method true')
                $.ajax({
                url: '/ajax/add_color/',
                data: {
                  'id': id,
                  'color': color,
                  'td_id': td_id,
                  'text_color': color_method,
                },
                dataType: 'json',
//                success: function (data) {
//                  if (data) {
//                    alert("Success");
//                  }
//                }
                });
//                if(this.style.color == "" || this.style.color =="white") {
//                    $(this).css('color', color);
//                }
                $(this).css('color', color);

            }



        //var row_id = $('row.id').val();
        //console.log('row id: '+row_id)

//        else {
//            $(this).css('background', 'white');
//        }
    });

    $('td').dblclick(function() {
        var color_method = $('#color_method').prop('checked')
        var id = $(this).closest('tr').find('.id').text();
        var td_id = $(this).attr('class');
        if (color_method == false){
                //console.log('color_method false')
                $.ajax({
                url: '/ajax/add_color/',
                data: {
                  'id': id,
                  'color': '',
                  'td_id': td_id,
                  'text_color': color_method,
                },
                dataType: 'json',
                });
                $(this).css('background', '');

            }else{
                console.log('color_method true')
                $.ajax({
                url: '/ajax/add_color/',
                data: {
                  'id': id,
                  'color': '',
                  'td_id': td_id,
                  'text_color': color_method,
                },
                dataType: 'json',
                });
                $(this).css('color', '');
            }
        });
});