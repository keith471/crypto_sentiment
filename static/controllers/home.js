angular.module('Visualizer')
.controller('HomeController', function ($scope, Data) {
	$scope.options = {
		chart: {
			type: 'multiChart',
			height: 500,
			margin : {
				top: 30,
				right: 60,
				bottom: 50,
				left: 70
			},
			duration: 500,
			xAxis: {
				axisLabel: 'Date',
				tickFormat: function(d){
					return d3.time.format('%m-%d %H:%M')(new Date(d))
				},
				rotateLabels: 30
			},
			yAxis1: {
				tickFormat: function(d){
					return d;
				}
			},
			yAxis2: {
				tickFormat: function(d){
					return d;
				}
			}
		}
	};

	Data.getCoins().then((data) => {
		$scope.coinStr = data.map((coin) => coin.name).reduce((acc, val) => val);
	});

	$scope.data = [
		{
			key: 'Text Summary Sentiment',
			type: 'line',
			yAxis: 1
		},
		{
			key: 'Price in USD',
			type: 'line',
			yAxis: 2,
		}
	];

	Data.getTextSummariesForCoin('BTC').then((data) => {
		$scope.data[0].values = data.map((point) => {
			return {
				x: new Date(point.posted_at).getTime(),
				y: point.sentiment
			};
		});
		Data.getPricesForCoin('BTC').then((data) => {
			$scope.data[1].values = data.map((point) => {
				return {
					x: new Date(point.created_at).getTime(),
					y: point.price
				};
			});
		});
	});
});
