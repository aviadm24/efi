// https://stackoverflow.com/questions/17843478/changing-the-color-of-a-row-on-click?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
$(document).ready(function () {



    $('tr').click(function () {
        var color = $('#custom').val();

        //Check to see if background color is set or if it's set to white.
        $('#id_Color').val(color);
        if(this.style.background == "" || this.style.background =="white") {
            $(this).css('background', color);
        }
//        else {
//            $(this).css('background', 'white');
//        }
    });


    $('table tr').each(function () {
        var color_id = $(this).find(".color_id").html();
//        var color_id = $('td.color_id').text();
        console.log('color id:' + color_id)
        $(this).css('background', color_id);
    });


});

$('#id_Type_of_service').on("change", function (e) {
    console.log('id_Type_of_service change')
    hide_for_transfer();
});


// if type of service is transfer then black out some td's
function hide_for_transfer() {
    var transfer = $('#id_Type_of_service option:selected').text();
    // https://stackoverflow.com/questions/10613873/get-the-jquery-index-of-td-element
    console.log('Type_of_service:' + transfer)
    if(transfer == "Transfer") {
        $('td:nth-child(9),th:nth-child(9)').hide();
        //$('#id_Type_of_service').hide();
    }
}

//https://stackoverflow.com/questions/14460421/get-the-contents-of-a-table-row-with-a-button-click?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa