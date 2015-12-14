## 概念

### Module
```js
//注册模块
var myModule = angular.module("module1", ['module2']);
```

### Service
* substitutable objects that are wired together using dependency injection (DI)
* organize and share code
* Lazily instantiated
* Singletons

### Controllers

```js
//简单controler
myModule.controller('test1',
    function($scope) {
        $scope.msg = 'hello';
    }
);

//使用其他services
myModule.controller('test2', ['$scope', '$http',
    function($scope, $http) {
        $scope.msg = 'hello';
        $http.get('/someUrl', config).then(successCallback, errorCallback);
    }
);
```

### Scopes
* root scope
* child scopes
* isolate scopes

### Templates

### Filters

## 参考
* [AngularJS中文网](http://www.apjs.net/)
* [带你走近AngularJS - 基本功能介绍](http://www.cnblogs.com/powertoolsteam/p/angularjs-introdection.html)
* [细说Angular ng-class](http://www.cnblogs.com/whitewolf/archive/2013/05/22/3092184.html)
* [AngularJS API Docs](https://docs.angularjs.org/api)
* [Tutorial 7 - Routing & Multiple Views](https://docs.angularjs.org/tutorial/step_07)
* [Guide to AngularJS Documentation](https://docs.angularjs.org/guide)
* [What are Scopes?](https://docs.angularjs.org/guide/scope)