import "babel-polyfill"
import GidonisMap from "./lib/map"

const map = new GidonisMap()

map
    .init(() => console.log("Gidonis map loaded"))
    .catch(console.error)



function addMarker(location, title) {
            var marker = new google.maps.Marker({
              position: new google.maps.LatLng(location.x, location.y),
              map: map,
              title: title
            });
            markers.push(marker);
          }

function setMapOnAll(map) {
            for (var i = 0; i < markers.length; i++) {
              markers[i].setMap(map);
            }
          }

function clearMarkers() {
            setMapOnAll(null);
          }
    

var getJSON = function(url, callback) {

    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    
    xhr.onload = function() {
    
        var status = xhr.status;
        
        if (status == 200) {
            callback(xhr);
        } else {
            callback(status);
        }
    };
    
    xhr.send()
}

var getObjectByValue = function (array, key, value) {
    return array.filter(function (object) {
        return object[key] === value;
    });
};

var markers = [];

function loadMarkers(map, google, types){
getJSON("http://90.189.168.29:13452/all_touch", function(places) {
        localStorage.setItem('places', JSON.stringify(places.response));
        for(var i = 0; i < places.response.length; i++){
            if(types.indexOf(places.response[i].type) > -1 || (types.length == 0)){
                var latLng = new google.maps.LatLng(places.response[i].x, places.response[i].y); 
                // Creating a marker and putting it on the map
                var marker = new google.maps.Marker({
                    position: latLng,
                    map: map,
                    title: places.response[i].name
                })
                markers.push(marker);
                marker.addListener('click', function(event) {
                    var res = getObjectByValue(JSON.parse(localStorage.getItem('places')), "name", event.wa.srcElement.title );
                    document.getElementById("location_name").textContent = res[0].name
                    document.getElementById("location_desc").textContent = res[0].descript
                    document.getElementById("rating").textContent = res[0].rating
                    document.getElementById("reviews").textContent = res[0].time
                });
            }
        }
    })
}


function loadCategories()
{
    getJSON("http://90.189.168.29:13452/geo_types", function(categories) {
        localStorage.setItem('categories', JSON.stringify(categories.response.data));
        for(var i = 0; i < categories.response.data.length; i++){
            var cat = document.createElement("input");
            cat.setAttribute("type","checkbox");
            cat.setAttribute("checked", true);
            //cat.setAttribute("onClick", "changeCategory('" + categories.response.data[i] + "')");
            cat.addEventListener( "click" , function(event) {
                var places = JSON.parse(localStorage.getItem('places'))
                for (var i = 0; i < places.length; i++)
                {
                    if(places[i].type == event.target.id && event.target.checked == false)
                    {
                        //remove marker
                        //clearMarkers()
                        markers[markers.indexOf(places[i])].setMap(null);
                    }
                    else if (places[i].type == event.target.id && event.target.checked == true)
                    {
                        //add marker to map
                        addMarker(places[i])
                    }
                }
            })
            cat.setAttribute("id",categories.response.data[i]);
            cat.setAttribute("name",categories.response.data[i]);
            var labelCat = document.createElement("label");
            labelCat.setAttribute("for",categories.response.data[i]);
            labelCat.append(categories.response.data[i]);
            var checkboxDiv = document.createElement("div");         
            checkboxDiv.appendChild(cat);                              
            checkboxDiv.appendChild(labelCat);                              
            document.getElementById("categories").appendChild(checkboxDiv);
            }
        
    })
}

loadCategories()

