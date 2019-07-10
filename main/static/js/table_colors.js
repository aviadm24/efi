
$(document).ready(function() {
//    $('.Color').hide();
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
               if (key.endsWith('_text')){
                   //console.log('ends with text! '+key)
                   var new_key =  key.split("_")[0]
                   //console.log('new_key: '+new_key)
                   var td = row.find("."+new_key);
                   //console.log('td: '+td)
                   td.css('color', val);
               }else{
                   var td = row.find("."+key);
                   //console.log('td: '+td.text())
                   td.css('background', val);
               }

        });
    });
});

$(document).ready(function () {

        $('table#mainlist tbody tr td').click(function () {
        console.log('checked: '+$('#color_on').prop('checked'))
        if ($('#color_on').prop('checked')==true){
            var color = $('#custom').val();
            var color_method = $('#color_method').prop('checked')
            console.log('color_method: '+color_method)
            var id = $(this).closest('tr').find('.id').text();
            var td_id = $(this).attr('class').split(' ')[0];
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
                    });
                    $(this).css('color', color);

                }
            }else{console.log('color off')}
        });

        $('td').dblclick(function() {
//        var color_method = $('#color_method').prop('checked')
            if ($('#color_on').prop('checked')==true){
                    var id = $(this).closest('tr').find('.id').text();
                    var td_id = $(this).attr('class').split(' ')[0];
                    $.ajax({
                            url: '/ajax/add_color/',
                            data: {
                              'id': id,
                              'color': '',
                              'td_id': td_id,
                              'text_color': false,
                            },
                            dataType: 'json',
                            });
                    $(this).css('background', '');
                    $.ajax({
                            url: '/ajax/add_color/',
                            data: {
                              'id': id,
                              'color': '',
                              'td_id': td_id,
                              'text_color': true,
                            },
                            dataType: 'json',
                            });
                    $(this).css('color', '');
            }
        });
});


$(document).ready(function() {
//    $(".Provider").each(function(e){
//    var status_val = $(this).html();
//    if (status_val=='—'){
//        $(this).css('background-color', 'yellow');
//    }
//    });
    $('#mainlist tbody tr td').each(function(e){
//    $('#mainlist').find('tbody tr td:nth-child(5),td:nth-child(6),td:nth-child(7),td:nth-child(8),td:nth-child(9),td:nth-child(10),td:nth-child(11),td:nth-child(12),td:nth-child(13), td:nth-child(14)').each(function () {
        var tag = $(this).html();
        if (tag == '—'){
            $(this).css('background-color', 'rgb(255,255,50)');
        }
    });
});
