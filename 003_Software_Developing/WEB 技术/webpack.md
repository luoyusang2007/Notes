https://www.runoob.com/w3cnote/webpack-tutorial.html

# 功能
本身能把多个js文件打包成一个js文件。npm安装loader后，使用loader，可以打包其它文件（file-loader或者url-loader可以打包图片；css-loader和style-loader两个共同作用loader来打包CSS代码）
npm命令如果不加-g参数，就会安装在当前目录下，不能在命令行中使用。
```
npm install webpack -g
npm install css-loader style-loader

```
# 命令
打包
```
webpack source_with_requires.js out_bundle.js
```
