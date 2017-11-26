var todoapp = window.angular.module("todoapp",[]);

todoapp.controller("todolistcontroller",['$scope', function($scope) {
	$scope.text = '';

	$scope.todolist = [{
		text: 'hello world',
		done: false
	},{
		text: "I use Python",
		done: false
	}];

	$scope.add = function() {
		var text = $scope.text.trim();
		if(text){
			$scope.todolist.push({
				text: text,
				done: false
			});

			$scope.text = '';
		}
	};

	$scope.delete = function(){
		var index = $scope.todolist.indexOf(todo);
		$scope.todolist.splice(index, 1);
	};

	$scope.doneCount = function(){
		var temp = $scope.todolist.filter(function(item){
			return item.done;
		})

		return temp.length;
	};

}]);