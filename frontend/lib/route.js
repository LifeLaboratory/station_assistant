import Point from "./point"

export default class Route {

    constructor({rawPoints, google}) {

        const points = rawPoints.map((point) => (new Point(point)))

        const [start, end] = points.filter((point) => point.type === "point")
        const waypoints = points.filter((point) => point.type !== "point")

        this.points = points

        if (points.length > 0) {
            this.startPoint = new Point(start)
            this.endPoint = new Point(end)
            this.waypoints = waypoints
        }

    }

}
