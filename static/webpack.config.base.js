var path = require('path');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var precss = require('precss');
var autoprefixer = require('autoprefixer');

module.exports = {
    context: path.resolve('src'),
    entry: {
        main: './js/main.js',
        vendor: [
            'font-awesome/css/font-awesome.css',
            'angular',
            'angular-translate',
            'angular-animate',
            'angular-cookies',
            'bootstrap-loader/extractstyles',
            'angular-ui-bootstrap',
            'angular-ui-switch/angular-ui-switch.min.css',
            'angular-ui-switch/angular-ui-switch.min.js',
        ]
    },
    output: {
        filename: '[name]-[hash].js',
        path: path.join(__dirname, 'dist')
    },
    plugins: [
        new ExtractTextPlugin('[name]-[hash].css'),
        new BundleTracker({filename: './webpack-stats.json'}),
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendor',
        }),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery",
        }),
    ],
    module: {
        loaders: [
            {
                test: /\.woff2?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: "url?limit=10000"
            },
            {
                test: /\.(ttf|eot|svg)(\?[\s\S]+)?$/,
                loader: 'file'
            },
            {
                test: /\.png$/,
                loader: "url-loader?mimetype=image/png"
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                loader: ExtractTextPlugin.extract('style-loader', 'css-loader?importLoaders=1!postcss-loader')
            },
            {
                test: /\.css$/,
                include: /node_modules/,
                loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
            },
            {
                test: /\.html$/,
                loader: 'raw-loader'
            },
            {
                test: /bootstrap-sass\/assets\/javascripts\//,
                loader: 'imports?jQuery=jquery'
            },
            {
                test: /\.js$/,
                loader: 'ng-annotate',
                exclude: /node_modules/
            },
        ]
    },
    postcss: function () {
        return [precss, autoprefixer];
    }
}
