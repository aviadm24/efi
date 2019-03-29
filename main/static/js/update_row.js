$(document).on("dblclick", "#mainlist tbody tr td", function(e) {
    var id = $(this).closest('tr').find('.id').text();
    var td_id = $(this).attr('class');
    console.log('id'+ td_id);
    $('#row_id').val(id);
    $('#cell_id').val(td_id);
    if (td_id.includes('time')){
        console.log('date and time update')
        $('#new_date_time').show();
    }else if(td_id.includes('Date')){
        console.log('only date update')
        $('#new_date').show();
    }
});

function update_row(){
    var id = $('#row_id').val();
    var td_id = $('#cell_id').val();
    if (td_id.includes('time')){
        var new_value = $('#id_new_date_time').val()
        console.log('input new date:' + new_value)
    }else if(td_id.includes('Date')){
        var new_value = $('#id_new_date').val()
    }else{
        var new_value = $('#new_value').val()
    }

    $.ajax({
        url: '/ajax/update_cell/',
        data: {
          'id': id,
          'new_value': new_value,
          'td_id': td_id,
        },
        dataType: 'json',
        success: function(response){
                    alert('row was updated');
                    },
        error:function(){alert('row was not updated!');}
        });
    if (td_id.includes('highlight')){
        var class_atr = td_id.split(' ')[0];
        //console.log('class_atr' + class_atr);
        $('#mainlist tbody tr td.'+class_atr+'.highlight').each(function() {
        console.log($(this).text());
            if($(this).closest('tr').find('.id').text()==id){
                console.log('chnaging: '+$(this).text());
                $(this).text(new_value);
            }
        });
    }else{
        var class_atr = td_id.split(' ')[0];
        $('#mainlist tbody tr td.'+class_atr).each(function() {
        //console.log($(this).text())
            if($(this).closest('tr').find('.id').text()==id){
                console.log('chnaging: '+$(this).text());
                $(this).text(new_value);
            }
        });
    }
    $('#new_value').val('');
    start_min_end_func()
}