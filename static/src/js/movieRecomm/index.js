angular.module('movieRecommApp', [])
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    })
    .config(function ($httpProvider) {
    })
;
require('./controllers');
