$(document).ready(function() {
    $('#hospital-search').keyup(function() {
        var query = $(this).val();
        $.getJSON('/hospitals', {query: query}, function(data) {
            var hospitalsList = $('#hospitals-list');
            hospitalsList.empty();
            $.each(data, function(index, hospital) {
                hospitalsList.append('<li><input type="checkbox" name="hospital" value="' + hospital.id + '"> ' + hospital.name + '</li>');
            });
        });
    });

$('#service-search').keyup(function() {
    var query = $(this).val();
    $.getJSON('/services', {query: query}, function(data) {
        var servicesList = $('#services-list');
        servicesList.empty();
        $.each(data, function(index, service) {
            servicesList.append('<li><input type="checkbox" name="service" value="' + service.id + '"> ' + service.name + '</li>');
        });
    });
  });
});
  