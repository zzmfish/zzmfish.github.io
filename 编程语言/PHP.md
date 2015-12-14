# PHP

## 安装
```bash
./configure --prefix=$HOME/local \
    --with-apxs2=$HOME/local/bin/apxs \
    --with-mysql \
    --with-pdo-mysql \
    --with-openssl \
    --enable-zip \
    --enable-mbstring
make -j5
make install
```

## 语言
### 数据类型
```php
<?php
//数组/字典
$array = array(
    "foo" => "bar",
    "bar" => "foo",
    100   => -100,
    -100  => 100,
);
?>
```

## 工具
### [Composer](https://getcomposer.org/)
```bash
# 安装
curl -sS https://getcomposer.org/installer | php -- --install-dir=$HOME/local/bin
```

## 框架

### [Laravel](http://laravel.com/)
#### 安装和配置
```bash
# 安装
php composer.phar global require "laravel/installer"
# 环境变量
export PATH=$HOME/.composer/vendor/bin:$PATH
# 创建项目
laravel new hello_laraval
# 创建数据库表
php artisan make:migration create_tasks_table --create=tasks
# 创建模型
php artisan make:model Task
# 数据库迁移
php artisan migrate
# 运行
cd public
php -S 127.0.0.1:9090 -t .
```
### 文件
|文件     |说明
|-----    |---------
app/Http/routes.php | 路由
database/migrations/ | 数据库迁移文件

### 概念
#### 路由
```php
<?php
Route::get('/hello1', function () {
    return view('hello');
});
Route::get('/hello2', 'HelloController@hello');
?>
```
#### 模板
#### 中间件
#### 控制器

## 参考
* [PHP5.5新特性介绍](http://wulijun.github.io/2013/07/17/whats-new-in-php-5-5.html)
* [PHP5.6新特性介绍](http://wulijun.github.io/2014/01/25/whats-new-in-php-5-6.html)
* [PHP6与PHP5相比的那些变化与改进？](http://www.weste.net/2013/5-28/91772.html)
* [PHP手册 -> 语言参考 -> 支持的协议和封装协议](http://php.net/manual/zh/wrappers.php.php)
* [PHP 过滤器](http://www.runoob.com/php/php-filter.html)
* [PHP框架Laravel还是Codeigniter？](http://www.zhihu.com/question/21617669)
* [最好的 PHP 框架是什么？为什么？](http://www.zhihu.com/question/19558755)
* [Laravel学院](http://laravelacademy.org/)
* [Unix 系统下的 Apache 2.x](http://php.net/manual/zh/install.unix.apache2.php)