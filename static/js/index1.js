$(document).ready(function() {
    // Search hospitals
    $('#hospital-search').on('input', function() {
        var query = $(this).val();

        $.ajax({
            url: '/hospitals',
            type: 'GET',
            data: { query: query },
            success: function(data) {
                var results = '';
                data.forEach(function(hospital) {
                    results += '<li>' + hospital.name + '</li>';
                });
                $('#hospitals-list').html(results);
            }
        });
    });

    // Search services
    $('#service-search').on('input', function() {
        var query = $(this).val();

        $.ajax({
            url: '/services',
            type: 'GET',
            data: { query: query },
            success: function(data) {
                var results = '';
                data.forEach(function(service) {
                    results += '<li>' + service.name + '</li>';
                });
                $('#services-list').html(results);
            }
        });
    });
});