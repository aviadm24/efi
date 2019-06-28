

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
            var status = $(this).closest('tr').find('.Status').text();
            if (status.includes('Cancled')||status.includes('Canceled')){
                $(this).closest('tr').find('.Status').text('END - Canceled');
                $(this).closest('tr').css('background-color', 'pink');
            }else{
                $(this).closest('tr').find('.Status').text('END');
                $(this).closest('tr').css('background-color', 'pink');
            }

        }
    });
    // remove projects from select
    $("#p_num option[value='"+proj_num+"']").remove();
//    $('#p_num').remove
}

function stage_project(past_projects){
//    var proj_num = $('#m_select').val()

    var past_projects_json = JSON.stringify(past_projects);
    console.log('proj to stage: '+ past_projects_json)
    $.ajax({
        url: '/ajax/stage_project/',
        data: {
          'past_projects_json': past_projects_json,
        },
        dataType: 'json',
//        success: function(response){alert('project staged');},
        error:function(){alert('projects was not staged!');}
        });
    $('#mainlist tbody tr td.Project_num').each(function() {
        if (in_array($(this).text(), past_projects)){
            var status = $(this).closest('tr').find('.Status').text();
            if (status.includes('Cancled')||status.includes('Canceled')){
                $(this).closest('tr').find('.Status').text('Past - Canceled');
                $(this).closest('tr').css('background-color', 'plum');
            }else{
                $(this).closest('tr').find('.Status').text('Past');
                $(this).closest('tr').css('background-color', 'plum');
            }

        }
    });
    // remove projects from select
//    var selectobject=document.getElementById("mySelect");
//      for (var i=0; i<selectobject.length; i++){
//      if (selectobject.options[i].value == 'A' )
//         selectobject.remove(i);
//      }
    //$("#p_num option[value='"+proj_num+"']").remove();

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



function check_status(){
    var today = moment();
    past_projects = [];
    past_projects_with_invoice = [];
    $('#mainlist tbody tr td.Date').each(function() {
        var date = $(this).text();
        var proj_num = $(this).closest('tr').find('.Project_num').text();
        var yesterday = moment().subtract(2, 'days').toDate();
//        let yesterday = moment().subtract(1, 'day').toDate();
//        console.log(yesterday)
        if (moment(date).isBefore(yesterday)){

            var hazmanat_rechesh = $(this).closest('tr').find('.Provider_status').text();
            var heshbonit = $(this).closest('tr').find('.Client_status').text();
            if (hazmanat_rechesh.includes('נשלחה') && heshbonit.startsWith('נשלחה חשבונית מס')){
//                console.log('project: '+proj_num)
                if (!in_array(proj_num, past_projects_with_invoice)){
                  past_projects_with_invoice.push(proj_num);
                }
            }else{
                var index = past_projects_with_invoice.indexOf(proj_num);
                if (index > -1) {
                  past_projects_with_invoice.splice(index, 1);
                }
            }
//            console.log('project: '+proj_num)
            if (!in_array(proj_num, past_projects)){
                past_projects.push(proj_num)
            }
        }else{

            var index = past_projects_with_invoice.indexOf(proj_num);
            if (index > -1) {
              past_projects_with_invoice.splice(index, 1);
            }
            var index = past_projects.indexOf(proj_num);
            if (in_array(proj_num, past_projects)) {
              past_projects.splice(index, 1);
            }

        }
    });
    console.log('past_projects_with_invoice: '+past_projects_with_invoice)
    console.log('past_projects: '+past_projects)
    return {
     past_projects: past_projects,
     past_projects_with_invoice: past_projects_with_invoice,
    };
}


var windowLoc = $(location).attr('pathname');
//console.log('windowLoc: '+windowLoc)
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
            $("#m_body").html('projects: \n' + past_proj_with_invoice + '\nwhere not closed yet!\n do you want to close the project?');
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

        if (windowLoc.endsWith('whole_list')){
            if (past_projects.length > 0){
                $('#m_select').empty();
                $("#m_body").html('projects: \n' + past_projects + '\n are finished waiting for invoice and going to be moved to staged projects');
                $('#m_select').hide();
                $('#before_update_buttons').show();
                $('#update_buttons').hide()
                $("#general_purpose_Modal").modal();
            }


            stage_project(past_projects);
        }

//        $('#mainlist tbody tr td.Project_num').each(function() {
//            var proj_num = $(this).text();
//            if (in_array(proj_num, past_projects)){
//                stage_project(proj_num);
//            }
//        });


    });

}
