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
    // get old td value
    if (!$('#color_on').prop('checked')){
        var old_val = $(this).text()
        console.log('old val: '+old_val)
        $('#last_val').text(old_val)
        console.log('update function called')
        e.preventDefault();
        $('#clone_input').empty();
        $('#update_button').show();
        $('#update_values').hide();
        $('#new_date').hide();
        $('#new_date_time').hide();
        $('#flight_shcedule_update').hide();
        var id = $(this).closest('tr').find('.id').text();
        var canceled = $(this).closest('tr').find('.Canceled').text();
    //    var status = $(this).closest('tr').find('.Status').text();
        if (canceled=='✔'){
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
            if(td_id == 'Comments'){
                clo.text(old_val);
            }
            var clone_button = $('#update_button').clone();
            $(this).append(clo)
            $(this).append(clone_button)
            $(this).attr("id", "updating_now");
    //        $('#clone_input').append(clo)
    //        $('#clone_input').css({"border-style": "inset", cursor:"default"});
        }

        }

    }

});


// clone the select according to id
//http://www.jqueryfaqs.com/Articles/Clone-Copy-Dropdown-List-with-Selected-Value-using-jQuery.aspx

//$('#clo_status_cheshbonit_yeruka1').on("change", function () {
//https://stackoverflow.com/questions/18746381/dynamically-created-select-menu-on-change-not-working
$(document).on("change", '#clo_Provider_status', function () {
    var new_value = $("#clo_Provider_status option:selected").text()
    if (new_value == 'נשלחה הזמנת רכש'){
        alert('צריך לקלוט מספר הזמנת רכש')
        var html = '<input id="id_hazmanat_rechesh" type="text" />';
        $('#updating_now').append(html);
    }
});

$(document).on("change", '#clo_Client_status', function () {
    var new_value = $("#clo_Client_status option:selected").text()
    if (new_value == 'נשלחה חשבונית מס'){
        alert('צריך לקלוט מספר חשבונית לכל הפרוייקט')
        var html = '<input id="id_cheshbonit" type="text" />';
        $('#updating_now').append(html);
    }else if(new_value.includes('חשבונית עסקה')){
        alert('צריך לקלוט מספר חשבונית עסקה לכל הפרוייקט')
        var html = '<input id="id_cheshbonit_iska" type="text" />';
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
            if (td_id == 'Canceled'){
                new_value = $("#clo_"+td_id).val();
                if (new_value == 'True'){
                    tr_tag = $('#updating_now').closest('tr');
                    turn_cost_to_zero(tr_tag)
                }
            }else{
                var new_value = $("#clo_"+td_id+" option:selected").text();
                console.log('select new val: '+new_value)
                if (new_value == 'נשלחה הזמנת רכש'){
                    var order_num = $("#id_hazmanat_rechesh").val();
                    console.log('order_num val: '+order_num)
                    new_value = 'נשלחה הזמנת רכש'+'\n'+order_num;
                }else if(new_value == 'נשלחה חשבונית מס'){
                    var cheshbonit_num = $("#id_cheshbonit").val();
                    console.log('cheshbonit_num val: '+cheshbonit_num)
                    new_value = 'נשלחה חשבונית מס'+'\n'+cheshbonit_num;
                    change_for_all_project_rows('Client_status', new_value)
                }else if(new_value.includes('חשבונית עסקה')){
                    var cheshbonit_iska_num = $("#id_cheshbonit_iska").val();
                    console.log('cheshbonit_num val: '+cheshbonit_iska_num)
                    new_value = 'נשלחה חשבונית עסקה מס'+'\n'+cheshbonit_iska_num;
                    change_for_all_project_rows('Client_status', new_value)
                }
            }
        }else{
            var new_value = $("#clo_"+td_id).val();
            if (td_id.includes('Cost')){
                    if ( new_value.includes('$') || new_value.includes('€') || new_value.includes('₪') ){
                    }else{
                        if (new_value != ''){
                            new_value = '$'+new_value;
                        }
                    }
                }
        }

    }
    console.log('new val: '+new_value)
    if (new_value!='END'){

    $.ajax({
        url: '/ajax/update_cell/',
        data: {
          'id': id,
          'new_value': new_value,
          'td_id': td_id,
        },
        dataType: 'json',
//        success: function(response){alert('row was updated');},
        error:function(){alert('row was not updated!');}
        });

    }

    if (new_value == 'True'){ new_value = '✔'}else if(new_value == 'False'){new_value = '✘'}
    $('#updating_now').text(new_value);

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
        var proj_num = $('#updating_now').closest('tr').find('.Project_num').text();
        console.log('project num: '+ proj_num)
        $('.Project_num').each( function(){
            console.log('other project num: '+ $(this).text())
            if($(this).text()== proj_num){
                $(this).closest('tr').find('.Contact').text(new_value);
            }
        });
    }
    $('#new_value').val('');
    $("#clone_input").empty();
    $("#special_clone_input").children().hide();

    if (td_id=='Status'){
        var current_status = $('#updating_now').text();
        if (current_status == 'Cancled' || current_status == 'Canceled'){
            on_cancel(id)
        }else if(current_status == 'END'){
            var status_check = check_status();
            var past_proj_with_invoice = status_check.past_projects_with_invoice;
            var with_invoice_not_past = status_check.with_invoice_not_past;
            console.log('past_proj_with_invoice: '+past_proj_with_invoice)
            console.log('with_invoice_not_past: '+with_invoice_not_past)

            var pastProj = $('#updating_now').closest('tr').find('.Project_num').text();
            if (in_array(pastProj, past_proj_with_invoice)){
                $("#m_title").html('Are you sure?');
                $("#m_body").html('changing this cell to "END" means the whole project: '+pastProj+ '\nwill be sent to the "ended projects table" \nand changes will be restricted!');
                $('#m_select').show();
                $('#before_update_buttons').hide();
                $('#update_buttons').show()
                $('#m_select').empty();
                var option = '';
                   option += '<option value="'+ pastProj + '">' + pastProj + '</option>';
                $('#m_select').append(option);

                $("#general_purpose_Modal").modal();
            }else if(in_array(pastProj, with_invoice_not_past)){
                $("#m_title").html('Are you sure?');
                $("#m_body").html('The date of this project is still in main list - changing this cell to "END" means the whole project: '+pastProj+ '\nwill be sent to the "ended projects table" \nand changes will be restricted!');
                $('#m_select').show();
                $('#before_update_buttons').hide();
                $('#update_buttons').show()
                $('#m_select').empty();
                var option = '';
                   option += '<option value="'+ pastProj + '">' + pastProj + '</option>';
                $('#m_select').append(option);

                $("#general_purpose_Modal").modal();
            }else{
                $('#m_select').empty();
                $("#m_body").html('projects: \n' + past_projects + '\n can not be changed to END until invoice will be sent');
                $('#m_select').hide();
                $('#before_update_buttons').show();
                $('#update_buttons').hide()
                $("#general_purpose_Modal").modal();

                var old_val = $('#last_val').html();
                console.log('old_val: '+ old_val);
                $('#updating_now').text(old_val);
            }
        }
    };

    start_min_end_func();
    if (td_id=='Start_time' || td_id=='End_time' || td_id =='Based_on_client' || td_id =='Based_on_provider'){
//        console.log('update_sum_table fired')
        update_sum_table()
    };
    sum_sum_list();

}


$('.Status').on('change', '#clo_Status', function(){
    var current_status = $("#clo_Status option:selected").text();
    console.log('current: '+current_status)
    if(current_status=='END'){
        $("#m_title").html('Are you sure?');
            $("#m_body").html('changing this cell to "END" means the whole project: \nwill be sent to the "ended projects table" \nand changes will be restricted!');
            $('#m_select').hide();
            $('#before_update_buttons').show();
            $('#update_buttons').hide();
            $("#general_purpose_Modal").modal();
    }
});