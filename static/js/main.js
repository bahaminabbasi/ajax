$('#select_categories').change(function() {
    var value = $('#select_categories').val();
    $.ajax({
        url: '/category/levelzero_selected/',
        method: 'POST',
        data: {
            'selected_category': value,
        },
        success: function(data){
            $('#levelone_placeholder').empty()
            $('#leveltwo_placeholder').empty()
            $('#levelone_placeholder').append(
                `<option id='levelone_placeholder'">-------------</option>`
            )
            $('#leveltwo_placeholder').append(
                `<option id='levelone_placeholder'">-------------</option>`
            )
                for (i = 0; i < data['result'].length; i++) {
                    $('#levelone_placeholder').append(
                        `<option id='levelone_placeholder' value="` + data['result'][i] + `">` + data['result'][i] + `</option>`
                    );

                }
        }

    });
});

$('#levelone_placeholder').change(function() {
    var value = $('#levelone_placeholder').val();
    $.ajax({
        url: '/category/levelone_selected/',
        method: 'POST',
        data: {
            'selected_category_one': value,
        },
        success: function(data){
            $('#leveltwo_placeholder').empty()
            $('#leveltwo_placeholder').append(
                `<option id='levelone_placeholder'">-------------</option>`
            )
                for (i = 0; i < data['result'].length; i++) {
                    $('#leveltwo_placeholder').append(
                        `<option id='leveltwo_placeholder' value="` + data['result'][i] + `">` + data['result'][i] + `</option>`
                    );

                }
        }

    });
});