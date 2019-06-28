function change_for_all_project_rows(class_name, new_val){
    var proj_num = $('#updating_now').closest('tr').find('.Project_num').text();
    console.log('change_for_all_project_rows project num: '+ proj_num)
    $.ajax({
        url: '/ajax/change_for_all_project_rows/',
        data: {
          'class_name': class_name,
          'new_val': new_val,
          'proj_num': proj_num,
        },
        dataType: 'json',
//        success: function(response){alert('project staged');},
        error:function(){alert('projects was not changed!');}
        });
    $('.Project_num').each( function(){
//        console.log('other project num: '+ $(this).text())
        if($(this).text()== proj_num){
            $(this).closest('tr').find('.'+class_name).text(new_val);
        }
    });
}

function in_array(val, array){
    var index = array.indexOf(val);
    if (index > -1){
        return true
    }else{
        return false
    }
}