
# 常用命令

- ls cd
- pwd
- mkdir rm mv cp cat rmdir
- nl
- more less head tail
- which whereis locate
- find xargs
- wc
- nc
- grep
- 正则
- cut
- paste
- tr
- sort diff patch
- df
- du
- time
- whoami whois
- mount
- adduser=useradd


  ```
  adduser [-c comment] [-d home_dir] [-e expire_date] [-f inactive_time] [-g initial_group] [-G group[,...]] [-m [-k skeleton_dir] | -M] [-p passwd] [-s shell] [-u uid [ -o]] [-n] [-r] loginid
  ```
  删除：
  ```
  adduser -D [-g default_group] [-b default_home] [-f default_inactive] [-e default_expire_date] [-s default_shell]
  ```
- userdel
- xargs
- fdisk
- netstat
- ifconfig netstat route arp 等属于 `net-tools` 而 `net-tools` 已不再维护
  - CentOS 7 没有 `ifconfig` 命令
- ip ss 命令属于 `iproute2` 用于代替  `net-tools` 
- ps
- pgrep
- top htop
- pstree 以树状显示所有进程
- pkill killall kill skill
- free


# 变量
set env export


## nohop和screen

## cat more less
- 先进程度（用户友好）：less>more>cat 


# 消息管道/重定向
## 到文件
- `command > right.txt` 将stdout覆盖写到txt文件，stderr屏幕输出。这是覆写，若不存在自动新建（但是不会新建目标路径中的文件夹）
- `command >> right.txt` 若要追加，使用 `>>` 其它与覆写相同。
- `command 1> right.txt 2> err.txt` 1代表stdout，2代表stderr。
- `command [param] 1> out.txt 2>&1` out和err放一起覆写txt文件。
- `command [param] 1>> out.txt 2>&1` out和err放一起追加txt文件（注意没有 `2>>&1` 的语法）。
- `command [param] 1>>right.txt 2>wrong.txt` 正确的结果追加，错误的结果覆盖。
- `command [param] 1>>right.txt 2>/dev/null` 错误的丢弃

## 从文件
- `command [param] < in.txt` 从文件输入【期间文件改动？】

此外，一些命令可实现监听文件实时变化的功能，如 `tail -f`。

# 到进程（管道和过滤器）
https://www.it610.com/article/2575261.htm   
`|` 管道并不能处理上一个命令的错误输出信息。如果要在管道里处理错误信息：
- `command [param] 2>&1 | grep "fff"` ，out和err都进了管道。
- `command [param] 2>&1 1>out.txt | grep "XXX"` ，这样先把stderr定向到out，这样最初的out进文件，err进管道给别的进程。


# 快捷键
## 定位

## 删除
## 历史

# 案例

## 删除七天前的文件
https://blog.csdn.net/ak57193856/article/details/78251611   
在 `/logs` 目录中查找更改时间在7日以前的文件并删除它们：
```
$ find logs/ -type f -mtime +7 -exec rm -f {} \;
```
在 `/logs` 目录中查找更改时间在7日以内的文件并删除它们：
```
$ find logs/ -type f -mtime -7 -exec rm -f {} \;
```


## 测试磁盘速度
写入无缓存：
```shell
time dd if=/dev/zero bs=1024 count=1000000 of=/1Gb.file oflag=direct
```
写入有缓存：
```shell
time dd if=/dev/zero bs=1024 count=1000000 of=/1Gb.file
```
读取：
```shell
time dd if=/1Gb.file bs=64k |dd of=/dev/null
```

## 把进程列表输出到文件


## 在子文件夹中搜索文件



## 在文件中搜索文本
| grep

## 下载


## 服务管理
- daemon
- systemd
- nohup
从CentOS 7.x开始，CentOS开始使用systemd来代替daemon。命令上，systemctl命令代替service命令。  https://blog.csdn.net/u012834750/article/details/80501440   

