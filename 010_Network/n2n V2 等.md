# 简介
二层 VPN。

# n2n 版本
edge -h 可见版本号
- V1 ： https://github.com/meyerd/n2n/tree/master/n2n_v1 （版本号是 v.1.x.x） 这是德国网友的微改版本，与官方 V1 兼容
- V2 ： https://github.com/ntop/n2n                      （版本号是 v.2.x.x） 官方.最后一个 V2 稳定版是 V2.8。
- V2s： https://github.com/meyerd/n2n/tree/master/n2n_v2 （版本号是 v.2.1.0） 德国网友的魔改版，与官方 V2 不兼容
- V3 ： ntop 官方版本，与之前版本都不兼容 注意 V2.9 及之后都属于 V3

# 资料
- http://www.lucktu.com/archives/767.html
- http://www.lucktu.com/archives/767.html/2
- http://www.lucktu.com/archives/751.html
- http://www.lucktu.com/archives/786.html
- http://www.lucktu.com/archives/783.html
- http://www.lucktu.com/archives/750.html 前世今生

# 官方
- https://github.com/ntop/n2n 
- https://www.ntop.org/

# 关于 meyerd
是一名德国网友。

# docker 镜像
- https://registry.hub.docker.com/r/supermock/supernode
  - 具有多个 Tag ，支持多种系统和架构
  - 支持 官方 V1 和 V2 版本
  - latest 标签似乎是 V1

# ntop 官方说明
官方(ntop) V2 相比 V1，更为安全，加密更结实，能够抵御带 DPI 功能的路由器探测拦截。


# 驱动依赖
所有版本都依赖 tap-windows 。有的 win 客户端已经自带。但是要管理虚拟网卡，还是需要 tap-windows。
- https://tap-windows.updatestar.com/
  - 注意安装后运行 bat 文件需要管理员权限。

# 监控端口/管理端口
http://www.lucktu.com/archives/767.html/2 最后有说。监控端口可以不开放。
- supernode 监控端口固定 5645 值得由 127.0.0.1 连接。
- edge 监控端口可以使用 -t 指定
netcat (nc) 本机 UDP 链接监控端口，按回车就可以显示信息。

