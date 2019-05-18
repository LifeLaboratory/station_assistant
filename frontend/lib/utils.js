import fetch from "cross-fetch"
import logger from "./logger"

export default class Utils {

    static async getGeoRoute({origin, destination, time , priority}) {

        const url = `http://90.189.168.29:13452/geo?origin_x=${origin.x}&origin_y=${origin.y}&destination_x=${destination.x}&destination_y=${destination.y}&time=${time}&priority=${JSON.stringify(priority)}`
        logger.info(url)
        const response = await fetch(url)

        switch (response.status) {
            case 200:
                return await response.json()
            default:
                logger.error(`API RESPONSE STATUS ${response.status}`)
                throw new Error("UnknownAPIResponseError")
        }
    }
}