# 特殊语法
- 类型后置
- 大小写关系到作用域
- select
- 无需 break
- 没有"->"操作，"." 完成一切
- 不允许大括号换行
    ```go
    main () {
        fmt.Println("ABC")
    }

    ```

# 新建对象

- new
- make  make 只能用于 slice、map 和 channel 的初始化
- 直接定义 := 可以赋初值

```go
package main

import (
	"fmt"
)
type man struct{
	age int
}
func main() {
	man1 := new(man)    // 得到地址
	fmt.Printf("%v,%p\n", *man1, man1)
    
	man2 := &man{}      // 得到地址
	fmt.Printf("%v,%p\n", *man2, man2)

	man3 := man{}       // 得到结构体
	fmt.Printf("%v,%p\n", man3, &man3)

}

```

