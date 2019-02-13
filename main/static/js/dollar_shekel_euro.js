// €

$("#mainlist").find("td.Status").each(function() { //get all rows in table

    var status = $(this).text();
    console.log(status)
    if (status == 'Cancled'){
        $(this).closest('tr').css('background-color', 'red');
    }

});

var counter = 0;
$('#mainlist').find("tbody tr td:nth-child(26),td:nth-child(27),td:nth-child(28),td:nth-child(29),td:nth-child(30),td:nth-child(31),td:nth-child(32),td:nth-child(33),td:nth-child(34),td:nth-child(35)").bind("contextmenu",function(e) {
    var dollar_mode = $('#dollar_mode').prop('checked')
    if (dollar_mode){
        console.log('counter: '+counter)
        e.preventDefault();
        var text = $(this).text();
        var id = $(this).closest('tr').find('.id').text();
        var td_id = $(this).attr('class');
        console.log('td_id: '+td_id)

        counter++;
        if (td_id == 'Cost_extra_hour_client'){
            console.log('Extra_hours_client:'+ $('#Extra_hours_client').val())
//            if($('#Extra_hours_client').val()>0){
                switch(counter){
                case 1:
                    var added_text = dollar();
                    $(this).text(added_text)
                    console.log('text: '+ added_text)
                    break;
                case 2:
                    var added_text = shekel();
                    $(this).text(added_text)
                    break;
                case 3:
                    var added_text = euro();
                    $(this).text(added_text)
                    counter=0;
                    break;
                }
//            }

        }else if (td_id == 'Cost_extra_hour_provider'){
//            if($('#Extra_hours_provider').val()>0){
                switch(counter){
                case 1:
                    var added_text = dollar();
                    $(this).text(added_text)
                    console.log('text: '+ added_text)
                    break;
                case 2:
                    var added_text = shekel();
                    $(this).text(added_text)
                    break;
                case 3:
                    var added_text = euro();
                    $(this).text(added_text)
                    counter=0;
                    break;
                }
//            }
        }else{
            switch(counter){
            case 1:
                var added_text = dollar();
                $(this).text(added_text)
                console.log('text: '+ added_text)
                break;
            case 2:
                var added_text = shekel();
                $(this).text(added_text)
                break;
            case 3:
                var added_text = euro();
                $(this).text(added_text)
                counter=0;
                break;
            }
        }


        function dollar(){
            if (text.includes('₪')){
                var new_text = text.replace('₪','');
            }else if (text.includes('$')){
                var new_text = text.replace('$','');
            }else{
                var new_text = text.replace('€','');
            }
            var int_to_save_in_db = parseInt(new_text)+ '33'

            $.ajax({
                url: '/ajax/add_dollar/',
                data: {
                  'id': id,
                  'td_id': td_id,
                  'new_int':int_to_save_in_db
                },
                dataType: 'json',
                });
            return '$'+ new_text
        };

        function shekel(){
            if (text.includes('₪')){
                var new_text = text.replace('₪','');
            }else if (text.includes('$')){
                var new_text = text.replace('$','');
            }else{
                var new_text = text.replace('€','');
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
            return '₪'+ new_text
        };

        function euro(){
            if (text.includes('₪')){
                var new_text = text.replace('₪','');
            }else if (text.includes('$')){
                var new_text = text.replace('$','');
            }else{
                var new_text = text.replace('€','');
            }
            var int_to_save_in_db = parseInt(new_text+ '35')
            console.log('int_to_save_in db:'+ int_to_save_in_db)
            $(this).text('€'+ new_text);
            console.log('new_text:'+ $(this).text())
            $.ajax({
                url: '/ajax/add_euro/',
                data: {
                  'id': id,
                  'td_id': td_id,
                  'new_int':int_to_save_in_db
                },
                dataType: 'json',
                });
            return '€'+ new_text
        };

        $("#sum_list td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id)

//        var sum_array = sum_price(id)
//        var sum_text = ''
//        for(var i = 0; i < sum_array.length; i++) {
//        context = context[sum_array[i]];
//            if (context != 0){
//                if (i==0){
//                    sum_text += '$'+sum_dollar+
//                }
//
//            }
//        }
        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
        });

//        alert($(this).text());
    }
    sum_sum_list()
});

$(document).ready(function () {

    $('table#mainlist tbody tr td:nth-child(26),td:nth-child(27),td:nth-child(28),td:nth-child(29),td:nth-child(30),td:nth-child(31),td:nth-child(32),td:nth-child(33),td:nth-child(34),td:nth-child(35),td:nth-child(36),td:nth-child(37)').each(function () {
        var from_db = $(this).text();

        var doll_or_shek = from_db % 100;
        var new_var = (from_db/100).toFixed(0)

        if (from_db != '—' && doll_or_shek==33 || doll_or_shek==34 || doll_or_shek==35){
//            console.log('from_db '+ from_db)
//            console.log('new var: '+ new_var)
            if (doll_or_shek == 33){
                $(this).text('$'+ new_var);
            }else if (doll_or_shek == 34){
                $(this).text('₪'+ new_var);
            }else{
                $(this).text('€'+ new_var);
            }
        }

    });
});
// for update view!
$(document).ready(function () {

    $('.currency_sign').each(function () {
        var from_db = $(this).val();
//        console.log('from_db '+ from_db)
        var doll_or_shek = from_db % 100;
        var new_var = (from_db/100).toFixed(0)

        if (from_db != '—' && doll_or_shek==33 || doll_or_shek==34 || doll_or_shek==35){
            console.log('doll_or_shek '+ doll_or_shek)

            if (doll_or_shek == 33){
                $(this).val('$'+ new_var.toString());
            }else if (doll_or_shek == 34){
                console.log('new var: '+ '₪'+ new_var.toString())
                $(this).val('₪'+ new_var.toString());
            }else{
                $(this).val('€'+ new_var.toString());
            }
        }

    });
});

//var myform = $('#update_form');
//myform.onsubmit = function(){
//    $('.currency_sign').each(function () {
//    console.log('update_form submit')
//    var from_db = $(this).val();
//    console.log('from_db '+ from_db)
//});
//};

function DoSubmit(){
    console.log('update_form submit')
    $('.currency_sign').each(function () {
        var from = $(this).val();
        console.log('from_db '+ from)
        if (from.includes('₪')){
                $(this).val(from.replace('₪','')+'34');
            }else if (from.includes('$')){
                $(this).val(from.replace('$','')+'33');
            }else if (from.includes('$')){
                $(this).val(from.replace('€','')+'35');
            }


    });
    return true;
}
