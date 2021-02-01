# 结构
- 由 supernode 和 edge 组成，版本必须对应
- supernode 不参与组网。无需指定社区、密码等
- 注意，V1 版本必须要密码
# 安卓客户端
- 安卓客户端： hin2n
- ios 没有客户端

# docker 安装 supernode
- https://github.com/ntop/n2n 推荐的 supernode docker 是 https://hub.docker.com/r/supermock/supernode/ 
  - 其版本是 V1
  - 默认端口 7654

# Linux APT 安装 Edge
命令： `sudo apt install n2n` 注意 apt 安装（安装之后会有 edge 和 supernode）的也是 v1 。此时已经装好了虚拟网卡，且可以单独运行 edge 和 supernode。 

# MTU 设置
MTU 设置过大可能导致包过大，大包会在链路中被丢弃。所以设置为1300左右比较合适。n2n 默认 1400 一般物理网卡 MTU 一般为 1500 。

## 设置服务配置文件
编辑 `/etc/default/n2n` 按照注释编辑即可。

默认的文件不包含 MTU 选项，需要自己添加：
- `/etc/init.d/n2n` 在 do_start 函数中：
  - 第二个 `start-stop-daemon` 处， `-l` 之后添加 `-s $N2N_MASK -M $N2N_MTU`
- `/etc/default/n2n` 添加：
  - N2N_MASK="255.255.0.0"
  - N2N_MTU="1300"
- 更新： `systemctl daemon-reload`

## 启动 edge 服务
```shell
sudo service n2n start
```

# 自己设置 linux edge V1 自启动

以树莓派 raspbian 为例，apt 安装 n2n 之后，可以使用 service 和 init.d 配置服务开机启动（在用户登录前启动） 
编辑 `/etc/init.d/n2n1_hwcloud.sh`
```shell
#!/bin/bash
### BEGIN INIT INFO
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Description:       User Service of N2N V1 Edge Node
### END INIT INFO

N2N1_V_ADDR=10.0.1.1
N2N1_V_NETMASK=255.255.0.0
N2N1_COMM_NAME=lysnet
N2N1_PASS=88100143
N2N1_SNONE_ADDR=114.116.252.141
N2N1_SNODE_PORT=7654
N2N1_LOG_FILE=/log/n2n1_u_service.log

edge -a $N2N1_V_ADDR -s $N2N1_V_NETMASK -c $N2N1_COMM_NAME -k $N2N1_PASS -l $N2N1_SNONE_ADDR:$N2N1_SNODE_PORT > $N2N1_LOG_FILE
```

# 文档
- https://www.zhuguodong.com/?id=398
- http://www.lucktu.com/archives/749.html
- http://www.lucktu.com/archives/767.html
- http://www.lucktu.com/archives/768.html



