import utils from "./utils"
import Route from "./route"
import logger from "./logger"
import LatLng from "./latlng"

export default class GidonisMap {

    constructor() {
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
            time: 180,
            priority: ["bar", "museum", "point_of_interest", "park"]
        }

        const rawGeoPoints = await utils.getGeoRoute(routeRequest)

        const geoRoute = new Route({rawPoints: rawGeoPoints, google})

        this.map = new google.maps.Map(
            document.getElementById("map"), {zoom: 4, center: new LatLng(routeRequest.origin.x, routeRequest.origin.y)})

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