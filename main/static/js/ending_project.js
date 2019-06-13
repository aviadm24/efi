

function close_project(proj_num){
    var proj_num = $('#m_select').val()
    console.log('proj to close: '+ proj_num)
    $.ajax({
        url: '/ajax/end_project/',
        data: {
          'proj_num': proj_num,
        },
        dataType: 'json',
        success: function(response){alert('project ended and removed');},
        error:function(){alert('project was not ended!');}
        });
    $('#mainlist tbody tr td.Project_num').each(function() {
        if ($(this).text() == proj_num){
            $(this).closest('tr').find('.Status').text('END');
            $(this).closest('tr').css('background-color', 'pink');
        }
    });
    // remove projects from select
    $("#p_num option[value='"+proj_num+"']").remove();
//    $('#p_num').remove
}

function dont_close_project(){
    var old_val = $('#last_val').html();
    console.log('old_val: '+ old_val)
    $('#updating_now').text(old_val)
}

//function i_understand(){
//    var old_val = $('#last_val').html();
//    console.log('old_val: '+ old_val)
//    $('#updating_now').text(old_val)
//}

function in_array(val, array){
    var index = array.indexOf(val);
    if (index > -1){
        return true
    }else{
        return false
    }
}

function check_status(){
    var today = moment();
    past_projects = [];
    past_projects_with_invoice = [];
    $('#mainlist tbody tr td.Date').each(function() {
        var date = $(this).text();
        var proj_num = $(this).closest('tr').find('.Project_num').text();
        if (moment(date).isBefore()){

            var hazmanat_rechesh = $(this).closest('tr').find('.Provider_status').text();
            var heshbonit = $(this).closest('tr').find('.Client_status').text();
            if (hazmanat_rechesh.startsWith('נשלחה הזמנת רכש') && heshbonit.startsWith('נשלחה חשבונית מס')){
                if (!in_array(proj_num, past_projects_with_invoice)){
                  past_projects_with_invoice.push(proj_num);
                }
            }else{
                if (!in_array(proj_num, past_projects)){
                    past_projects.push(proj_num)
                }
            }
        }else{

            var index = past_projects_with_invoice.indexOf(proj_num);
            if (index> -1) {
              past_projects_with_invoice.splice(index, 1);
            }
            var index = past_projects.indexOf(proj_num);
            if (in_array(proj_num, past_projects)) {
              past_projects.splice(index, 1);
            }

        }
    });
//    console.log('past projects: '+past_projects)
    return {
     past_projects: past_projects,
     past_projects_with_invoice: past_projects_with_invoice,
    };
}


var windowLoc = $(location).attr('pathname');
console.log('windowLoc: '+windowLoc)
if (windowLoc.endsWith('ended_projects')){
}else{
//console.log('not ended projects')

    $(document).ready(function () {
        var today = moment();
//        past_projects = []
//        check_status()
        var status_check = check_status();
        var past_proj_with_invoice = status_check.past_projects_with_invoice;
        var past_projects = status_check.past_projects;
//        console.log('past_proj_with_invoice: '+past_proj_with_invoice)
//        console.log('past_proj: '+past_projects)


        if (past_proj_with_invoice.length > 0){
             $('#m_select').empty();
    // https://stackoverflow.com/questions/36621481/how-to-open-modal-from-function-call-jquery
    // https://www.tutorialsplane.com/pass-data-to-bootstrap-modal/
            $("#m_body").html('projects: \n' + past_proj_with_invoice + '\nwhere not closed yet!\n do you whant to close the project?');
            $('#m_select').show();
            $('#before_update_buttons').hide();
            $('#update_buttons').show()
            var option = '';
            for (var i=0;i<past_proj_with_invoice.length;i++){
               option += '<option value="'+ past_proj_with_invoice[i] + '">' + past_proj_with_invoice[i] + '</option>';
            }
            $('#m_select').append(option);

            $("#general_purpose_Modal").modal();
        }

        if (past_projects.length > 0){
            $('#m_select').empty();
            $("#m_body").html('projects: \n' + past_projects + '\n are finished waiting for invoice');
            $('#m_select').hide();
            $('#before_update_buttons').show();
            $('#update_buttons').hide()
//            var option = '';
//            for (var i=0;i<past_projects.length;i++){
//               option += '<option value="'+ past_projects[i] + '">' + past_projects[i] + '</option>';
//            }
//            $('#m_select').append(option);

            $("#general_purpose_Modal").modal();
        }
        $('#mainlist tbody tr td.Project_num').each(function() {
            var proj_num = $(this).text();
            if (in_array(proj_num, past_projects)){
                $(this).closest('tr').css('background-color', 'plum');
            }
        });


    });

}