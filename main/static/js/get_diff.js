
function get_diff(){
    var start = $("#id_Start_time").val();
    var end = $("#id_End_time").val();
    var base = $("#id_Based_on").val();
    var startMinEnd = moment(end,"dddd HH:mm a").diff(moment(start,"dddd HH:mm a"));
    //var difftMinBase = moment(startMinEnd,"HH:mm").diff(moment(base,"HH:mm"));
    var difftMinBase = startMinEnd - (3600000*9);
    var d = moment.duration(difftMinBase);
    //https://stackoverflow.com/questions/18623783/get-the-time-difference-between-two-datetimes
    var extra = difftMinBase/3600000
    console.log('diff2: '+extra)
    $("#id_Extra_hours").val(extra.toFixed(2));
}

//https://stackoverflow.com/questions/27398028/bootstrap-datetimepicker-trigger-dp-change-on-class
$('#id_End_time').on("dp.change",function() {
    console.log('change')
    get_diff()
    //$(this).val() // get the current value of the input field.
});

$(document).ready(function()
{
 $("#id_DepOrArr").change(function()
 {
  if($(this).val() == "Arr")
  {
   $("#id_Time_of_PU").show();
  }
  else
  {
   $("#id_Time_of_PU").hide();
  }
 });
 $("#id_Time_of_PU").hide();
});


//function DepArrCheck() {
//  var deporarr = $('#id_DepOrArr').val();
//  console.log(deporarr);
//  if (deporarr == 'Dep') {
//      console.log('Dep req');
//      $('#id_Time_of_PU').style.display = 'none';
//  }
//  else{
//      console.log('Arr req');
//      $('#id_Time_of_PU').style.display = 'block';
//  }
//}
//DepArrCheck()