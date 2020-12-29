# 综述
Golang 没有抽象方法、虚函数等，很难实现“父类调用子类”。
Python 天生支持多态。因为类型无关。


```python
class Super(object):
    def name(self):
        return "Super"
    def WhoAmI(self):
        print("I'm {name}".format(name=self.name()))
class Sub(Super):
    def name(self):
        return "Sub"
if __name__ == "__main__":
    sub  = Sub()
    sub.WhoAmI()
# Get "I'm Sub"
```


```go
package main
import "fmt"
type Super struct{}
func (super *Super) name() string {
    return "Super"
}
func (super *Super) WhoAmI() {
    fmt.Printf("I'm %s.\n", super.name())
}
type Sub struct {
    Super
}
func (sub *Sub) name() string {
    return "Sub"
}
func main() {
    sub := &Sub{Super{}}
    sub.WhoAmI()
}
// Get "I'm Super"
```
# 结构体中加入 Interface 无法解决问题

结构体中加入 interface 只能用于强制赋值。

https://www.jianshu.com/p/a5bc8add7c6e

# 把 Interface 作为虚函数的集合




# 案例


```go

package main

type PersonIfce interface {
	//GetUp()
	GetDressed() //virtual
}

type Person struct {
}

// The un-implemented function
// func (self *Person) GetDressed() {
// 	panic("Virtual")
// }

// following no use
// func (self *Person) GetUp() {
// 	println("Brush teeth.")
// 	self.GetDressed()
// }

func GetUp(self PersonIfce) {
	println("Brush teeth.")
	self.GetDressed()
}

type Man struct {
	Person
}

func (self Man) GetDressed() {
	println("Wear nicktie.")
}

type Woman struct {
	Person
}

func (self Woman) GetDressed() {
	println("Wear skirt.")
}

func main() {
	man := Man{}
	//man.GetUp()
	GetUp(man)
}


```


or
```go

package main

type PersonIfce interface {
	//GetUp()
	GetDressed() //virtual
}

type Person struct {
}

// The un-implemented function
// func (self *Person) GetDressed() {
// 	panic("Virtual")
// }

// following no use
// func (self *Person) GetUp() {
// 	println("Brush teeth.")
// 	self.GetDressed()
// }

func GetUp(self PersonIfce) {
	println("Brush teeth.")
	self.GetDressed()
}

type Man struct {
	Person
}

func (self *Man) GetDressed() {
	println("Wear nicktie.")
}

type Woman struct {
	Person
}

func (self *Woman) GetDressed() {
	println("Wear skirt.")
}

func main() {
	man := Man{}
	//man.GetUp()
	GetUp(&man)
}


```


都输出
```
Brush teeth.
Wear nicktie.
```