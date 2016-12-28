angular.module('movieRecommApp')
    .controller(
        'ImgListCtrl',
        [
            '$scope',
            '$http',
            function ($scope, $http) {
                $http.get('/list/',
                    {params: {count: 20}}
                )
                    .success(function (resp) {
                        console.log(resp);
                        $scope.items = resp.items;
                    })
                    .finally(function (resp) {
                        console.log(resp);
                    })
                ;
            }
        ]
    )
;
