/* eslint-disable no-undef */
const path = require("path")
const HtmlWebpackPlugin = require("html-webpack-plugin")
const Dotenv = require("dotenv-webpack")

module.exports = {
    entry: "./index.js",
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "bundle.js"
    },
    devtool: "source-map",
    plugins: [
        new HtmlWebpackPlugin({
            template: "./index.html"
        }),
        new Dotenv()
    ],
    devServer: {
        contentBase: path.join(__dirname, "dist"),
        port: 9000
    }
}