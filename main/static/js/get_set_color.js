// https://stackoverflow.com/questions/17843478/changing-the-color-of-a-row-on-click?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
$(document).ready(function () {



//    $('table.mainlist tr').click(function () {
//        var color = $('#custom').val();
//        console.log('main list tr')
//        //Check to see if background color is set or if it's set to white.
//        $('#id_Color').val(color);
//        if(this.style.background == "" || this.style.background =="white") {
//            $(this).css('background', color);
//        }
//    });


    $('table tr').each(function () {
        var color_id = $(this).find(".color_id").html();
//        var color_id = $('td.color_id').text();
//        console.log('color id:' + color_id)
        $(this).css('background', color_id);
    });


});

//https://stackoverflow.com/questions/14460421/get-the-contents-of-a-table-row-with-a-button-click?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa