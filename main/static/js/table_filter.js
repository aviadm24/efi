
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



function update_sum_table(){
    $("#sum_list_client td, #sum_list_provider td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id);
        if (id == 'hakol_client'){
            console.log('UPDATE sum table called')
            console.log('check: '+[sum_dollar,sum_shekel,sum_euro])
        }

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


//     $("#sum_list_client td, #sum_list_provider td").each(function() {
//        var id = $(this).attr("id");
//        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id)
//        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
//        //$("#"+id).text('$'+sum_dollar+'\n'+'₪'+sum_shekel)
//    });
    update_sum_table()
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
    $('#mainlist').find('.Extra_hours_provider, .Based_on_provider, .Extra_KM_provider, .Cost_per_provider, .Cost_transfer_provider, .Cost_extra_hour_provider, .Cost_VIP_provider, .shonot_provider').hide();
    $('#sum_list_provider').hide()
//    $('#mainlist').find('thead tr th:nth-child(15),th:nth-child(16),th:nth-child(17),th:nth-child(18),th:nth-child(19),th:nth-child(20),th:nth-child(23),th:nth-child(24),th:nth-child(27),th:nth-child(29),th:nth-child(31),th:nth-child(33),th:nth-child(35)').hide();
//    $('#mainlist').find('tbody tr td:nth-child(15),td:nth-child(16),td:nth-child(17),td:nth-child(18),td:nth-child(19),td:nth-child(20),td:nth-child(23),td:nth-child(24),td:nth-child(27),td:nth-child(29),td:nth-child(31),td:nth-child(33),td:nth-child(35)').hide();

    update_sum_table()
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

    $('#mainlist').find('.Extra_hours_client, .Based_on_client, .Extra_KM_client, .Cost_per_client, .Cost_transfer_client, .Cost_extra_hour_client, .Cost_VIP_client, .shonot_client').hide();
    $('#sum_list_client').hide()
    update_sum_table()
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
    update_sum_table()
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