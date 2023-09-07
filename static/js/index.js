$(document).ready(function() {
    $('#hospital-search').keyup(function() {
        var query = $(this).val();
        $.getJSON('/search_hospitals', {query: query}, function(data) {
            var hospitalslist = $('#hospitals-list');
            hospitalslist.empty();
            $.each(data, function(index, hospital) {
                var hospitalLink = $('<a/>')
                    .attr('href', hospital.htmlLink)
                    .text(hospital.name)
                    .appendTo($('<li/>').appendTo(hospitalslist));
            });
        });
    });
// });

    $('#service-search').keyup(function() {
        var query = $(this).val();
        $.getJSON('/search_services', {query: query}, function(data) {
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

