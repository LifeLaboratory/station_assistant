import utils from "./utils"
import Route from "./route"
import logger from "./logger"
import LatLng from "./latlng"

export default class GidonisMap {

    constructor() {

        /*
        *
        *
        *

    // The location of Uluru
    var first = {lat: 52.377002, lng: 4.889937}
    var second = {lat: 51.377002, lng: 4.889937}
    var third = {lat: 50.377002, lng: 4.889937}
    var fourth = {lat: 49.377002, lng: 4.889937}
    // The marker, positioned at Uluru

    // The map, centered at Uluru
    const map = new google.maps.Map(
        document.getElementById("map"), {zoom: 4, center: first})

    var firstMarker = new google.maps.Marker({position: first, map: map})
    var secondMarker = new google.maps.Marker({position: second, map: map})
    var thirdMarker = new google.maps.Marker({position: third, map: map})
    var fourthMarker = new google.maps.Marker({position: fourth, map: map})

    var directionsService = new google.maps.DirectionsService()
    var directionsDisplay = new google.maps.DirectionsRenderer()

    directionsDisplay.setMap(map)
    directionsDisplay.setPanel(document.getElementById("directionsPanel"))*/


        this.init = this.init.bind(this)
        this.drawRoute = this.drawRoute.bind(this)

    }

    async init() {
        const google = await this.loadGoogleMaps()

        this.directionsService = new google.maps.DirectionsService()
        this.directionsDisplay = new google.maps.DirectionsRenderer()

        const routeRequest = {
            origin: {
                x: 55.023013,
                y: 82.922431
            },
            destination: {
                x: 55.044237,
                y: 82.916694
            },
            time: 520,
            priority: ["bar", "museum", "point_of_interest", "park"]
        }

        const rawGeoPoints = await utils.getGeoRoute(routeRequest)

        const geoRoute = new Route({rawPoints: rawGeoPoints, google})

        this.map = new google.maps.Map(
            document.getElementById("map"), {zoom: 4, center: new LatLng(geoRoute.startPoint.x, geoRoute.startPoint.y)})

        await this.drawRoute(geoRoute)
    }


    async drawRoute(route) {
        return new Promise((resolve, reject) => {
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