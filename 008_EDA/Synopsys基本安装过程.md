# 与新思公司同名的软件
- 有一款光学 CAD/CAE 软件也叫 Synopsys ，但是并不是新思的产品。
- 巧合的是，新思公司也涉及光学 CAD/CAE 软件。

# 结构
- Synopsys 的EDA软件基于LINUX系统。应用软件以及授权管理器SCL的软件包是Synopsys自有的格式。

# 系统
- 由于 Synopsys 推荐 Redhat， 故使用 CentOS 7

# 桌面环境
## 使用远程 Xming
- bitvise SSH 客户端开启 `X11 Forwarding`
- 确保操作机的Xming正在运行
- 操作机退出多屏模式以增加兼容性
- 确保远程主机（被操控）开启了服务端的 `X11 Forwarding`配置文件位置： `/etc/ssh/sshd_config`


## 本机安装 XServer


# Synposys Installer 安装
- 先确保安装了csh包。
- Installer使用.run文件安装即可。
- 安装好后注意操作用户不能是root，且这个用户要有Installer安装目录以及temp目录的写入权。
- 最后，CD到Installer的安装目录，再使用非管理员运行：
```shell
./setup.sh
```
出现图形界面说明成功。

# Synposys SCL 安装
在 Installer 安装目录下执行：
```shell
./setup.sh
```
注意操作用户不能是root，且这个用户要有Installer安装目录以及temp目录、安装目标目录的的写入权。对于目标目录，可以新建并且设置写权限，如安装路径是`/usr/synopsys`：
``` shell
mkdir /usr/synopsys
chmod +w /usr/synopsys
```

SCL是授权管理器。在安装之前，先要安装 LSB 否则装完之后运行 `/usr/synopsys/scl/<ver>/<arch>/bin` 下的 `lmstat` 会报错 `/lib64/ld-lsb-x86-64.so.3: bad ELF interpreter` 。在 CentOS 下的安装命令如下：
``` shell
sudo yum install lsb
```

- 放置需要的安装包，注意安装包可能有依赖关系如果有多个
- 对于没有权限的文件夹，就手动新建（若没有）再手动给权限。

# Synopsys 其它组件安装
以下是实用组件得安装。

## VCS
过程和 SCL 安装一样。只是如果安装了64位版本，要使用 `-full64` 运行 VCS 。



# 激活授权


## 验证License
``` shell
<SCL_PATH>/amd64/bin/sssverify <dat File>
```



