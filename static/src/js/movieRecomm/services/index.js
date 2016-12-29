angular.module('MovieRecommApp')
    .service('restSrv', ['$http', function ($http) {
        this.listMovies = function (count) {
            return $http.get('/list/',
                {params: {count: count}}
            )
                .error(function (resp) {
                    console.error(resp);
                })
            ;
        }
    }])
;
