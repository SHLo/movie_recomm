var path = require('path');
var webpack = require('webpack');
var WebpackDevServer = require('webpack-dev-server');
var config = require('./webpack.config.dev');
var port = config.devServerPort;
//var WriteFilePlugin = require('write-file-webpack-plugin');
var OpenBrowserPlugin = require('open-browser-webpack-plugin');

config.plugins = config.plugins.concat([
  //  new OpenBrowserPlugin({
  //    url: 'http://localhost:' + config.devServerPort + '/dist/',
  //    browser: 'Google Chrome'
  //  }),
  //new WriteFilePlugin()
]);

new WebpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    hot: true,
    inline: true,
    historyApiFallback: true,
    //outputPath: path.join(__dirname, './dist')
})
.listen(port, '0.0.0.0', function (err, result) {
    if (err) {
        console.log(err)
    }

    console.log('Listening at 0.0.0.0:' + port)
});
