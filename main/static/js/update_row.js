//document.addEventListener('click', function(event) {
//    var dollar_mode = $('#dollar_mode').prop('checked')
//    if (!dollar_mode){
//    alert("בדיקה לגבי קליק יחיד!");  
//    event.preventDefault();  
//    event.stopPropagation();
//  }   
//  },  true //capturing phase!!
//
//);

$(document).on("dblclick", "#mainlist tbody tr td", function(e) {
    e.preventDefault();
    $('#clone_input').empty();
    $('#update_button').show();
    $('#update_values').hide();
    $('#new_date').hide();
    $('#new_date_time').hide();
    $('#flight_shcedule_update').hide();
    var id = $(this).closest('tr').find('.id').text();
    var td_id = $(this).attr('class');
    td_id = td_id.split(' ')[0];
    console.log('class:' + td_id);
    $('#row_id').val(id);
    $('#cell_id').val(td_id);

    if (td_id.includes('time')){
        $('#new_date_time').show();
    }else if(td_id.includes('Date')){
        $('#new_date').show();
    }else if(td_id == 'Flight_shcedule'){
        $('#flight_shcedule_update').show();
    }else{
        var clo = $('#id_'+td_id).clone();
        //Set the ID and Name
        clo.attr("id", "clo_"+td_id);
        clo.attr("name", "clo");
        $('#clone_input').append(clo)
        $('#clone_input').css({"border-style": "inset", cursor:"default"});
//        $('#update_values').show();
    }

});


//$(window).scroll(function(){
//    $('#clone_input').css({
//        'left': $(this).scrollLeft() + 15 //Why this 15, because in the CSS, we have set left 15, so as we scroll, we would want this to remain at 15px left
//    });
//});

// clone the select according to id
//http://www.jqueryfaqs.com/Articles/Clone-Copy-Dropdown-List-with-Selected-Value-using-jQuery.aspx
function update_row(){
    var id = $('#row_id').val();
    var td_id = $('#cell_id').val();
    td_id = td_id.split(' ')[0]; // get rid of highlight word in td id
    if (td_id.includes('time')){
        var new_value = $('#id_new_date_time').val()
    }else if(td_id.includes('Date')){
        var new_value = $('#id_new_date').val()
    }else if(td_id == 'Flight_shcedule'){
        var new_value = $('#id_flight_shcedule_update').val()
    }else{
        if ($("#clo_"+td_id).is('select')){
//            alert('Select');
            var new_value = $("#clo_"+td_id+" option:selected").text()
        }else{
//            alert('input');
            var new_value = $("#clo_"+td_id).val()
        }

    }
    console.log('new_value: ' + new_value);
    $.ajax({
        url: '/ajax/update_cell/',
        data: {
          'id': id,
          'new_value': new_value,
          'td_id': td_id,
        },
        dataType: 'json',
        success: function(response){alert('row was updated');},
        error:function(){alert('row was not updated!');}
        });
    if (td_id.includes('highlight')){
        var class_atr = td_id.split(' ')[0];

        $('#mainlist tbody tr td.'+class_atr+'.highlight').each(function() {
//        console.log($(this).text());
            if($(this).closest('tr').find('.id').text()==id){
                console.log('changing: '+$(this).text());
                $(this).text(new_value);
            }
        });
    }else{
        var class_atr = td_id.split(' ')[0];
        $('#mainlist tbody tr td.'+class_atr).each(function() {
//        console.log($(this).text())
            if($(this).closest('tr').find('.id').text()==id){
                console.log('changing: '+$(this).text());
                $(this).text(new_value);
            }
        });
    }
    if (td_id=='KM'){
        $('#mainlist tbody tr td.KM').each( function(){
            var km = parseInt($(this).text());
            console.log('km == '+Number.isInteger(km))
            var km_min_20  = km - 200;
            if(km > 200){
                var km_min_str = km_min_20.toString();
                console.log('km_min == '+km_min_str)
                $(this).closest('tr').find('.Extra_KM_client').text(km_min_str);
                $(this).closest('tr').find('.Extra_KM_provider').text(km_min_str);
                $.ajax({
                    url: '/ajax/update_cell/',
                    data: {
                      'id': id,
                      'new_value': km_min_str,
                      'td_id': 'Extra_KM_client',
                    },
                    dataType: 'json',
//                    success: function(response){alert('row was updated');},
//                    error:function(){alert('row was not updated!');}
                    });
                $.ajax({
                    url: '/ajax/update_cell/',
                    data: {
                      'id': id,
                      'new_value': km_min_str,
                      'td_id': 'Extra_KM_provider',
                    },
                    dataType: 'json',
//                    success: function(response){alert('row was updated');},
//                    error:function(){alert('row was not updated!');}
                    });

            }
        });
    }
    $('#new_value').val('');
    $("#clone_input").empty();
    $("#special_clone_input").children().hide();
    $('#update_button').hide();
    if (td_id=='Status'){
        on_cancle()
    };

    start_min_end_func();
    if (td_id=='Start_time' || td_id=='End_time' || td_id =='Based_on_client' || td_id =='Based_on_provider'){
        console.log('update_sum_table fired')
        update_sum_table()
    };
    sum_sum_list();
}