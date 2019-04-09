


function on_cancle(){
    console.log("cancle_function")
    $("#mainlist").find("td.Status").each(function() { //get all rows in table
        var status = $(this).text();
        //console.log(status)
        if (status == 'Cancled'|| status == 'cancled'){
            $(this).closest('tr').css('color', 'red');
        }
    });
}

$(document).ready(function () {
    $("#mainlist").find("td.Status").each(function() { //get all rows in table
        var status = $(this).text();
        //console.log(status)
        if (status == 'Cancled'|| status == 'cancled'){
            $(this).closest('tr').css('color', 'red');
        }
    });
});