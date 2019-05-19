import utils from "./utils"
import Route from "./route"
import logger from "./logger"
import LatLng from "./latlng"
import Marker from "./marker"

export default class GidonisMap {

    constructor() {
        this.init = this.init.bind(this)
        this.drawRoute = this.drawRoute.bind(this)
    }

    async init() {
        const google = await this.loadGoogleMaps()

        this.directionsService = new google.maps.DirectionsService()
        this.directionsDisplay = new google.maps.DirectionsRenderer()

        var routeRequest = {
            origin: {
                x: 55.023013,
                y: 82.922431
            },
            destination: {
                x: 55.044237,
                y: 82.916694
            },
            time: 180,
            priority: ["bar", "museum", "point_of_interest", "park"]
        }

        const rawGeoPoints = await utils.getGeoRoute(routeRequest)

        const geoRoute = new Route({rawPoints: rawGeoPoints, google})

        this.map = new google.maps.Map(document.getElementById("map"), {zoom: 4, center: new LatLng(routeRequest.origin.x, routeRequest.origin.y)})
        
        createMarker.onclick = () => {
            this.map.addListener('click',(event) => {
                var objSel = document.getElementById("type");
                fetch('http://90.189.168.29:13452/geo_types')
                    .then((res) => {
                        return res.json();
                    })
                    .then((val) => {
                        var i = 0;
                        val.data.forEach((el) => {
                            objSel.options[i] = new Option(el, el);
                            i++;
                       })
                    })
                const geodata = [event.latLng.lat(), event.latLng.lng()];
                document.getElementsByClassName('popup')[0].style.display = "block";
                submitMarker.onclick = () => {
                    Marker.addMarker(geodata[0], geodata[1], document.getElementById('type').value, document.getElementById('name').value, document.getElementById('about').value, document.getElementById('date').value+" "+document.getElementById('time').value, document.getElementById('timeLenght').value, document.getElementById('timeNoLimit').checked )
                    document.getElementsByClassName('popup')[0].style.display = "none";
                    var ur = {lat: geodata[0], lng: geodata[1]};
                    var marker =  new google.maps.Marker({
                        title: document.getElementById('name').value,
                        position: ur, 
                        label: '',
                        map: this.map,
                    });
                }
                
            })
        }

        closeMarker.onclick = () => {
            Marker.closePopup();
        }

        firstDot.onclick = () => {
            this.map.addListener('click',(event) => {
                const geodata = [event.latLng.lat(), event.latLng.lng()];
                
                new google.maps.Marker({
                        title: document.getElementById('name').value,
                        position: new LatLng(event.latLng.lat(), event.latLng.lng()), 
                        label: '',
                        map: this.map,
                    });
                routeRequest.origin.x = event.latLng.lat()
                routeRequest.origin.y = event.latLng.lng()
                document.getElementById('firstDot').style.background = 'green'
        })
    }
        

        secondDot.onclick = () => {
            this.map.addListener('click',(event) => {
                const geodata = [event.latLng.lat(), event.latLng.lng()];
                new google.maps.Marker({
                        title: document.getElementById('name').value,
                        position: new LatLng(event.latLng.lat(), event.latLng.lng()), 
                        label: '',
                        map: this.map,
                    });
                routeRequest.destination.x = event.latLng.lat()
                routeRequest.destination.y = event.latLng.lng()
                document.getElementById('secondDot').style.background = 'green'
                
        })
    }
        
        await this.drawRoute(geoRoute)
    }

    async drawRoute(route) {
        return new Promise((resolve, reject) => {
            if (!route.points.length) {
                throw new Error("NoPointsError")
            }

            const request = {
                origin: new LatLng(route.startPoint.x, route.startPoint.y),
                destination: new LatLng(route.endPoint.x, route.endPoint.y),
                waypoints: route.waypoints.map((waypoint) => ({location: new LatLng(waypoint.x, waypoint.y)})),
                travelMode: "WALKING"
            }

            this.directionsService.route(request, async (response, status) => {
                if (status === "OK") {
                    this.directionsDisplay.setDirections(response)
                    this.directionsDisplay.setMap(this.map)
                    this.directionsDisplay.setPanel(document.getElementById("directionsPanel"))

                    resolve()
                } else {
                    logger.error(status)
                    reject("DirectionServiceUnknownError")
                }
            })
        })
    }

    async loadGoogleMaps() {
        return new Promise((resolve, reject) => {
            // eslint-disable-next-line no-undef
            const GOOGLE_MAPS_API_KEY = process.env.GOOGLE_MAPS_API_KEY

            if (!GOOGLE_MAPS_API_KEY) {
                throw new Error("Specify GOOGLE_MAPS_API_KEY in .env")
            }

            let loaded = false

            window.initApp = () => {
                loaded = true
                resolve(window.google)
            }

            const script = document.createElement("script")
            script.type = "text/javascript"
            script.async = true
            script.src = `https://maps.googleapis.com/maps/api/js?key=${GOOGLE_MAPS_API_KEY}&callback=initApp`

            document.body.appendChild(script)


            setTimeout(5000, () => {
                if (!loaded) {
                    reject("GoogleMapsLoadTimeoutError")
                }
            })
        })
    }


}