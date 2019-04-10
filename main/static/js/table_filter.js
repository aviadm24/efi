
var table = $('#mainlist').DataTable({
              paging: false,
//              "pageLength": 500,
              "order": [[ 4, "desc" ]],
              "createdRow": function ( row, data, index ) {
//                    var today = new Date()
                    var today = moment().format('MM/DD/YYYY');
//                    if ( data[5].replace(/[\$,]/g, '') * 1 > 150000 ) {
//                        $('td', row).eq(5).addClass('highlight');
//                    }
                    if ( data[4]==today) {
                        $('td', row).addClass('highlight');
                    }
                },
//              "iDisplayLength": -1,
//              "aLengthMenu": [[ 25, 50, 100,500,1000,-1], [25, 50,100,500,1000, "All"]],
              });
// https://datatables.net/reference/option/pageLength
// https://stackoverflow.com/questions/9443773/how-to-show-all-rows-by-default-in-jquery-datatable
//$('#example').dataTable({
//    paging: false
//});

function sum_sum_list(){
    console.log( 'sum sum list called!')
    var sum_dollar = 0;
    var sum_shekel = 0;
    var sum_euro = 0;

    $("#sum_list td").each(function() {
        if($(this).attr('id')=='hakol' ||$(this).attr('id')=='maam'){}
        else{
            if ( $(this).not(':hidden') ) {
                var price_str = $(this).html();
                // https://stackoverflow.com/questions/34609571/extract-numbers-from-string-and-store-them-in-array-javascript
                var dollar = price_str.match(/\d+/g)[0];
                var shekel = price_str.match(/\d+/g)[1]
                var euro = price_str.match(/\d+/g)[2]
                console.log('shekel: '+shekel)

                var dollar_num = parseInt(dollar);
                sum_dollar += dollar_num;
                console.log('sum_dollar: '+sum_dollar)
                var shekel_num = parseInt(shekel);
                sum_shekel += shekel_num;
                var euro_num = parseInt(euro);
                sum_euro += euro_num;
//                console.log($(this).attr('id'))
             }
        }

    });
    $("#hakol").html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
}

function sum_price(cla){
    var sum_dollar = 0;
    var sum_shekel = 0;
    var sum_euro = 0;
    var new_value = 0;
    // iterate through each td based on class and add the values
    $("."+cla).each(function() {
        if (cla == 'Cost_extra_hour_client'){
            var cost_extra =  parseInt($(this).closest('tr').find('.Extra_hours_client').text());
//            console.log('cost_extra: '+ cost_extra)
            if(cost_extra>0){
                console.log('cost_extra: '+ cost_extra)
                var value = $(this).text();
                    if (value.includes('₪')){
                        new_value = parseInt(value.replace('₪',''));
                        sum_shekel += new_value*cost_extra;
                    }else if (value.includes('$')){
                        new_value = parseInt(value.replace('$',''));

                        sum_dollar += new_value*cost_extra;
                        console.log('sum_dollar: '+ sum_dollar)
                    }else if (value.includes('€')){
                        new_value = parseInt(value.replace('€',''));
                        sum_euro += new_value*cost_extra;
                    }else{
                        new_value = parseInt(value);
                    }
            }
        }else if(cla == 'Cost_extra_hour_provider'){
            var cost_extra =  parseInt($(this).closest('tr').find('.Extra_hours_provider').text());
            if(cost_extra>0){
                var value = $(this).text();
                    if (value.includes('₪')){
                        new_value = parseInt(value.replace('₪',''));
                        sum_shekel += new_value*cost_extra;
                    }else if (value.includes('$')){
                        new_value = parseInt(value.replace('$',''));
                        sum_dollar += new_value*cost_extra;
                    }else if (value.includes('€')){
                        new_value = parseInt(value.replace('€',''));
                        sum_euro += new_value*cost_extra;
                    }else{
                        new_value = parseInt(value);
                    }
            }
        }else{
            var value = $(this).text();
            if (value.includes('₪')){
                new_value = parseInt(value.replace('₪',''));
                sum_shekel += new_value;
            }else if (value.includes('$')){
                new_value = parseInt(value.replace('$',''));
                sum_dollar += new_value;
            }else if (value.includes('€')){
                new_value = parseInt(value.replace('€',''));
                sum_euro += new_value;
            }else{
                new_value = parseInt(value);
            }
        }


        // add only if the value is number
        // added this in the code above
//        if(!isNaN(new_value) && new_value.length != 0) {
//            if(value.includes("$")){
//                sum_dollar += parseFloat(new_value);
//            }else if (value.includes('₪')){
//                sum_shekel += parseFloat(new_value);
//            }else if (value.includes('€')){
//                sum_euro += parseFloat(new_value);
//            }
//        }
    });
    return [sum_dollar,sum_shekel,sum_euro]
}

function update_sum_table(){
    $("#sum_list td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id);
        console.log('check: '+[sum_dollar,sum_shekel,sum_euro])
        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
    });
}


$(document).ready(function() {
    update_sum_table()
//    $("#sum_list td").each(function() {
//        var id = $(this).attr("id");
//        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id);
//        console.log()
//        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
//    });
});

function project_filter() {
    var project_num = $('#p_num').val()
    //console.log('project num:' + project_num)
// https://stackoverflow.com/questions/31458060/is-it-possible-to-filter-a-jquery-datatable-by-data-attribute
    $.fn.dataTable.ext.search.push(
       function(settings, data, dataIndex) {
          var dataLabel = table
              .row(dataIndex)         //get the row to evaluate
              .nodes()                //extract the HTML - node() does not support to$
              .to$()                  //get as jQuery object
              .find('td.Project_num') //find column with data-label
              .text();                //get the value of data-label
          //console.log('data label:'+dataLabel)
          return dataLabel  == project_num;
       }
    );
//    $.fn.dataTable.ext.search.push(
//       function(settings, data, dataIndex) {
//          console.log('project num:' +  $(table.row(dataIndex).node()).attr('data-user') == 5;
//          return $(table.row(dataIndex).node()).td.text() == project_num;
//       }
//    );
    table.draw();

//    console.log('tables: '+$('#mainlist'))
    // hide unwanted td's
//    $('#mainlist').find('thead tr th:nth-child(18),th:nth-child(19),th:nth-child(20),th:nth-child(21),th:nth-child(22),th:nth-child(27),th:nth-child(29),th:nth-child(31),th:nth-child(33),th:nth-child(35)').hide();
//    $('#mainlist').find('tbody tr td:nth-child(18),td:nth-child(19),td:nth-child(20),td:nth-child(21),td:nth-child(22),td:nth-child(27),td:nth-child(29),td:nth-child(31),td:nth-child(33),td:nth-child(35)').hide();

     $("#sum_list td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id)
        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
        //$("#"+id).text('$'+sum_dollar+'\n'+'₪'+sum_shekel)
    });
    sum_sum_list()
}

function customer_filter() {

    var customer = $('#customer').val()
    console.log('Customer:' + customer)
    $.fn.dataTable.ext.search.push(
       function(settings, data, dataIndex) {
          var dataLabel = table
              .row(dataIndex)
              .nodes()
              .to$()
              .find('td.Customer')
              .text();
          //console.log('data label:'+dataLabel)
          return dataLabel  == customer;
       }
    );
    table.draw();

    // delete unwanted td's
    $('#mainlist').find('thead tr th:nth-child(15),th:nth-child(16),th:nth-child(17),th:nth-child(18),th:nth-child(19),th:nth-child(20),th:nth-child(23),th:nth-child(24),th:nth-child(27),th:nth-child(29),th:nth-child(31),th:nth-child(33),th:nth-child(35)').hide();
    $('#mainlist').find('tbody tr td:nth-child(15),td:nth-child(16),td:nth-child(17),td:nth-child(18),td:nth-child(19),td:nth-child(20),td:nth-child(23),td:nth-child(24),td:nth-child(27),td:nth-child(29),td:nth-child(31),td:nth-child(33),td:nth-child(35)').hide();

    $("#sum_list td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id)
        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
    });

    $('#sum_list').find('thead tr th:nth-child(2),th:nth-child(4),th:nth-child(6),th:nth-child(8)').hide();
    $('#sum_list').find('tbody tr td:nth-child(2),td:nth-child(4),td:nth-child(6),td:nth-child(8)').hide();
    sum_sum_list()
}

function provider_filter() {

    var provider = $('#provider').val()
    console.log('provider:' + provider)
    $.fn.dataTable.ext.search.push(
       function(settings, data, dataIndex) {
          var dataLabel = table
              .row(dataIndex)
              .nodes()
              .to$()
              .find('td.Provider')
              .text();
          //console.log('data label:'+dataLabel)
          return dataLabel  == provider;
       }
    );
    table.draw();

    // delete unwanted td's
    $('#mainlist').find('thead tr th:nth-child(18),th:nth-child(19),th:nth-child(20),th:nth-child(21),th:nth-child(22),th:nth-child(26),th:nth-child(28),th:nth-child(30),th:nth-child(32),th:nth-child(34),th:nth-child(36)').hide();
    $('#mainlist').find('tbody tr td:nth-child(18),td:nth-child(19),td:nth-child(20),td:nth-child(21),td:nth-child(22),td:nth-child(26),td:nth-child(28),td:nth-child(30),td:nth-child(32),td:nth-child(34),td:nth-child(36)').hide();

     $("#sum_list td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id)
        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
    });

    $('#sum_list').find('thead tr th:nth-child(1),th:nth-child(3),th:nth-child(5),th:nth-child(7)').hide();
    $('#sum_list').find('tbody tr td:nth-child(1),td:nth-child(3),td:nth-child(5),td:nth-child(7)').hide();
    sum_sum_list()

}
//https://stackoverflow.com/questions/38717543/how-do-i-filter-date-range-in-datatables
function date_filter(){
    $.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min  = $('#id_start').val();
        var max  = $('#id_end').val();
        var createdAt = data[4] || 0; // Our date column in the table

        if  (
                ( min == "" || max == "" )
                ||
                ( moment(createdAt).isSameOrAfter(min) && moment(createdAt).isSameOrBefore(max) )
            )
        {
            return true;
        }
        return false;
        }
    );
    table.draw();
    $("#sum_list td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id)
        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
    });
    sum_sum_list()
}
// Re-draw the table when the a date range filter changes
//$('.date-range-filter').change( function() {
//    table.draw();
//} );
// https://stackoverflow.com/questions/30086341/datatable-hide-and-show-rows-based-on-a-button-click-event

$("#hide").click(function() {
    $.fn.dataTable.ext.search.push(
       function(settings, data, dataIndex) {
          return $(table.row(dataIndex).node()).attr('data-user') == 5;
       }
    );
    table.draw();
});

//$("#reset").click(function() {
//    $.fn.dataTable.ext.search.pop();
//    table.draw();
//    $('#mainlist thead tr th').show();
//    $('#mainlist tbody tr td').show();
//    //console.log($('#p_num').data('default'))
//    $('#p_num').val(0);
//    $('#customer').val(1);
//    $('#provider').val(1);
//});