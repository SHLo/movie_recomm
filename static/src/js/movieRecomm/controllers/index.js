require('../services');

angular.module('MovieRecommApp')
    .controller(
	'MainCtrl',
	[
	    '$scope',
	    '$http',
            '$interval',
	    '$uibModal',
	    'restSrv',
	    function ($scope, $http, $interval,  $uibModal, restSrv) {
                var stop;
		$scope.listSizes = [
		    20,
		    60,
		    100,
		]
		$scope.historyMode = false;
		$scope.auth = window.auth;
                $scope.currentCount = 20;

                $scope.setCurrentCount = function (cnt) {
                    $scope.currentCount = cnt;
                    listMovies();
                };

		$scope.openRatingModal = function (item) {
                    clearInterval();
		    console.log(item);
		    var modalInst = $uibModal.open(
			{
			    template: require('./modal.html'),
			    controller: 'ModalCtrl',
			    resolve: {
				item: function () {
				    return item;
				},
				historyMode: $scope.historyMode
			    }
			}
		    );
		    modalInst.result.then(function (rating) {
                        startInterval();
			if (typeof rating === 'undefined') return;
			$http.post(
			    '/rating/',
			    {item: item.id, rating: rating}
			)
			    .success(function (resp) {
				console.log('post suc:', resp);
                                listMovies($scope.currentCount);
			    })
			    .error(function (resp) {
				console.error('post err:', resp);
                            })
			;

			console.log(item.id, rating);
                    }, function () {
                        startInterval();
                    });
		};

		$scope.onModeChange = function () {
		    console.log('mode: ', $scope.historyMode);
                    if ($scope.historyMode) {
                        clearInterval();
                        listHistory();
                    }
                    else {
                        listMovies();
                        startInterval();
                    }
		};

		listMovies();
                startInterval();

		function listHistory () {
		    restSrv.listHistory()
			.success(function (resp) {
			    console.log(resp);
                            if (!$scope.historyMode) return;
			    $scope.items = resp.items;
			})
		    ;
		}

		function listMovies () {
		    restSrv.listMovies($scope.currentCount)
			.success(function (resp) {
			    console.log(resp);
                            if ($scope.historyMode) return;
			    $scope.items = resp.items;
			})
		    ;
		}

                function startInterval () {
                    if (angular.isDefined(stop)) return;
                    if ($scope.historyMode) return;

                    stop = $interval(
                        listMovies.bind(null, $scope.currentCount),
                        60000
                    );
                }

                function clearInterval () {
                    if (angular.isDefined(stop)) {
                        $interval.cancel(stop);
                        stop = undefined;
                    }
                }
	    }
	]
    )
    .controller('ModalCtrl',
	[
	    '$scope',
	    '$uibModalInstance',
	    'item',
	    'historyMode',
	    function ($scope, $uibModalInstance, item, historyMode) {
		$scope.item = item;
		$scope.auth = window.auth;
		$scope.historyMode = historyMode;
		$scope.rating = item.rating;
		$scope.ok = function () {
		    console.log('mode: ', historyMode);
		    console.log('rating: ', $scope.rating);
		    $uibModalInstance.close($scope.rating);
		};
		$scope.cancel = function () {
		    $uibModalInstance.dismiss('cancel');
		};
	    }
	]
    )
;
