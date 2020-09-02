const path = require("path");
const HWP = require("html-webpack-plugin");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: path.join(__dirname, `/src/index.js`),
    output: {
        filename: "build.js",
        path: path.join(__dirname, `/dist/js`)
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.html$/,
                use: [
                    {
                        loader: "html-loader"
                    }
                ]
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {
                            publicPath: '../'
                        }
                    },
                    'css-loader'
                ]
            }
        ]
    },
    devtool: 'source-map',
    plugins: [
        new HWP(
            {
                template: path.join(__dirname,`/src/index.html`)
            }
        ),
        new MiniCssExtractPlugin({
            filename: 'app.css',
            chunkFilename: '[id].css',
            ignoreOrder: false
        })
    ]
};
