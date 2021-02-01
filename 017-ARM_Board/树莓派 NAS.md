# 树莓派 NAS （Docker+NextCloud）


# 无 Docker 的参考
[仅供参考](https://www.jianshu.com/p/54ab0753b244)

# 安装 docker 和 docker-compose
docker 安装后换源


# 拉取 docker 镜像
```shell
sudo docker pull arm32v7/nextcloud
```
适合 ARM 的镜像：[arm32v7/nextcloud](https://hub.docker.com/r/arm32v7/nextcloud/)


参考资料：    [参考1](https://www.jianshu.com/p/a6d355de3dba) [参考2](https://www.jianshu.com/p/f57390c9b68b) [参考3](https://www.jianshu.com/p/717884796efc)

> 要删除 composer 容器 `sudo docker-compose down`
> 要列出所有容器（包括停止的） `sudo docker ps -a` 或者 `docker container ls -a`

# 磁盘操作
## 基本操作
- 挂载 `sudo mount <partition> <path>`
- 卸载 `sudo umount <path>`
- 分区 `sudo fdisk <disk>`
- 格式化 `sudo mkfs -t ext4 <partition>`
- 查看使用和挂载情况 `df -h`
- 插入自动挂载（未验证） [参考](https://shumeipai.nxez.com/2015/06/23/raspberry-pi-usb-storage-device-automatically-mounts.html)



## 自动挂载
编辑 `/etc/fstab` 加一行：
```shell
# <partition_dev>  <dir_path>      <format>    defaults        0  0 
/dev/sda1          /dsf            ext4        defaults        0  0
```


## Windows 访问 ext4 分区
[ext2fsd](https://sourceforge.net/projects/ext2fsd/files/latest/download)


# 通过 docker-compose 启动 docker 镜像
先新建文件夹，然后进入此文件夹    
编写 `docker-compose.yml` ：
```yml
version: '2'
services:
  app:
    image: arm32v7/nextcloud
    ports:
      - "8888:80" # 容器外:容器内
    volumes:
      - "./cloud/config:/var/www/html/config" # Configure files
      - "./cloud/apps:/var/www/html/apps" # App files
      - "/mnt/hdd2t/nextcloud:/var/www/html/data" # User data files
    restart: always
```

运行（-d 后台运行）：
```shell
sudo docker-compose up -d
```


# 安装插件

# 共享文件（群组）
先新建群组
