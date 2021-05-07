# 树莓派 NAS （Docker+NextCloud）


# 无 Docker 的参考
[简书文章引用，仅供参考](https://www.jianshu.com/p/54ab0753b244)

# 安装 docker 和 docker-compose
docker 安装后换源。参考 https://www.runoob.com/docker/docker-mirror-acceleration.html


# 拉取 docker 镜像
```shell
sudo docker pull arm32v7/nextcloud
```
适合 ARM 的镜像：[arm32v7/nextcloud](https://hub.docker.com/r/arm32v7/nextcloud/) 此镜像本身不包含 MySQL/MariaDB 所以要使用 MySQL/MariaDB 作为数据库，需要单独跑一个数据库容器。


参考资料：[参考1](https://www.jianshu.com/p/a6d355de3dba) [参考2](https://www.jianshu.com/p/f57390c9b68b) [参考3](https://www.jianshu.com/p/717884796efc)

> 要删除 composer 容器 `sudo docker-compose down`
> 要列出所有容器（包括停止的） `sudo docker ps -a` 或者 `docker container ls -a`

# 磁盘操作
## 基本操作
- 挂载 `sudo mount <partition> <path>`
- 卸载 `sudo umount <path>`
- 分区 `sudo fdisk <disk>` / `sudo parted <disk>`
- 格式化 `sudo mkfs -t ext4 <partition>`
- 查看使用和挂载情况 `df -h`
- 插入自动挂载（未验证） [参考](https://shumeipai.nxez.com/2015/06/23/raspberry-pi-usb-storage-device-automatically-mounts.html)


# EXT4 分区格式硬盘灯狂闪
- 按照 https://blog.csdn.net/stlinax/article/details/108029802 无效
- 按照 https://cloud.tencent.com/developer/article/1465600 无效
- 最后选择 ext3 格式，有所改善。
- https://segmentfault.com/a/1190000013515410 可能是没有重启的原因。
- https://www.bbsmax.com/A/gVdnpXNEJW/ ext4 的惰性初始化也是闪烁原因。但是如果日志不关，初始化完成之后还会闪烁
- 如果不进行惰性初始化，ext4 的格式化时间就会很长。因为格式化期间需要初始化。
- 对于 ext3 ，关闭文件系统日志之后还是就不会闪烁了。



# 大分区格式化
以 ext3 为例：
```shell
mkfs.ext3 -T largefile /dev/sdb1
```
其中 `-T largefile` 是为了加速格式化。



## 自动挂载
编辑 `/etc/fstab` 加一行：
```shell
# <partition_dev>  <dir_path>      <format>    defaults        0  0 
/dev/sdXN          /mnt/XXX         ext4        defaults        0  0
```
注意此文件编辑错误会导致无法开机。所以编辑完成之后要使用 `sudo mount -a` 测试，而非直接重启。

## Windows 访问 ext4 分区
- [读写 ext2 FSD](https://sourceforge.net/projects/ext2fsd/)
- [只读 ext2 Read](https://sourceforge.net/projects/ext2read/)

# 通过 docker-compose 启动 docker 镜像
先新建文件夹，然后进入此文件夹    
编写 `docker-compose.yml` ：
```yml
version: '2'
services:
  app:
    image: arm32v7/nextcloud
    ports:
      - "8888:80"                                 # 容器外:容器内
    volumes:
      - "./cloud/config:/var/www/html/config"     # Configure files
      - "./cloud/apps:/var/www/html/apps"         # App files
      - "/mnt/hdd2t/nextcloud:/var/www/html/data" # User data files
    restart: always
```
注意以上 YAML 不包含数据库。所以在网页配置阶段必须选择 Sqlite 数据库， 默认是 `html/data/owncloud.db` （容器内地址）。

运行（-d 后台运行）：
```shell
sudo docker-compose up -d
```


# 安装插件（应用）
解决应用商店打不开的问题：
国内镜像使用方法参考： http://www.orcy.net.cn/1129.html

## 方法一：科学上网
...

## 方法二：使用国内镜像
编辑配置文件 config.php
```php
$CONFIG = array (
  // ...
  // ADD:
  'appstoreenabled' => true,
  'appstoreurl' => 'https://www.orcy.net/ncapps/v1/',
  // ...
);
```

# 共享文件（群组）
- 进入网页 UI
- 先新建群组（用户分组）
- 点击要共享文件的共享按钮，侧边栏搜索群组名

# 开启外部存储
https://www.wangzhengzhen.com/3157.html

注意外部存储插件默认是被禁用了的。


# 手动添加文件
https://blog.csdn.net/wyw815514636/article/details/82020095

```bash
# 扫描所有用户的所有文件
sudo -u www-data php occ files:scan --all 
```
occ有三个用于管理 Nextcloud 中文件的命令：
- `files:cleanup` 清除文件缓存 
- `files:scan` 重新扫描，更新文件 
- `files:transfer-ownership` 移动所有文件和文件夹

