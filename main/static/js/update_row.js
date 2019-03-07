$(document).on("dblclick", "#mainlist tbody tr td", function(e) {
    var id = $(this).closest('tr').find('.id').text();
    var td_id = $(this).attr('class');
    console.log('id'+ id)
    $('#row_id').val(id)
    $('#cell_id').val(td_id)
});

function update_row(){
    var id = $('#row_id').val();
    var td_id = $('#cell_id').val();
    var new_value = $('#new_value').val()
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
        console.log('class_atr' + class_atr);
        $('#mainlist tbody tr td.'+class_atr+'.highlight').each(function() {
        console.log($(this).text());
            if($(this).closest('tr').find('.id').text()==id){
                console.log('chnaging: '+$(this).text());
                $(this).text(new_value);
            }
        });
    }else{
        $('#mainlist tbody tr td.'+td_id).each(function() {
        console.log($(this).text())
            if($(this).closest('tr').find('.id').text()==id){
                console.log('chnaging: '+$(this).text());
                $(this).text(new_value);
            }
        });
    }
    $('#new_value').val('');

}