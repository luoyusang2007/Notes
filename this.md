


# 自建存储服务方案
- sync box
- 
- serv-u
- freenas
- Seafile  
  国内开源，Docker部署

- dzzoffice
- cloudreve

其它 https://blog.csdn.net/enweitech/article/details/84934831

# 软路由系统
## WayOS/维盟
可以做PPPoE server

## PfSense


## OPNSense
一键配置端口回流



## 爱快


## LEDE/OpenWRT


## ROS

## PANABIT


## 碧海威 海蜘蛛



## 不死鸟/老毛子/潘多拉




# 华为防火墙如何设置端口回流/hairpin？
https://www.cnblogs.com/Yu-Qing/p/11984297.html


# HTTP代理如何代理UDP连接比如QQ？


# 如何UDP打洞？


# OpenVPN默认自带的虚拟网卡叫啥？
TAP

# Virt-Viewer Windows版装好了没有快捷方式

# A类地址是否可以使用C类子网掩码
在有类网络中，IP地址为192.168.250.44 mask不能是 255.255.248.0。因为这是一个C类网络，子网掩码只能是/24~/30。而掩码255.255.248.0（相当于/21）是不符合规定的。但是在无类网络中却是可以的。
有类网络将IP地址视为3部分：网络字段、地址末尾的主机部分、网络和主机部分之间的子网部分。对于无类网络，有类地址划分的网络部分和子网部分合并为一个单独部分，称为子网或前缀，而地址末端也是主机部分。

# ABCDE 类IP
ABC类IP是IPV4下的产物，IPV6的分类完全不同。ABC类直接决定了子网掩码的取值范围。

| 分类 | 地址范围                  | 私有地址范围                                       | 默认子网掩码  |
| ---- | ------------------------- | -------------------------------------------------- | ------------- |
| A    | 1.0.0.0-126.255.255.255   | 10.0.0.0-10.255.255.255（默认一个网络，最大126个） | 255.0.0.0     |
| B    | 128.0.0.0-191.255.255.255 | 172.16.0.0-172.31.255.255                          | 255.255.255.0 |
| C    | 192.0.0.0-223.255.255.255 |                                                    |               |
| D    | 224.0.0.0-239.255.255.255 |                                                    |               |
| E    | 240.0.0.0-255.255.255.255 |                                                    |               |

# 源NAT和目的NAT
源NAT指的是包经过路由器后，包的源地址信息被更改了。
目的NAT指的是包经过路由器之后，包的目的地址信息被更改了。

# Windows 指定网卡（按照目的地址路由或设置网卡顺序）
比如我通过虚拟网卡联入了VPN，想使用虚拟网内的网关，就需要指定数据走哪张网卡或者哪个网关。
不要出现同一网段的两张网卡。

## 配置网卡顺序
https://blog.csdn.net/a2009a11a29/article/details/77880549
控制面板，进入“更改适配器设置”（“网络连接”或者“查看网络连接”）点入后，按一下alt建（弹出菜单栏），按高级，再按高级设置，在第一个页面调整顺序。

## 更改路由表
使用Route命令可以更改Windows的路由表。可以给不同的网段指定网关。
https://wenku.baidu.com/view/1c91f431bb1aa8114431b90d6c85ec3a87c28bd3.html
https://blog.csdn.net/qq_33611327/article/details/78271289


# Windows的TAP/TUN虚拟网卡
https://www.updatestar.com/directdownload/tap-windows/2281292
https://www.wintun.net/

# Go 语言调用 TAP/TUN
https://godoc.org/github.com/songgao/water
https://github.com/ICKelin/article/issues/9


# Windows没有tun
https://stackoverflow.com/questions/12513580/using-tun-driver-in-windows
OpenVPN的TAP-Windows只是二层设备。

# 环境变量设置语法

| 平台       | 当前堆栈（脚本）有效       | 调用脚本不新建堆栈 | 进程有效     | 永久设置                              |
| ---------- | -------------------------- | ------------------ | ------------ | ------------------------------------- |
| CMD        | set 配合SETLOCAL和ENDLOCAL |                    | set a=b      |                                       |
| SHELL      | a="b"                      | 加.（点）          | export a="b" |                                       |
| Powershell |                            | 加.（点）          | $env:a="b"   | [environment]::SetEnvironmentvariable |




# UDP连接
UDP本身是无连接的。
在Go语言中的实现请看
https://studygolang.com/articles/3345

可见，虽然 golang 试图 像 TCP 那样处理 UDP， 但是**并没有 listen-accept 过程**。

# TCP/UDP端口复用
TCP和UDP可以占用同一个端口.
在Golang中，一次 ListenUDP + 一次 DialUDP 使用同一个端口不会报错。
两次Listen在用一个端口或者两次Dial在同一个端口就会报错：
`Only one usage of each socket address (protocol/network address/port) is normally permitted`

# 命令行GUI/字符GUI/伪GUI
ncurses

go语言：https://github.com/gdamore/tcell

# Golang全局变量问题



# Golang点号和引用问题


# Golang 代理
https://github.com/goproxy/goproxy.cn/blob/master/README.zh-CN.md

# Golang Language Server For VSCode
## 进入Go扩展设置
按下`Ctrl+Shift+P`，输入`user settings`进入用户设置
找到Go扩展的设置
## 启动LanguageServer
找到`Use Language Server`
勾上后按照提示安装 gopls


# Bitvise 使用代理连接
第一页蓝色小字。ProxySetting

# Bitvise 代理到被连接的主机


