import Point from "./point"
import LatLng from "./latlng"
import logger from "./logger"

export default class Route {

    constructor({rawPoints, google}) {

        const points = rawPoints.map((point) => (new Point(point)))

        const [start, end] = points.filter((point) => point.type === "point")
        const waypoints = points.filter((point) => point.type !== "point")

        this.points = points
        this.startPoint = new Point(start)
        this.endPoint = new Point(end)
        this.waypoints = waypoints

    }

}
