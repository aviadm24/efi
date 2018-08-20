//$(document).ready(function() {
//
//});

function sum_sum_list(){
    var sum_dollar = 0;
    var sum_shekel = 0;
    var sum_euro = 0;

    $("#sum_list td").each(function() {
        if($(this).attr('id')=='hakol' ||$(this).attr('id')=='maam'){}
        else{
            if ( $(this).is(':visible') ) {
                var price_str = $(this).html();
                // https://stackoverflow.com/questions/34609571/extract-numbers-from-string-and-store-them-in-array-javascript
                var dollar = price_str.match(/\d+/g)[0];
                var shekel = price_str.match(/\d+/g)[1]
                var euro = price_str.match(/\d+/g)[2]

                var dollar_num = parseInt(dollar);
                sum_dollar += dollar_num;
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
                    console.log($(this).attr('id'))
                }
        }
    });
    $("#maam").html('$'+sum_dollar_maam+'<br/>'+'₪'+sum_shekel_maam+'<br/>'+'€'+sum_euro_maam)
}

$(document).ready(function() {
    sum_sum_list()
});