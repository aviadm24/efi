
function turn_cost_to_zero(closest_tr){
    closest_tr.css('color', 'red');
    closest_tr.find('.Extra_hours_client, .Based_on_client, .Extra_KM_client, .Cost_per_client, .Cost_transfer_client, .Cost_extra_hour_client, .Cost_VIP_client, .Cost_shonot_client, .Extra_hours_provider, .Based_on_provider, .Extra_KM_provider, .Cost_per_provider, .Cost_transfer_provider, .Cost_extra_hour_provider, .Cost_VIP_provider, .Cost_shonot_provider').text('0');
}

function on_cancel(id){
    console.log("on cancel function")
//    var id = closest_tr.find('.id').text();
    $.ajax({
        url: '/ajax/cancel_currency_fields/',
        data: {
          'id': id,
        },
        dataType: 'json',
//        success: function(response){alert('row was updated');},
        error:function(){alert('currency_fields were not turned to zero!');}
        });
    $("#mainlist").find("td.Status").each(function() { //get all rows in table
        var status = $(this).text();
        //console.log(status)
        if (status.includes('Cancled')|| status.includes('cancled')|| status.includes('Canceled')){
            var closest_tr = $(this).closest('tr');
            turn_cost_to_zero(closest_tr);
        }
    });
    update_sum_table()
    sum_sum_list()
}

$(document).ready(function () {
    $("#mainlist").find("td.Status").each(function() { //get all rows in table
        var status = $(this).text();
        //console.log(status)
        if (status.includes('Cancled')|| status.includes('cancled')|| status.includes('Canceled')){
            var closest_tr = $(this).closest('tr');
            turn_cost_to_zero(closest_tr);
            closest_tr.css('color', 'red');
//            $(this).closest('tr').css('color', 'red');
        }
    });
});

$(document).ready(function () {
    console.log('new cancel function')
    $("#mainlist").find("td.Status").each(function() { //get all rows in table
        var status = $(this).text();
        //console.log(status)
        if (status.includes('Cancled')|| status.includes('cancled')|| status.includes('Canceled')){
            var id = $(this).closest('tr').find('.id').text();
//            console.log('id to cancel: '+id)
            on_cancel(id)
        }
    });
});

$(document).ready(function () {
    $("#mainlist").find("td.Canceled").each(function() {
        var canceled = $(this).text();
        if (canceled == '✔'){
            var closest_tr = $(this).closest('tr');
            turn_cost_to_zero(closest_tr);
        }
//        console.log(canceled)

    });
});