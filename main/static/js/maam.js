//$(document).ready(function() {
//
//});

function sum_sum_list(){
//    console.log( 'sum sum list called!')
    var sum_dollar = 0;
    var sum_shekel = 0;
    var sum_euro = 0;
    // https://stackoverflow.com/questions/5767334/jquery-get-elements-without-display-none
    $('#sum_list td:not([style*="display: none"])').each(function() {
        if($(this).attr('id')=='hakol' ||$(this).attr('id')=='maam'){}
        else{
            if ( $(this).not(':hidden') ) {
                var price_str = $(this).html();
                // https://stackoverflow.com/questions/34609571/extract-numbers-from-string-and-store-them-in-array-javascript
                var dollar = price_str.match(/\d+/g)[0];
                var shekel = price_str.match(/\d+/g)[1]
                var euro = price_str.match(/\d+/g)[2]
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
    $("#hakol").html('$'+sum_dollar+'<br/>'+'₪'+sum_shekel+'<br/>'+'€'+sum_euro)
}

function maam(){
    var sum_dollar_maam = 0;
    var sum_shekel_maam = 0;
    var sum_euro_maam = 0;

    $("#sum_list td").each(function() {
        if ($(this).attr('id')=='hakol' || $(this).attr('id')=='maam'){}
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
    $("#maam").html('$'+sum_dollar_maam.toFixed(2)+'<br/>'+'₪'+sum_shekel_maam.toFixed(2)+'<br/>'+'€'+sum_euro_maam.toFixed(2));
}

$(document).ready(function() {
    sum_sum_list()
});