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
var td_added_list = []
$(document).on("dblclick", "#mainlist tbody tr td", function(e) {
    console.log('update function called')
    e.preventDefault();
    $('#clone_input').empty();
    $('#update_button').show();
    $('#update_values').hide();
    $('#new_date').hide();
    $('#new_date_time').hide();
    $('#flight_shcedule_update').hide();
    var id = $(this).closest('tr').find('.id').text();
    if ($(this).closest('tr').find('.Status').text() == 'Cancled'){
        alert('אין אפשרות לשנות בשורה זו')
    }else{

        var td_id = $(this).attr('class');
    td_id = td_id.split(' ')[0];
//    console.log('class:' + td_id);111
    $('#row_id').val(id);
    $('#cell_id').val(td_id);

    if (td_id.includes('time')){
        $('#updating_now').children().remove();
        $('#updating_now').removeAttr( "id" );

        var html =
        '<div class="input-group date" id="new_date_time" data-target-input="nearest" style="width:220px">'+
          '<input name="new_date_time" id="id_new_date_time" type="text" class="form-control datetimepicker-input" data-target="#new_date_time"/>'+
          '<div class="input-group-append" data-target="#new_date_time" data-toggle="datetimepicker">'+
              '<div class="input-group-text"><i class="fa fa-calendar"></i></div>'+
          '</div>'+
        '</div>'
        $('#new_date_time').datetimepicker('setDate', '04/30/2019');
//        var clo = $('#new_date_time').clone();
//        clo.attr("id", "clo_"+td_id);
        var clone_button = $('#update_button').clone();
        $(this).append(html)
        $(this).append(clone_button)
//        $('#new_date_time').show();
        $(function () {
            $('#new_date_time').datetimepicker({
              format: 'YYYY-MM-DD HH:mm',
              useCurrent: false
            });
        });
        $(this).attr("id", "updating_now");

    }else if(td_id.includes('Date')){
        $('#updating_now').children().remove();
        $('#updating_now').removeAttr( "id" );

        var html =
        '<div class="input-group date" id="new_date" data-target-input="nearest" style="width:220px">'+
          '<input name="new_date" id="id_new_date" type="text" class="form-control datetimepicker-input" data-target="#new_date"/>'+
          '<div class="input-group-append" data-target="#new_date" data-toggle="datetimepicker">'+
              '<div class="input-group-text"><i class="fa fa-calendar"></i></div>'+
          '</div>'+
        '</div>'
        var clone_button = $('#update_button').clone();
        $(this).append(html)
        $(this).append(clone_button)
        $(function () {
            $('#new_date').datetimepicker({
              format: "YYYY-MM-DD",
              useCurrent: false
            });
        });
        $(this).attr("id", "updating_now");

    }else if(td_id == 'Flight_shcedule'){
        $('#updating_now').children().remove();
        $('#updating_now').removeAttr( "id" );

        var html =
        '<div class="input-group date" id="flight_shcedule_update" data-target-input="nearest" style="width:120px">'+
          '<input name="flight_shcedule_update" id="id_flight_shcedule_update" type="text" class="form-control datetimepicker-input" data-target="#flight_shcedule_update"/>'+
          '<div class="input-group-append" data-target="#flight_shcedule_update" data-toggle="datetimepicker">'+
              '<div class="input-group-text"><i class="fa fa-calendar"></i></div>'+
          '</div>'+
        '</div>'
        var clone_button = $('#update_button').clone();
        $(this).append(html)
        $(this).append(clone_button)
        $(function () {
            $('#flight_shcedule_update').datetimepicker({
              format: 'YYYY-MM-DD HH:mm',
              useCurrent: false
            });
        });
        $(this).attr("id", "updating_now");

    }else if(td_id == 'Flight_num'||td_id == 'To'||td_id == 'From'|| td_id == 'Driver_name'|| td_id == 'Provider'){
        $('#updating_now').children().remove();
        $('#updating_now').removeAttr( "id" );
        var clo = $('#id_'+td_id).clone();
        //Set the ID and Name
        clo.attr("id", "clo_"+td_id);
        clo.attr("style", "width:120px;");

        var clone_button = $('#update_button').clone();
        $(this).append(clo);
        $('#clo_'+td_id).select2({
              tags: true
            });
        $(this).append(clone_button);
        $(this).attr("id", "updating_now");

    }else{
        $('#updating_now').children().remove();
        $('#updating_now').removeAttr( "id" );

        var clo = $('#id_'+td_id).clone();
        //Set the ID and Name
        clo.attr("id", "clo_"+td_id);
        clo.attr("name", "clo");
        var clone_button = $('#update_button').clone();
        $(this).append(clo)
        $(this).append(clone_button)
        $(this).attr("id", "updating_now");
//        $('#clone_input').append(clo)
//        $('#clone_input').css({"border-style": "inset", cursor:"default"});
    }

    }

});


// clone the select according to id
//http://www.jqueryfaqs.com/Articles/Clone-Copy-Dropdown-List-with-Selected-Value-using-jQuery.aspx

//$('#clo_status_cheshbonit_yeruka1').on("change", function () {
//https://stackoverflow.com/questions/18746381/dynamically-created-select-menu-on-change-not-working
$(document).on("change", '#clo_status_cheshbonit_yeruka1', function () {
    var new_value = $("#clo_status_cheshbonit_yeruka1 option:selected").text()
    if (new_value == 'נשלחה הזמנת רכש'){
        alert('צריך לקלוט מספר הזמנת רכש')
        var html = '<input id="id_hazmanat_rechesh" type="text" />';
        $('#updating_now').append(html);
    }
});

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
            var new_value = $("#clo_"+td_id+" option:selected").text();
            if (new_value == 'נשלחה הזמנת רכש'){
                var order_num = $("#id_hazmanat_rechesh").val();
                console.log('order_num val: '+order_num)
                new_value = ':נשלחה הזמנת רכש'+'\n'+order_num;
            }
        }else{
            var new_value = $("#clo_"+td_id).val();
        }

    }
    console.log('new val: '+new_value)
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
//                console.log('changing: '+$(this).text());
                $(this).text(new_value);
            }
        });
    }
    if (td_id=='KM'){
        $('#mainlist tbody tr td.KM').each( function(){
            var km = parseInt($(this).text());
//            console.log('km == '+Number.isInteger(km))
            var km_min_20  = km - 200;
            if(km > 200){
                var km_min_str = km_min_20.toString();
//                console.log('km_min == '+km_min_str)
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
    if (td_id=='Contact'){
        var proj_num = $(this).closest('tr').find('.Project_num').text();
        console.log('project num: '+ proj_num)
        $('.Project_num').each( function(){
            console.log('project nums: '+ $(this).text())
            if($(this).text()==proj_num){
            $(this).closest('tr').find('.Contact').text(new_value);
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
//        console.log('update_sum_table fired')
        update_sum_table()
    };
    sum_sum_list();

}