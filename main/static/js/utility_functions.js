
function in_array(val, array){
    var index = array.indexOf(val);
    if (index > -1){
        return true
    }else{
        return false
    }
}

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
        success: success,
        error:function(){alert('projects was not changed!');}
        });

    function success(data) {
        console.log(data.id_list)

        var id_list = data.id_list;
        $('.id').each( function(){
            console.log(id_list.indexOf(parseInt($(this).text())))
            console.log('other project num: '+ $(this).text())
            if(in_array(parseInt($(this).text()),id_list) ){

                $(this).closest('tr').find('.'+class_name).text(new_val);
            }
        });
    }

}

