# 概况
- 二进制下载 https://github.com/lucktu/n2n
- 竞争产品 zerotier； wireguard

# 结构
- 由 supernode 和 edge 组成，版本必须对应
- supernode 不参与组网。无需指定社区、密码等
- 注意，V1 版本必须要密码 (-k)

# 安卓客户端
- 安卓客户端： hin2n 支持 V1 V2 V2s
- ios 没有客户端

# docker 安装 supernode
在具有公网 IP 的云服务器安装


https://github.com/ntop/n2n 推荐的 supernode docker 是 https://hub.docker.com/r/supermock/supernode/ 
  - 其版本是 V1
  - 默认端口 7654

# Linux APT 安装 Edge（树莓派可用）
命令： `sudo apt install n2n` 注意 apt 安装（安装之后会有 edge 和 supernode）的也是 v1 。此时已经装好了虚拟网卡，且可以单独运行 edge 和 supernode。 

# MTU 设置
MTU 设置过大可能导致包过大，大包会在链路中被丢弃。所以设置为1300左右比较合适。n2n 默认 1400 一般物理网卡 MTU 一般为 1500 。

## 设置服务配置文件
编辑 `/etc/default/n2n` 按照注释编辑即可。

默认的文件不包含 MTU 和子网掩码选项，需要自己添加：
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

## 查看日志
```shell
journalctl _SYSTEMD_UNIT=n2n.service
```

# 自己设置 linux edge V1 自启动（未经测试）
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
- 好运博客 http://www.lucktu.com/
  - http://www.lucktu.com/archives/749.html
  - http://www.lucktu.com/archives/767.html
  - http://www.lucktu.com/archives/768.html
- https://www.zhuguodong.com/?id=398



# V1 问题
在树莓派下会卡死。
- 第一次卡死日志如下：
```
Feb 04 03:00:59 raspberrypi n2n[8990]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 03:01:59 raspberrypi n2n[8990]: Registering with supernode
Feb 04 03:01:59 raspberrypi n2n[8990]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 03:02:59 raspberrypi n2n[8990]: Registering with supernode
Feb 04 03:02:59 raspberrypi n2n[8990]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 03:03:59 raspberrypi n2n[8990]: Registering with supernode
Feb 04 03:03:59 raspberrypi n2n[8990]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 03:04:59 raspberrypi n2n[8990]: Registering with supernode
Feb 04 03:04:59 raspberrypi n2n[8990]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 03:05:59 raspberrypi n2n[8990]: Registering with supernode
Feb 04 03:05:59 raspberrypi n2n[8990]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 03:06:59 raspberrypi n2n[8990]: Registering with supernode
Feb 04 03:06:59 raspberrypi n2n[8990]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 03:07:59 raspberrypi n2n[8990]: Registering with supernode
Feb 04 03:07:59 raspberrypi n2n[8990]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 03:08:44 raspberrypi n2n[8990]: WARNING: Failed to decompress 1524 byte packet. LZO error=-4
```

- 第二次卡死日志如下：
```
Feb 04 16:32:37 raspberrypi n2n[8509]: Registering with supernode
Feb 04 16:32:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 16:33:37 raspberrypi n2n[8509]: Registering with supernode
Feb 04 16:33:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 16:34:37 raspberrypi n2n[8509]: Registering with supernode
Feb 04 16:34:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 16:35:37 raspberrypi n2n[8509]: Registering with supernode
Feb 04 16:35:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 16:36:37 raspberrypi n2n[8509]: Registering with supernode
Feb 04 16:36:37 raspberrypi n2n[8509]: Peer removed: pending=0, operational=1
Feb 04 16:36:37 raspberrypi n2n[8509]: Pending peers list size=1
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending additional REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending additional REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending additional REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending additional REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending additional REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending additional REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending additional REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending additional REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Sending additional REGISTER request to 1.82.188.216:25853
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: Pending peers list size=0
Feb 04 16:36:37 raspberrypi n2n[8509]: Operational peers list size=2
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: WARNING: Failed to find sender in pending_peers.
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: WARNING: Failed to find sender in pending_peers.
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: WARNING: Failed to find sender in pending_peers.
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: WARNING: Failed to find sender in pending_peers.
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: WARNING: Failed to find sender in pending_peers.
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: WARNING: Failed to find sender in pending_peers.
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: WARNING: Failed to find sender in pending_peers.
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: WARNING: Failed to find sender in pending_peers.
Feb 04 16:36:37 raspberrypi n2n[8509]: Received REGISTER_ACK from remote peer [ip=1.82.188.216:25853]
Feb 04 16:36:37 raspberrypi n2n[8509]: WARNING: Failed to find sender in pending_peers.
Feb 04 16:36:50 raspberrypi n2n[8509]: WARNING: Failed to decompress 1524 byte packet. LZO error=-6
```

第三次卡死
```
Feb 05 01:11:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=117.36.144.240:3999]
Feb 05 01:11:19 raspberrypi n2n[11285]: WARNING: Failed to find sender in pending_peers.
Feb 05 01:11:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=117.36.144.240:3999]
Feb 05 01:11:19 raspberrypi n2n[11285]: WARNING: Failed to find sender in pending_peers.
Feb 05 01:11:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=117.36.144.240:3999]
Feb 05 01:11:19 raspberrypi n2n[11285]: WARNING: Failed to find sender in pending_peers.
Feb 05 01:11:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=117.36.144.240:3999]
Feb 05 01:11:19 raspberrypi n2n[11285]: WARNING: Failed to find sender in pending_peers.
Feb 05 01:11:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=117.36.144.240:3999]
Feb 05 01:11:19 raspberrypi n2n[11285]: WARNING: Failed to find sender in pending_peers.
Feb 05 01:11:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=117.36.144.240:3999]
Feb 05 01:11:19 raspberrypi n2n[11285]: WARNING: Failed to find sender in pending_peers.
Feb 05 01:11:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=117.36.144.240:3999]
Feb 05 01:11:19 raspberrypi n2n[11285]: WARNING: Failed to find sender in pending_peers.
Feb 05 01:11:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=117.36.144.240:3999]
Feb 05 01:11:19 raspberrypi n2n[11285]: WARNING: Failed to find sender in pending_peers.
Feb 05 01:12:19 raspberrypi n2n[11285]: Registering with supernode
Feb 05 01:12:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 05 01:13:19 raspberrypi n2n[11285]: Registering with supernode
Feb 05 01:13:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 05 01:14:19 raspberrypi n2n[11285]: Registering with supernode
Feb 05 01:14:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 05 01:15:19 raspberrypi n2n[11285]: Registering with supernode
Feb 05 01:15:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 05 01:16:19 raspberrypi n2n[11285]: Registering with supernode
Feb 05 01:16:19 raspberrypi n2n[11285]: Received REGISTER_ACK from remote peer [ip=114.116.252.141:7654]
Feb 05 01:17:08 raspberrypi n2n[11285]: WARNING: Failed to decompress 1524 byte packet. LZO error=-4
```



# 备份
http://www.lucktu.com/archives/785.html

