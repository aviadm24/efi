
function get_diff(){
    var start = $("#id_Start_time").val();
    var end = $("#id_End_time").val();
    var base = $("#id_Based_on").val();
    var startMinEnd = moment(end,"HH:mm").diff(moment(start,"HH:mm"));
    //var difftMinBase = moment(startMinEnd,"HH:mm").diff(moment(base,"HH:mm"));
    var difftMinBase = startMinEnd - (3600000*9);
    var d = moment.duration(difftMinBase);
    //https://stackoverflow.com/questions/18623783/get-the-time-difference-between-two-datetimes
    console.log('diff: '+startMinEnd)
    console.log('diff2: '+difftMinBase)
    console.log('d3: '+d)
    $("#id_Extra_hours").val(d.get("hours"));
}

$('#id_End_time').on('mouseup', function() {
    get_diff()
    //$(this).val() // get the current value of the input field.
});

//$("input").mouseup(function () {
//    alert("Changed!");
//});