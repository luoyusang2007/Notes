
# Go List 命令
https://golang.org/doc/articles/go_command.html
- 要获得关于 `go list` 命令的详细帮助，可以使用 `go help list` 获得。
- `go list` 用于列出包，不加 `-json` 的话只显示包文件夹路径
  - 必须在有 `.go` 文件的文件夹下使用
  - 可以使用 `go list ./...` 列出当前文件夹和子孙文件夹下的包
- `go list -m` 用于列出模块而不是包。

# 模块和包结构
Golang的包和Python类似：一个文件夹一个包。而模块与Python不同。Golang的模块可以包含多个包，而Python模块只是一个文件。

- 一个文件夹下只能有一个package：一个文件夹下可以有多go文件，这些go文件必须有相同的package名，否则会报错。
- 子文件夹中的package名与当前文件夹相同的文件不会被搜索（不参与编译也不报错）。或者说，子文件夹中若有go文件，子文件夹属于新的包（子包也是新的包）。
- main包会被编译成可执行程序。除了main包外，其它包都是可以被引用的。这和Python不同。Python中任何 `.py` 文件都可以被执行。

- golang中，包所在的文件夹名可以和包名不同，但不推荐。只是在 `import` 时：
    ```go
    import(
        "package/dir/path1" // 表示import这个文件夹（path1）下的包，path1不一定是包名。使用时path1.xxx()不一定奏效。
        as_name "package/dir/path2" // 表示import这个文件夹（path2）下的包后，强制把包名替换成as_name来使用。
    )
    ```
- 文件夹中，`.go` 文件的文件名可以随便取。其中的变量/常量/函数都可以互相访问到。


## 在模块中时
如果当前文件所在文件夹或祖先文件夹中存在合法的 `go.mod` 文件，那么当前文件就在go模块中。此时：
- 如果当前文件夹和祖先文件夹中存在多个文件夹含有 `go.mod` 文件，那么当前文件夹位于最近的mod中。
- `import` 引用不相对于 `.go` 文件，而是模块（否则报错）
- `go list -m` 命令会返回当前文件夹的模块名

## 不在模块中也不在GOPATH中时
如果当前文件所在文件夹或祖先文件夹中不存在 `go.mod` 文件，那么当前文件不在go模块中。
- `import` 引用相对于 `.go` 文件，而不是模块
- `go list -m` 命令会报错

# 源文件的搜索
注意，在某一个文件夹中运行 `go build` ，子文件夹中package名相同的 `.go` 文件不会被搜索到。

# Golang Import
在没有别名时import语句中写的的是目录名，而import进来的东西却是包名。

# 别名、点和下划线import
- 别名import作用类似于Python的 `import XXX as XXX`
- 如果想在使用时省略包名，则可以 `.` 作为别名，类似Python中的 `from XXX import *`
- 如果只想执行包的 `init()` 函数，而不用这个包，则可以 `_` 作为别名。

# 导入一次
https://studygolang.com/articles/17073   
和Python一样，golang的包存在多次导入（如main导入了a和b，其中a又导入了b）时，每个包只会被导入一次。所以任何包中的变量只会被初始化一次。

# 单例模式（使用全局变量和锁）
https://www.cnblogs.com/daryl-blog/p/11369614.html


# 利用包的单例
https://www.cnblogs.com/soulsu/p/5491747.html


