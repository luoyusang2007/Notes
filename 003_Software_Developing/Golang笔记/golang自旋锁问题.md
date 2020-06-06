# 自旋锁/忙等待问题
https://golang.org/ref/mem

以下代码是不对的：
```go

var a string
var done bool

func setup() {
	a = "hello, world"
	done = true
}

func main() {
	go setup()
	for !done {
	}
	print(a)
}

```