
$(document).ready(function () {

    $('.Cost_per_client, .Cost_per_provider, .Cost_transfer_client, .Cost_transfer_provider, .Cost_extra_hour_client, .Cost_extra_hour_provider, .Cost_VIP_client, .Cost_VIP_provider, .shonot_client, .shonot_provider').each(function () {
        var from_db = $(this).text();

        var doll_or_shek = from_db % 100;
        var new_var = (from_db/100).toFixed(0)

        if (from_db != '—' && doll_or_shek==33 || doll_or_shek==34 || doll_or_shek==35){
//            console.log('from_db '+ from_db)
//            console.log('new var: '+ new_var)
            if (doll_or_shek == 33){
                $(this).text('$'+ new_var);
            }else if (doll_or_shek == 34){
                $(this).text('₪'+ new_var);
            }else{
                $(this).text('€'+ new_var);
            }
        }

    });
});
var table = $('#mainlist');
table = $('#mainlist').DataTable({
              paging: false,
//              "pageLength": 500,
              "order": [[ 5, "asc"], [12, "asc"]],
              "createdRow": function ( row, data, index ) {
//                    var today = new Date()
                    var today = moment().format('MM/DD/YYYY');
//                    if ( data[5].replace(/[\$,]/g, '') * 1 > 150000 ) {
//                        $('td', row).eq(5).addClass('highlight');
//                    }
                    if ( data[5]==today) {
                        $('td', row).addClass('highlight');
                    }
                },
                dom: 'Bfrtip',
                buttons: ['excel'],
                // https://datatables.net/forums/discussion/44588/hidden-fields-need-to-be-export-into-excel

                // "buttons": [ { extend: 'csv', text: 'CSV', exportOptions: { modifier: { search: 'applied' }}}, { extend: 'excel', text: 'Excel', exportOptions: { modifier: { search: 'applied' }}}, { extend: 'pdf', text: 'PDF', exportOptions: { modifier: { search: 'applied' }}}, { extend: 'print', text: 'Print visible', exportOptions: { modifier: { search: 'applied' }}} ]

//                "buttons": [{ extend: 'excel', text: 'Excel', exportOptions: { modifier: { search: 'applied' },
//                                                                                columns: '.exported',
//                                                                                format: {
//                body: function ( data, row, column, node ) {
//                    // Strip $ from salary column to make it numeric
//                    return column === 5 ?
//                        data.replace( /[$,]/g, '' ) :
//                        data;
//                }}
//                }}]

//              "iDisplayLength": -1,
//              "aLengthMenu": [[ 25, 50, 100,500,1000,-1], [25, 50,100,500,1000, "All"]],
              });
// https://datatables.net/reference/option/pageLength
// https://stackoverflow.com/questions/9443773/how-to-show-all-rows-by-default-in-jquery-datatable
//$('#example').dataTable({
//    paging: false
//});



//function update_sum_table(){
//    $("#sum_list_client td, #sum_list_provider td").each(function() {
//        var id = $(this).attr("id");
//        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id);
//        if (id == 'hakol_client'){
//            console.log('UPDATE sum table called')
//            console.log('check: '+[sum_dollar,sum_shekel,sum_euro])
//        }
//
//        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
//    });
//}
//
//
//$(document).ready(function() {
//    update_sum_table()
//});

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
    table.destroy();
//    $('#mainlist').find('td').not('.Extra_hours_provider, .Based_on_provider, .Extra_KM_provider, .Cost_per_provider, .Cost_transfer_provider, .Cost_extra_hour_provider, .Cost_VIP_provider, .Cost_shonot_provider').addClass('exported');
    table = $('#mainlist').DataTable({
              paging: false,
              "order": [[ 5, "asc"], [12, "asc"]],
              "createdRow": function ( row, data, index ) {
                    var today = moment().format('MM/DD/YYYY');
                    if ( data[5]==today) {
                        $('td', row).addClass('highlight');
                    }
                },
                dom: 'Bfrtip',
//                https://www.datatables.net/forums/discussion/38301/export-to-excel-only-visible-columns-not-working
                "buttons": [{ extend: 'excel', text: 'Excel', exportOptions: {columns: ':visible'}}],
                "columnDefs": [
                    {
                        "targets": [ 16,17,18,19,20,21,23,24,25,26,27,28,30,32,34,36,38 ],
                        "visible": false,
                        "searchable": true
                    },
//                    {
//                        "targets": [ 3 ],
//                        "visible": false
//                    }
                ]
              });

//    var columns = table.columns(1);
//    console.log('column: '+ column)
//    columns.visible( ! column.visible() );



    // delete unwanted td's
//    $('#mainlist').find('.Extra_hours_provider, .Based_on_provider, .Extra_KM_provider, .Cost_per_provider, .Cost_transfer_provider, .Cost_extra_hour_provider, .Cost_VIP_provider, .Cost_shonot_provider').hide();
    $('#mainlist').find('.Extra_hours_provider, .Extra_hours_client').hide();
    $('#sum_list_provider').hide()

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
          console.log('data label:'+dataLabel)
          console.log('provider == datalable:'+provider==dataLabel)
          return dataLabel  == provider;
       }
    );
    table.draw();
    table.destroy();
    table = $('#mainlist').DataTable({
              paging: false,
              "order": [[ 5, "asc"], [12, "asc"]],
              "createdRow": function ( row, data, index ) {
                    var today = moment().format('MM/DD/YYYY');
                    if ( data[5]==today) {
                        $('td', row).addClass('highlight');
                    }
                },
                dom: 'Bfrtip',
                "buttons": [{ extend: 'excel', text: 'Excel', exportOptions: {columns: ':visible'}}],
                "columnDefs": [
                    {
                        "targets": [ 0,1,2,3,4,17,18,19,20,21,22,23,25,26,27,28,29,31,33,35,37 ],
//                        "targets": 'Cost_shonot_client',

                        "visible": false,
                        "searchable": false
                    },
                ]
              });
    // delete unwanted td's

//    $('#mainlist').find('.Extra_hours_client, .Based_on_client, .Extra_KM_client, .Cost_per_client, .Cost_transfer_client, .Cost_extra_hour_client, .Cost_VIP_client, .Cost_shonot_client').hide();
    $('#mainlist').find('.Extra_hours_provider, .Extra_hours_client').hide();
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
        console.log(min)
        console.log(max)
        var createdAt = data[5] || 0; // Our date column in the table

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