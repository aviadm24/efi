

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
}

function dont_close_project(){
    var old_val = $('#last_val').html();
    console.log('old_val: '+ old_val)
    $('#updating_now').text(old_val)
}

var windowLoc = $(location).attr('pathname');
console.log('windowLoc: '+windowLoc)
if (windowLoc.endsWith('ended_projects')){
}else{
//console.log('not ended projects')

    $(document).ready(function () {
        var today = moment();
        past_projects = []
        $('#mainlist tbody tr td.Date').each(function() {
            var date = $(this).text();
            if (moment(date).isBefore()){
                var pastProj = $(this).closest('tr').find('.Project_num').text();
                var hazmanat_rechesh = $(this).closest('tr').find('.status_cheshbonit_yeruka1').text();
                var heshbonit = $(this).closest('tr').find('.status_cheshbonit_yeruka2').text();
                if (hazmanat_rechesh.startsWith('נשלחה הזמנת רכש') && heshbonit.startsWith('נשלחה חשבונית מס')){
                    var index = past_projects.indexOf(pastProj);
                    if (index == -1) {
                      past_projects.push(pastProj);
                    }
                }
            }else{
                var not_pastProj = $(this).closest('tr').find('.Project_num').text()
                var index = past_projects.indexOf(not_pastProj);
                if (index > -1) {
                  past_projects.splice(index, 1);
                }
            }
        });

    //    console.log('number of past projects: '+past_projects.length)
        if (past_projects.length > 0){
             $('#m_select').empty();
    // https://stackoverflow.com/questions/36621481/how-to-open-modal-from-function-call-jquery
    // https://www.tutorialsplane.com/pass-data-to-bootstrap-modal/
            $("#m_body").html('projects: \n' + past_projects + '\nwhere not closed yet!\n do you whant to close the project?');
            $('#m_select').show();
            $('#before_update_buttons').hide();
            $('#update_buttons').show()
            var option = '';
            for (var i=0;i<past_projects.length;i++){
               option += '<option value="'+ past_projects[i] + '">' + past_projects[i] + '</option>';
            }
            $('#m_select').append(option);

            $("#general_purpose_Modal").modal();
        }



    //    $.ajax({
    //        url: '/ajax/update_cell/',
    //        data: {
    //          'id': id,
    //          'new_value': km_min_str,
    //          'td_id': 'Extra_KM_provider',
    //        },
    //        dataType: 'json',
    //                    success: function(response){alert('row was updated');},
    //                    error:function(){alert('row was not updated!');}
    //        });

    });

}
