
function get_diff(){
    var start = $("#id_Start_time").val();
    var end = $("#id_End_time").val();
    var base_c = $("#id_Based_on_client").val();
    var base_p = $("#id_Based_on_provider").val();
    //console.log('Based_on: '+base_c);
    var startMinEnd = moment(end).diff(moment(start));
    //console.log('startMinEnd: '+startMinEnd);
    //var difftMinBase = moment(startMinEnd,"HH:mm").diff(moment(base,"HH:mm"));
    var diff_c = startMinEnd - (3600000*base_c);
    var diff_p = startMinEnd - (3600000*base_p);
    //var d = moment.duration(difftMinBase);
    //https://stackoverflow.com/questions/18623783/get-the-time-difference-between-two-datetimes
    var extra_c = diff_c/3600000;
    var extra_p = diff_p/3600000;
    //console.log('diff: '+extra_c);
    $("#id_Extra_hours_client").val(extra_c.toFixed(2));
    $("#id_Extra_hours_provider").val(extra_p.toFixed(2));
    get_cost();
}

function get_cost(){
    var extra_c = $("#id_Extra_hours_client").val();
    var extra_p = $("#id_Extra_hours_provider").val();
    var base_cost_c = $("#id_Cost_extra_hour_client").val();
    var base_cost_p = $("#id_Cost_extra_hour_provider").val();
    //console.log('extra_c: '+extra_c);
    //console.log('base_cost_c: '+base_cost_c);
    var cost_c = extra_c*base_cost_c;
    var cost_p = extra_p*base_cost_p;
    //console.log('cost c: '+cost_c);
    $("#id_Cost_per_client").val(cost_c.toFixed(2));
    $("#id_Cost_per_provider").val(cost_p.toFixed(2));

}


//https://stackoverflow.com/questions/27398028/bootstrap-datetimepicker-trigger-dp-change-on-class
//$('#id_End_time').on("change.datetimepicker",function() {
    //console.log('change')
    //get_diff()
    //$(this).val() // get the current value of the input field.
//});

// https://stackoverflow.com/questions/47490154/how-can-i-get-date-object-from-a-bootstrap-datetime-picker-plugin
$('#End_time').on("change.datetimepicker", function (e) {
      //date = $('#datetimepicker1').datetimepicker('viewDate');
      //console.log('change to: '+date);
      get_diff();
   	  //$('#getDate').text(date);
   });

$('#id_Cost_extra_hour_client, #id_Cost_extra_hour_provider').on('input', function() {
    //console.log('extra hour was changed!');
    var start = $('#id_Start_time').val(); // get the current value of the input field.
    if (start != ''){
        get_diff();
    }

});

$('#id_Based_on_client, #id_Based_on_provider').on("change", function (e) {
      get_diff();
   });

$('#id_Extra_hours_client, #id_Extra_hours_provider').on("change", function (e) {
      //console.log('extra hour was changed!')
      get_diff();
      //get_cost();
   });

$(document).ready(function() {
    $('table#mainlist tbody tr').each(function () {
        var id = $(this).find("td").eq(0).html();
        console.log('id: '+ id);
        $(this).find("td").eq(0).html('<a href="/update_row/'+id+'">'+id+'</a>');
    });
});