
var table = $('#mainlist').DataTable();

function sum_price(cla){
    //console.log('cla'+cla)
    var sum_dollar = 0;
    var sum_shekel = 0;
    // iterate through each td based on class and add the values
    $("."+cla).each(function() {

        var value = $(this).text();
        if (value.includes('₪')){
            var new_value = parseInt(value.replace('₪',''));
        }else{
            if (value.includes('$')){
            var new_value = parseInt(value.replace('$',''));
            }
        }


        //console.log('value num:' + new_value)
        // add only if the value is number
        if(!isNaN(new_value) && new_value.length != 0) {
            if(value.includes("$")){
                sum_dollar += parseFloat(new_value);
            }else{
                if (value.includes('₪')){
                sum_shekel += parseFloat(new_value);
                }
            }
        }
    });
    return [sum_dollar,sum_shekel]
}

$(document).ready(function() {
    $("#sum_list td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel] = sum_price(id);
        $("#"+id).text('$'+sum_dollar+'\n'+'₪'+sum_shekel)
    });
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

    console.log('tables: '+$('#mainlist'))
    // hide unwanted td's
//    $('#mainlist').find('thead tr th:nth-child(18),th:nth-child(19),th:nth-child(20),th:nth-child(21),th:nth-child(22),th:nth-child(27),th:nth-child(29),th:nth-child(31),th:nth-child(33),th:nth-child(35)').hide();
//    $('#mainlist').find('tbody tr td:nth-child(18),td:nth-child(19),td:nth-child(20),td:nth-child(21),td:nth-child(22),td:nth-child(27),td:nth-child(29),td:nth-child(31),td:nth-child(33),td:nth-child(35)').hide();

     $("#sum_list td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar, sum_shekel] = sum_price(id)
        $("#"+id).text('$'+sum_dollar+'\n'+'₪'+sum_shekel)
    });
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
        var [sum_dollar,sum_shekel] = sum_price(id)
        $("#"+id).text('$'+sum_dollar+'\n'+'₪'+sum_shekel)
    });
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
        var [sum_dollar,sum_shekel] = sum_price(id)
        $("#"+id).text('$'+sum_dollar+'\n'+'₪'+sum_shekel)
    });
}



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