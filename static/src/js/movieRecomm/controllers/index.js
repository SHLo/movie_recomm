require('../services');

angular.module('MovieRecommApp')
    .controller(
        'MainCtrl',
        [
            '$scope',
            '$http',
            '$uibModal',
            'restSrv',
            function ($scope, $http, $uibModal, restSrv) {
                console.log('scope: ', $scope);
                $scope.listMovies = function (count) {
                    restSrv.listMovies(count)
                    .success(function (resp) {
                        console.log(resp);
                        $scope.items = resp.items;
                    });
                }

                $scope.listSizes = [
                    20,
                    60,
                    100,
                ]


                $scope.openRatingModal = function (item) {
                    console.log(item);
                    var modalInst = $uibModal.open(
                        {
                            template: require('./modal.html'),
                            controller: 'ModalCtrl',
                            resolve: {
                                item: function () {
                                    return item;
                                }
                            },

                        }
                    );
                    modalInst.result.then(function (rating) {
                        console.log(item.id, rating);
                    });
                };

                $scope.listMovies(20);
            }
        ]
    )
    .controller('ModalCtrl',
        [
            '$scope',
            '$uibModalInstance',
            'item',
            function ($scope, $uibModalInstance, item) {
                $scope.item = item;
                $scope.ok = function () {
                    $uibModalInstance.close($scope.rating);
                };
                $scope.cancel = function () {
                    $uibModalInstance.dismiss('cancel');
                };
            }
        ]
    )
;
