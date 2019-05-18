import "babel-polyfill"

function loadGoogleMapsScript() {
    // eslint-disable-next-line no-undef
    const GOOGLE_MAPS_API_KEY = process.env.GOOGLE_MAPS_API_KEY

    if(!GOOGLE_MAPS_API_KEY) {
        throw new Error("Specify GOOGLE_MAPS_API_KEY in .env")
    }

    const script = document.createElement("script")
    script.type = "text/javascript"
    script.async = true
    script.src = `https://maps.googleapis.com/maps/api/js?key=${GOOGLE_MAPS_API_KEY}&callback=initMap`

    document.body.appendChild(script)
}

window.initMap = () => {
    const {google} = window

    // The location of Uluru
    var uluru = {lat: -25.344, lng: 131.036}

    // The map, centered at Uluru
    new google.maps.Map(
        document.getElementById("map"), {zoom: 4, center: uluru})
}

loadGoogleMapsScript()
