$(document).ready(function () {
    var today = moment();
    past_projects = []
    $('#mainlist tbody tr td.Date').each(function() {
        var date = $(this).text();
        if (moment(date).isBefore()){
            console.log(date+ ' befor: '+ moment().format("MM/DD/YYYY"))
            var pastProj = $(this).closest('tr').find('.Project_num').text();
            var index = past_projects.indexOf(pastProj);
            if (index == -1) {
              past_projects.push(pastProj);
            }

        }else{
            var not_pastProj = $(this).closest('tr').find('.Project_num').text()
            var index = past_projects.indexOf(not_pastProj);
            if (index > -1) {
              past_projects.splice(index, 1);
            }
        }
    });
//    past_projects_set = new Set(past_projects)
//    var getEntriesArry = past_projects_set.entries();
//    console.log('past projects: '+getEntriesArry.next().value)
    console.log('past projects: '+past_projects)
    alert('projects: ' + past_projects + 'where not closed yet!')


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