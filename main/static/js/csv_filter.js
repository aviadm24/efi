function csv_filter(){
    var project_num = $('#p_num').val()
    var customer = $('#customer').val()
    var provider = $('#provider').val()
    var min  = $('#id_start').val();
    var max  = $('#id_end').val();
    var mail  = $('#mail_to_send').val();
//    console.log('mail'+ mail)
    $.ajax({
        url: '/ajax/export_filter/',
        data: {
          'project_num': project_num,
          'customer': customer,
          'provider':provider,
          'min': min,
          'max': max,
          'mail': mail
        },
        dataType: 'json',
        });
}