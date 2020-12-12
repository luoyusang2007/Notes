# 传参是传值还是传引用？
又叫值传递/引用传递。
golang 中，字符串和数组默认是传值，但是 slice、map、interface、channel 传引用。

# 方法中传值和传引用
如果要改表对象，方法定义必须定义在对象指针上。
```go
package main

import (
	"fmt"
)
type myint int  // 必须重新定义类型，你无法给int类型加方法。
func (self * myint)plusone(){
	*self=*self+1
}

func main() {
	var i myint = 5
	i.plusone()
	fmt.Println(i)
}

// 输出 6
```

以下代码不能改变：
```go
package main

import (
	"fmt"
)
type myint int  // 必须重新定义类型，你无法给int类型加方法。
func (self myint)plusone(){
	self=self+1
}

func main() {
	var i myint = 5
	i.plusone()
	fmt.Println(i)
}

// 输出 5
```



对结构体的属性也是一样：

```go
package main

import (
	"fmt"
)
type man struct{
	age int
}
func (self man)grow(){
	self.age=self.age+1
}

func main() {
	i := man{
		age:5,
	}
	i.grow()
	fmt.Println(i)
}
// 输出{5}
```

如果使用指针定义方法，就输出6：
```go
func (self * man)grow(){
	self.age=self.age+1
}
```


# 返回指针？

# 方法指针？

# 语法糖？



