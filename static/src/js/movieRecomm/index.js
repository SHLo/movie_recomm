angular.module('MovieRecommApp', ['ui.bootstrap'])
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    })
    .config(function ($httpProvider) {
    })
;
require('./controllers');
