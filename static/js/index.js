$(document).ready(function() {
    $('#hospital-search').keyup(function() {
        var query = $(this).val();
        $.getJSON('/hospitals', {query: query}, function(data) {
            var hospitalsList = $('#hospitals-list');
            hospitalsList.empty();
            $.each(data, function(index, hospital) {
                hospitalsList.append('<li>' + hospital.name + '</li>');
            });
        });
    });

$('#service-search').keyup(function() {
    var query = $(this).val();
    $.getJSON('/services', {query: query}, function(data) {
        var servicesList = $('#services-list');
        servicesList.empty();
        $.each(data, function(index, service) {
            servicesList.append('<li>' + service.name + '</li>');
        });
    });
  });
});
const text = document.getElementById('typed-text').textContent;
document.getElementById('typed-text').textContent = '';

let index = 0;
const typingEffect = setInterval(() => {
  document.getElementById('typed-text').textContent += text[index];
  index++;

  if (index === text.length) {
    clearInterval(typingEffect);
  }
}, 100);


// $(document).ready(function() {
//     $('#hospital-search').on('input', function() {
//         var keyword = $(this).val().trim();
//         if (keyword !== '') {
//             $.ajax({
//                 type: 'POST',
//                 url: '/search',
//                 data: {'keyword': keyword},
//                 success: function(response) {
//                     var hospitals = response.hospitals;
//                     var hospitalsList = $('#hospitals-list');
//                     hospitalsList.empty();
//                     for (var i = 0; i < hospitals.length; i++) {
//                         var hospital = hospitals[i];
//                         hospitalsList.append('<li>' + hospital.name + ' - ' + hospital.address + '</li>');
//                     }
//                 }
//             });
//         } else {
//             $('#hospitals-list').empty();
//         }
//     });

//     $('#service-search').on('input', function() {
//         var keyword = $(this).val().trim();
//         if (keyword !== '') {
//             $.ajax({
//                 type: 'POST',
//                 url: '/search',
//                 data: {'keyword': keyword},
//                 success: function(response) {
//                     var services = response.services;
//                     var servicesList = $('#services-list');
//                     servicesList.empty();
//                     for (var i = 0; i < services.length; i++) {
//                         var service = services[i];
//                         servicesList.append('<li>' + service.name + '</li>');
//                     }
//                 }
//             });
//         } else {
//             $('#services-list').empty();
//         }
//     });
// });

