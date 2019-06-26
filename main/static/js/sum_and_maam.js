//$(document).ready(function() {
//
//});

function sum_price(cla){
    var sum_dollar = 0;
    var sum_shekel = 0;
    var sum_euro = 0;
    var new_value = 0;
    // iterate through each td based on class and add the values
    $("#mainlist td."+cla).each(function() {
        var row_status = $(this).closest('tr').find('.Status').text();
//        console.log('row status: ' + row_status)
        if (row_status == 'cancled' || row_status == 'Cancled'){}else{

            if (cla == 'Cost_extra_hour_client'){
                var cost_extra =  parseFloat($(this).closest('tr').find('.Extra_hours_client').html());
//                var cost_extra =  parseFloat($(this).closest('tr').find('.Extra_hours_client:hidden').html());
//                console.log('cost_extra client: '+ cost_extra)
                if(cost_extra>0){
//                    console.log('cost_extra2: '+ cost_extra)
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
                            console.log('sum_euro: '+ sum_euro)
                        }else{
                            new_value = parseInt(value);
                        }
                }
            }else if(cla == 'Cost_extra_hour_provider'){
                var cost_extra =  parseFloat($(this).closest('tr').find('.Extra_hours_provider').text());
//                console.log('cost_extra provider: '+ cost_extra)
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
//                console.log('sum and maam  - value: '+ new_value)
//                if (isNaN(new_value)){
//                    var row_proj_num = $(this).closest('tr').find('.Project_num').text();
//                    alert('in project number: '+row_proj_num+ 'cell name: '+ cla+'there is a problem with a number')
//                }
            }
        }
    });
    return [sum_dollar,sum_shekel,sum_euro]
}

function update_sum_table(){
    $("#sum_list_client td, #sum_list_provider td").each(function() {
        var id = $(this).attr("id");
        var [sum_dollar,sum_shekel,sum_euro] = sum_price(id);
        if (id == 'hakol_client'){
//            console.log('UPDATE sum table called')
//            console.log('check: '+[sum_dollar,sum_shekel,sum_euro])
        }

        $("#"+id).html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
    });
}


$(document).ready(function() {
    update_sum_table()
});

function sum_sum_list(){
//    console.log( 'sum sum list called!')
    var sum_dollar = 0;
    var sum_shekel = 0;
    var sum_euro = 0;
    // https://stackoverflow.com/questions/5767334/jquery-get-elements-without-display-none
    $('#sum_list_client td:not([style*="display: none"])').each(function() {
        if($(this).attr('id')=='hakol_client' ||$(this).attr('id')=='maam_client'){}
        else{
            if ( $(this).not(':hidden') ) {
                var price_str = $(this).html();
//                console.log('price_str: '+$(this).html())
                // https://stackoverflow.com/questions/34609571/extract-numbers-from-string-and-store-them-in-array-javascript
                var dollar_shekel_euro_array = price_str.split('<br>');
//                console.log('new _array: '+dollar_shekel_euro_array)
//                var dollar = price_str.match(/\d+/g)[0];
//                var shekel = price_str.match(/\d+/g)[1]
//                var euro = price_str.match(/\d+/g)[2]
                var dollar = parseFloat(dollar_shekel_euro_array[0].replace(/[^\d.]/g,''));
                var shekel = parseFloat(dollar_shekel_euro_array[1].replace(/[^\d.]/g,''));
                var euro = parseFloat(dollar_shekel_euro_array[2].replace(/[^\d.]/g,''));
//                console.log('shekel: '+shekel+ ':' +$(this).attr('id'))

                var dollar_num = dollar;
                sum_dollar += dollar_num;
//                console.log('sum_dollar: '+sum_dollar)
                var shekel_num = shekel;
                sum_shekel += shekel_num;
//                console.log('sum_shekel: '+sum_shekel)
                var euro_num = euro;
                sum_euro += euro_num;
//                console.log($(this).attr('id'))
             }
        }

    });
    $("#hakol_client").html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)

    var sum_dollar = 0;
    var sum_shekel = 0;
    var sum_euro = 0;
    $('#sum_list_provider td:not([style*="display: none"])').each(function() {
        if($(this).attr('id')=='hakol_provider' ||$(this).attr('id')=='maam_provider'){}
        else{
            if ( $(this).not(':hidden') ) {
                var price_str = $(this).html();
                var dollar_shekel_euro_array = price_str.split('<br>');
                var dollar = parseFloat(dollar_shekel_euro_array[0].replace(/[^\d.]/g,''));
                var shekel = parseFloat(dollar_shekel_euro_array[1].replace(/[^\d.]/g,''));
                var euro = parseFloat(dollar_shekel_euro_array[2].replace(/[^\d.]/g,''));
//                console.log('shekel: '+shekel+ ':' +$(this).attr('id'))

                var dollar_num = parseInt(dollar);
                sum_dollar += dollar_num;
//                console.log('sum_dollar: '+sum_dollar)
                var shekel_num = parseInt(shekel);
                sum_shekel += shekel_num;
                var euro_num = parseInt(euro);
                sum_euro += euro_num;
//                console.log($(this).attr('id'))
             }
        }

    });
    $("#hakol_provider").html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
}

function maam(){
    var sum_dollar_maam = 0;
    var sum_shekel_maam = 0;
    var sum_euro_maam = 0;

    $("#sum_list_client td").each(function() {
        if ($(this).attr('id')=='hakol_client' || $(this).attr('id')=='maam_client'){}
        else{
                if ( $(this).is(':visible') ) {
                    var price_str = $(this).html();
                    // https://stackoverflow.com/questions/34609571/extract-numbers-from-string-and-store-them-in-array-javascript
                    var dollar = price_str.match(/\d+/g)[0];
                    var shekel = price_str.match(/\d+/g)[1]
                    var euro = price_str.match(/\d+/g)[2]

                    var dollar_num_maam = parseInt(dollar)*1.17;
                    sum_dollar_maam += dollar_num_maam;
                    var shekel_num_maam = parseInt(shekel)*1.17;
                    sum_shekel_maam += shekel_num_maam;
                    var euro_num_maam = parseInt(euro)*1.17;
                    sum_euro_maam += euro_num_maam;
//                    console.log($(this).attr('id'))
                }
        }
    });
    $("#maam_client").html('$'+sum_dollar_maam.toFixed(2)+'<br/>'+'₪'+sum_shekel_maam.toFixed(2)+'<br/>'+'€'+sum_euro_maam.toFixed(2));

    var sum_dollar_maam = 0;
    var sum_shekel_maam = 0;
    var sum_euro_maam = 0;
    $("#sum_list_provider td").each(function() {
        if ($(this).attr('id')=='hakol_provider' || $(this).attr('id')=='maam_provider'){}
        else{
                if ( $(this).is(':visible') ) {
                    var price_str = $(this).html();
                    // https://stackoverflow.com/questions/34609571/extract-numbers-from-string-and-store-them-in-array-javascript
                    var dollar = price_str.match(/\d+/g)[0];
                    var shekel = price_str.match(/\d+/g)[1]
                    var euro = price_str.match(/\d+/g)[2]

                    var dollar_num_maam = parseInt(dollar)*1.17;
                    sum_dollar_maam += dollar_num_maam;
                    var shekel_num_maam = parseInt(shekel)*1.17;
                    sum_shekel_maam += shekel_num_maam;
                    var euro_num_maam = parseInt(euro)*1.17;
                    sum_euro_maam += euro_num_maam;
//                    console.log($(this).attr('id'))
                }
        }
    });
    $("#maam_provider").html('$'+sum_dollar_maam.toFixed(2)+'<br/>'+'₪'+sum_shekel_maam.toFixed(2)+'<br/>'+'€'+sum_euro_maam.toFixed(2));
}

$(document).ready(function() {
    sum_sum_list()
});