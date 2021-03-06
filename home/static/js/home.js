var map;
var markers = [];
var latlng;

/**
#       This code is written by
#        a) Austin Goh 
#        b) KC Koay
#        c) Khalil Gibran Von
#        d) Loh Yoong Keat
#        e) Azim
#       From University of Malaya
#       * WAES3306 Information System Intelligence
**/
$(document).ready(function(){
        initMap();
         $(".various").fancybox({
                                maxWidth    : 800,
                                maxHeight   : 600,
                                fitToView   : false,
                                width       : '70%',
                                height      : '70%',
                                autoSize    : false,
                                closeClick  : false,
                                openEffect  : 'none',
                                closeEffect : 'none'
                                });
        $('#btnConfirm').click(function() {
            var group = document.getElementById('group').value;
            var duration = document.getElementById('duration').value;
            var season = document.getElementById('season').value;
            var holidayType = document.getElementById('holidayType').value;
            var transportation = document.getElementById('transportation').value;

            if(season==""){
                alert("Please fill in the season you want to go for travelling~");
               document.getElementById('fl1').style.display = 'none';
            } else if(group==""){
                alert("Please fill in your group size");
                document.getElementById('fl1').style.display = 'none';
            } else if (holidayType==""){
                alert("Please fill in holiday type");
                document.getElementById('fl1').style.display = 'none';
            }  else if (transportation==""){
                alert("Please fill in transportation mode");
                document.getElementById('fl1').style.display = 'none';
            } else if (duration==""){
                alert("Please fill in the duration");
                document.getElementById('fl1').style.display = 'none';
            } else if(latlng==null) {
                alert("Please select a place which you are interested!")
                document.getElementById('fl1').style.display = 'none';
            } else {
                var postdata = {
                    'longitude': latlng.lng(),
                    'latitude': latlng.lat(),
                    'duration': duration,
                    'season': season,
                    'holidayType': holidayType,
                    'transportation': transportation,
                    'group': group
                    };
                $.ajax({
                    type: "POST",
                    contentType: "application/json; charset=utf-8",
                    url: "post_data/",
                    data: JSON.stringify(postdata),
                    beforeSend: function(xhr, settings) {
                     console.log("Before Send");
                     $.ajaxSettings.beforeSend(xhr, settings);
                    },
                    success: function(result) {
                        console.log(result.transportation);
                         document.getElementById('fl1').style.display = 'block';
                         document.getElementById('region_result').innerHTML = result.region;
                         document.getElementById('price_result').innerHTML = "Price : "+result.price;   
                         document.getElementById('holiday_type_result').innerHTML = "Holiday Type : "+result.holidayType;
                         document.getElementById('transportation_result').innerHTML = "Transportation : "+result.transportation;
                         document.getElementById('duration_result').innerHTML = "Duration in days : "+result.duration;   
                         document.getElementById('season_result').innerHTML = "Season : "+result.season;
                         document.getElementById('hotel_result').innerHTML = "Hotel : "+result.hotel;  
                         document.getElementById('group_result').innerHTML = "Number of Persons : "+result.numberOfPersons;      
                    },
                    
                });
                }
            });
        });     

function changeSeasonValue(season){
    document.getElementById('season').innerHTML=season;
    document.getElementById('season').value=season;
    document.getElementById('season').style.color = "#5F9EA0";
}

function changeTransportation(transportation){
    document.getElementById('transportation').innerHTML = transportation;
    document.getElementById('transportation').value = transportation;
    document.getElementById('transportation').style.color = "#5F9EA0";
}

function changeHolidayType(holidayType){
    document.getElementById('holidayType').innerHTML = holidayType;
    document.getElementById('holidayType').value = holidayType;
    document.getElementById('holidayType').style.color = "#5F9EA0";
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function initMap() {
        // Create a map object and specify the DOM element for display.
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 26.2540493, lng: 29.2675469},
          scrollwheel: true,
          zoom: 7
        });
        google.maps.event.addListener(map,'click', function(event) {
            setMapOnAll(null);
            addMarker(event.latLng);
            latlng = event.latLng;
            
        });
      }



$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

function addMarker(location) {
    var marker = new google.maps.Marker({
      position: location,
      map: map,
      animation:google.maps.Animation.DROP
    });
    markers.push(marker);
}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
      markers[i].setMap(map);
    }
}
