# 有空间和无空间
- 如果在结构体周中定义数组，那么这个结构体的大小会随着这个数组变化
- 如果在结构体中定义切片，切片会占据固定的24字节。
- 结构体大小一定是 8 字节的整数倍。

# C 中的情况
在C中，数组和数组指头针非常相似。但是定义时有区别。当数组在结构体中的时候，数组会整个放在结构体中占据结构体空间，而数组头指针不会。

# 结论
无论在 C 还是 Golang 中， 数组都不是数组头的引用。其含义包含了争端的长度。而 golang 中的切片确实是引用。所以传参时候传**切片**就好，没必要传切片指针。

