实验室的是USG2130BSR
# 手册
https://wenku.baidu.com/view/fd2d6ddf1611cc7931b765ce05087632311274b0.html
https://support.huawei.com/enterprise/zh/security/usg2100-pid-8577356 根据配置指南进行配置

# 华为命令行的三种视图
- 登录进入用户视图，提示位尖括号
- 在用户视图输入 `system-view` 进入系统视图
- 在系统视图输入 `aaa` 进入AAA视图

# 华为命令行帮助
- 直接打`？`
- 若要看参数，键盘键入 命令 空格 `?`

# 默认静态路由
默认0.0.0.0路由是WAN口DHCP客户端拿到的网关地址。是自动生成的。

# DHCP IP MAC 绑定
- 不要在防火墙设置，那是不让过
- 网络-DHCP服务器-服务-右边点击配置-高级-静态IP绑定
- 若提示已经存在于租约中：`reset dhcp server ip-in-use ip XXX.XXX.XXX.XXX`


# 查看 ARP 表
在防火墙-安全防护-IP MAC绑定 页面的下边 ARP列表

# 查看 WAN 口信息
以Ethernet0/0/0为例
- `display interface Ethernet0/0/0`
- 但是该命令看不到 WAN 口 通过 DHCP 拿到的 DNS、网关等。
- 子网掩码看IP后的斜杠数字。

# 查看路由表
- `display fib`
- WEB 路由-监控-路由表



# 问题：无法访问校园网，但是可以访问外网
只有 aaa.ncu.edu.cn 可以访问，
其它ncu.edu.cn均不可访问。
- 用替代路由器克隆其wan地址之后 renew dhcp wan 口 ip （重新获取）解决。


