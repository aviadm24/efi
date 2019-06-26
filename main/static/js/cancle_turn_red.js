
function turn_cost_to_zero(closest_tr){
    closest_tr.find('.Extra_hours_client, .Based_on_client, .Extra_KM_client, .Cost_per_client, .Cost_transfer_client, .Cost_extra_hour_client, .Cost_VIP_client, .shonot_client .Extra_hours_provider, .Based_on_provider, .Extra_KM_provider, .Cost_per_provider, .Cost_transfer_provider, .Cost_extra_hour_provider, .Cost_VIP_provider, .shonot_provider').text('0');
}

function on_cancle(){
    console.log("cancle_function")
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