# Nextcloud 容器迁移/修改挂载路径
- 原 docker-compose.yml
    ```yaml
    version: '2'
    services:
    app:
        image: arm32v7/nextcloud
        ports:
        - "8888:80"
        volumes:
        - "./cloud/config:/var/www/html/config"
        - "./cloud/apps:/var/www/html/apps"
        - "/mnt/hdd2t/nextcloud:/var/www/html/data"
        restart: always
    ```
- 新 docker-compose.yml
    ```yaml
    version: '2'
    services:
    app:
        image: arm32v7/nextcloud
        ports:
        - "8888:80"
        volumes:
        - "/mnt/hdd2t/nextcloud:/var/www/html"
        restart: always
    ```
可见新文件将 html 文件夹整体挂载。

# 修改挂载路径思路
Docker 本身不支持修改挂载路径，不如重新 run 容器。

# 步骤
- Stop 原容器
- 按照新配置组织文件夹（复制进来）
  - 文件夹组织过程可能会丢失文件所有者信息，但是在宿主机修复文件所有者并不方便，所以等进入容器后再操作。
- 删除原容器（不删除无法更改 volume 位置）
- 按照新配置创建新容器
  - 此时访问服务器会报服务器内部错误，这可能是因为没有权限
- 更改所有者
  - 使用 root 进入容器，进入 html 目录
  - `chown -R www-data .`
- 网页和 app 测试
- 删除原匿名 volume

