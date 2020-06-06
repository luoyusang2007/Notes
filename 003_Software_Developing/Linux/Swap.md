# Linux 的内存结构

```
# free -m
```
- 第一行 `Mem` 是物理内存统计，shared、buffers和cached都包含在used中
- 第二行 `-/+buffers/cache` 还是对第一行的细分统计
- 第三行 `Swap` 是虚拟内存
显示出来的参数如下：
- total 内存总数
- used 已经使用的内存数（我的程序使用内存数量+系统缓存使用的内数量）
- free 空闲的物理内存数（是真正的空闲，未被任何程序占用）
- shared 多个进程共享的内存总额
- buffers 磁盘缓存（Buffer Cache）的大小（可提高系统I/O调用的性能）
- cached  磁盘缓存（Page Cache）的大小（可提高系统I/O调用的性能）
- -buffers/cache 表示已被我们的程序使用的内存数，计算方法：used - buffers - cached
- +buffers/cache 表示还可已被我使用的内存数，计算方法：free + buffers + cached

其中：
- 内存总量total=used + free
  - used 包含真正进程用的和buffers、cached
- 可用内存总量=free + buffers + cached，也就是显示的+buffers/cache
- buffers是用来给块设备做的缓冲大小、buffers是用来存储目录里面有什么内容，权限等等
- cached用来给文件做缓冲，用来记忆我们打开的文件.


# Buffers 和 Cached 区别


# Swap
https://www.jianshu.com/p/36cbc654c7ea


在Linux上，可以使用 `swapon -s` 命令查看当前系统上正在使用的交换空间信息。
`/proc/sys/vm/swappiness` 这个文件，默认值是60，可以的取值范围是0-100，用来定义内核使用swap的积极程度。值越高，内核就会越积极的使用swap，如果这个值为0，那么内存在free和file-backed使用的页面总量小于高水位标记（high water mark）之前，不会发生交换。

## 