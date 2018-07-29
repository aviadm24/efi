//function mouseDown(e){
//  e = e || window.event;
//  switch (e.which) {
//   case 1: alert('left'); break;
//   case 2: alert('middle'); break;
//   case 3: alert('right'); break;
//  }
//}

// https://stackoverflow.com/questions/18453480/get-the-row-id-of-html-table-after-right-click
var oddClick = true;
    $('#mainlist').find("tbody tr td:nth-child(26),td:nth-child(27),td:nth-child(28),td:nth-child(29),td:nth-child(30),td:nth-child(31),td:nth-child(32),td:nth-child(33),td:nth-child(34),td:nth-child(35)").bind("contextmenu",function(e) {
    var dollar_mode = $('#dollar_mode').prop('checked')
    if (dollar_mode){
        e.preventDefault();
        var text = $(this).text();
        var id = $(this).closest('tr').find('.id').text();
        var td_id = $(this).attr('class');

        if (oddClick){
            if (text.includes('₪')){
                var new_text = text.replace('₪','');
            }else{
                var new_text = text.replace('$','');
            }
            var int_to_save_in_db = parseInt(new_text)+ '33'
            console.log('int_to_save_in db:'+ int_to_save_in_db)
            $(this).text('$'+ new_text);
            $.ajax({
                url: '/ajax/add_dollar/',
                data: {
                  'id': id,
                  'td_id': td_id,
                  'new_int':int_to_save_in_db
                },
                dataType: 'json',
                });
        }else{
            if (text.includes('$')){
                var new_text = text.replace('$','');
            }else{
                var new_text = text.replace('₪','');
            }
            var int_to_save_in_db = parseInt(new_text+ '34')
            console.log('int_to_save_in db:'+ int_to_save_in_db)
            $(this).text('₪'+ new_text);
            $.ajax({
                url: '/ajax/add_shekel/',
                data: {
                  'id': id,
                  'td_id': td_id,
                  'new_int':int_to_save_in_db
                },
                dataType: 'json',
                });
        }
        oddClick = !oddClick;

        $("#sum_list td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel] = sum_price(id)
        $("#"+id).text('$'+sum_dollar+'\n'+'₪'+sum_shekel)
        });

//        alert($(this).text());
    }
});

$(document).ready(function () {

    $('table#mainlist tbody tr td:nth-child(26),td:nth-child(27),td:nth-child(28),td:nth-child(29),td:nth-child(30),td:nth-child(31),td:nth-child(32),td:nth-child(33),td:nth-child(34),td:nth-child(35)').each(function () {
        var from_db = $(this).text();

        var doll_or_shek = from_db % 100;
        var new_var = (from_db/100).toFixed(0)

        if (from_db != '—' && doll_or_shek==33 || doll_or_shek==34){
//            console.log('from_db '+ from_db)
//            console.log('new var: '+ new_var)
            if (doll_or_shek == 33){
                $(this).text('$'+ new_var);
            }else{
                $(this).text('₪'+ new_var);
            }
        }

    });
});

