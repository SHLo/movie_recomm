angular.module('MovieRecommApp', ['ui.bootstrap', 'uiSwitch'])
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    })
    .config(function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = "csrftoken";
        $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
        $httpProvider.defaults.headers.post["Content-Type"] = "application/json;charset=UTF-8";
    })
;
require('./controllers');
