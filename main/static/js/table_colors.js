
$(document).ready(function() {
    $('#mainlist tbody tr td').each(function(e){
        var tag = $(this).html();
        if (tag == '—'){
            $(this).css('background-color', 'rgb(255,255,50)');
        }
    });
});

$(document).ready(function() {
//    $('.Color').hide();
//    $('#id_Color').hide();
    $('table#mainlist tbody tr').each(function () {
        var color_string = $(this).find(".Color").text();
        //console.log('color_string: '+color_string)
        if (color_string != '—'){
            var obj = JSON.parse(color_string);
        }
        var row  = $(this);
        $.each(obj, function(key,val){
            console.log('key:  '+key)
           if (key.endsWith('_text')){
               console.log('ends with text! '+key)
               var new_key =  key.replace('_text','');
               console.log('new_key: '+new_key)
               var td = row.find("."+new_key);
               console.log('td: '+td)
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



