
# 基础
chan 要用make创建，否则会产生空channel（nil-channel）。

# 只读、只写
一般情况下只在定义形参时候说明只读、只写。

# Select 配合的无阻塞通道读取

https://www.jianshu.com/p/3b24e909905f
select 不是 switch，但是它也是golang中的一个关键字，可以实现Channel是否可读的检测。https://golang.org/ref/spec#Select_statements
``` go
select { //不停的在这里检测
    case <-chanl : //检测有没有数据可以读
    //如果chanl成功读取到数据，则进行该case处理语句
    case chan2 <- 1 : //检测有没有可以写
    //如果成功向chan2写入数据，则进行该case处理语句

    //假如没有default，那么在以上两个条件都不成立的情况下，就会在此阻塞//一般default会不写在里面，select中的default子句总是可运行的，因为会很消耗CPU资源
    default:
    //如果以上都没有符合条件，那么则进行default处理流程
}

```
关于break：
https://golang.org/ref/spec#Break_statements



# Channel转换为IO





# 传参时使用channel


