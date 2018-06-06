$(document).ready(function() {
    $('.Color').hide();
    $('table tr').each(function () {
        var color_string = $(this).find(".Color").text();
        var color_list = color_string.split("^");
        //console.log('color_list: '+color_list)
        for(var i = 0; i < color_list.length-1; i++){
           var color_list_split =  color_list[i].split("-")
           //console.log('color_list_split length: '+color_list_split.length)
           if (color_list_split.length > 2){
               var td_class = color_list_split[0];
               var color = color_list_split[1];
               //console.log('td_class: '+td_class)
               var td = $(this).find("."+td_class);
               //console.log('td: '+td)
               td.css('color', color);
           }else{
               var td_class = color_list_split[0];
               var color = color_list_split[1];
               //console.log('td_class: '+td_class)
               var td = $(this).find("."+td_class);
               //console.log('td: '+td)
               td.css('background', color);
           }

           };
    });
});
function light_for_transfer() {
    var transfer = $('#id_Type_of_service option:selected').text();
    // https://stackoverflow.com/questions/10613873/get-the-jquery-index-of-td-element
    console.log('Type_of_service:' + transfer)
    if(transfer == "TRN") {
        $('th').css('color', 'rgb(0,0,0)');
        $('th:nth-child(4),th:nth-child(5),th:nth-child(6),th:nth-child(7),th:nth-child(8),th:nth-child(10),th:nth-child(12),th:nth-child(13),th:nth-child(22),th:nth-child(23),th:nth-child(24),th:nth-child(31),th:nth-child(32)').css('color', 'rgb(34,200,200)');
    }
    if(transfer == "ARR" || transfer == "DEP") {
        $('th:nth-child(2),th:nth-child(3),th:nth-child(4),th:nth-child(5),th:nth-child(6),th:nth-child(7),th:nth-child(8),th:nth-child(9),th:nth-child(10),th:nth-child(12),th:nth-child(13),th:nth-child(22),th:nth-child(23),th:nth-child(24),th:nth-child(31),th:nth-child(32)').css('color', 'rgb(34,200,200)');
    }
    if(transfer == "FT ARR" || transfer == "FT DEP") {
        $('th').css('color', 'rgb(0,0,0)');
        $('th:nth-child(2),th:nth-child(3),th:nth-child(4),th:nth-child(8),th:nth-child(9),th:nth-child(10),th:nth-child(21),th:nth-child(23),th:nth-child(24),th:nth-child(31)').css('color', 'rgb(34,200,200)');
    }

}

$('#id_Type_of_service').on("change", function (e) {
    console.log('id_Type_of_service change')
    light_for_transfer();
});


$(document).ready(function () {

    $('td').click(function () {
        var color = $('#custom').val();
        var color_method = $('#color_method').prop('checked')
        console.log('color_method: '+color_method)
        var id = $(this).closest('tr').find('.id').text();
        var td_id = $(this).attr('class');
        //$('#id_Color').val(color);
        if (color_method == false){
                console.log('color_method false')
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
                if(this.style.background == "" || this.style.background =="white") {
                    console.log('color: '+color)
                    $(this).css('background', color);
                }
            }else{
                console.log('color_method true')
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
                if(this.style.color == "" || this.style.color =="white") {
                    $(this).css('color', color);
                }
            }



        //var row_id = $('row.id').val();
        //console.log('row id: '+row_id)

//        else {
//            $(this).css('background', 'white');
//        }
    });


//    $('table tr').each(function () {
//        var color_id = $(this).find(".color_id").html();
//        var color_id = $('td.color_id').text();
//        console.log('color id:' + color_id)
//        $(this).css('background', color_id);
//    });


    });