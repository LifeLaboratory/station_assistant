import "babel-polyfill"
import GidonisMap from "./lib/map"

const map = new GidonisMap()

map
    .init(() => console.log("Gidonis map loaded"))
    .catch(console.error)