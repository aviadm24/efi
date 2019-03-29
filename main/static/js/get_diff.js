
$('#datetimepicker1').on("change.datetimepicker", function (e) {
    var date = $('#datetimepicker1').datetimepicker('viewDate');
//    console.log('date: '+moment(date).format("dddd, MMMM DD YYYY"));
    $('#Start_time').datetimepicker('date', e.date);
    $('#End_time').datetimepicker('date', e.date);
    // https://tempusdominus.github.io/bootstrap-4/Usage/
    // linked datetime pickers!!!
});


function get_diff(start_time, end_time, base_c, base_p){
    // https://devhints.io/moment
    var startMinEnd = moment(end_time).diff(moment(start_time));
    console.log('startMinEnd: '+startMinEnd);
    //var difftMinBase = moment(startMinEnd,"HH:mm").diff(moment(base,"HH:mm"));
    var diff_c = startMinEnd - (3600000*base_c);
    var diff_p = startMinEnd - (3600000*base_p);
    //var d = moment.duration(difftMinBase);
    //https://stackoverflow.com/questions/18623783/get-the-time-difference-between-two-datetimes
    var extra_c = diff_c/3600000;
    var extra_p = diff_p/3600000;
    if (extra_c < 0){
        extra_c = 0;
    }
    if (extra_p < 0){
        extra_p = 0;
    }
    console.log('diff: '+extra_c);
    return [extra_c.toFixed(2), extra_p.toFixed(2)]
}

function start_min_end_func(){
    $('table#mainlist tbody tr').each(function () {
        var start_time = $(this).find(".Start_time").text();
        var end_time = $(this).find(".End_time").text();
        var base_c = $(this).find(".Based_on_client").text();
        var base_p = $(this).find(".Based_on_provider").text();
        var extra_c, extra_p = null;
        extras = get_diff(start_time, end_time, base_c, base_p);
        extra_c = extras[0]
        extra_p = extras[1]
        console.log('extra c: '+ extra_c)
        $(this).find(".Extra_hours_client").text(extra_c);
        $(this).find(".Extra_hours_provider").text(extra_p);
    });
}


$(document).ready(function() {
    start_min_end_func()
});



//function get_cost(){
//    var extra_c = $("#id_Extra_hours_client").val();
//    var extra_p = $("#id_Extra_hours_provider").val();
//    var base_cost_c = $("#id_Cost_extra_hour_client").val();
//    var base_cost_p = $("#id_Cost_extra_hour_provider").val();
//    var cost_c = extra_c*base_cost_c;
//    var cost_p = extra_p*base_cost_p;
//    $("#id_Cost_per_client").val(cost_c.toFixed(2));
//    $("#id_Cost_per_provider").val(cost_p.toFixed(2));
//}


//https://stackoverflow.com/questions/27398028/bootstrap-datetimepicker-trigger-dp-change-on-class
// https://stackoverflow.com/questions/47490154/how-can-i-get-date-object-from-a-bootstrap-datetime-picker-plugin
//$('#End_time').on("change.datetimepicker", function (e) {
//      date = $('#datetimepicker1').datetimepicker('viewDate');
//      get_diff();
//   });
