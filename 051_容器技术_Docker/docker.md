# 容器和镜像
- 镜像：不变的，需要 `docker build` 自己构建或者 `docker pull` 下载
- 容器：可变的，用于运行的。 `docker run` 时创建

# Docker File
用于构建（即生成）镜像。

## 基本项
- **FROM** 声明基于哪个已存在的镜像。
- **RUN** 在镜像构建时运行，比如 `apt-get` 、 软件 `build`  之类。尽量写一行。因为多个 RUN 会创建多层镜像。
- **ONBUILD** 在 FROM 本镜像的子镜像构建时执行。
- **CMD** 在容器运行时运行，会被 `docker run` 的参数覆盖
- **ENTRYPOINT** 类似 CMD ，但其不会被 `docker run` 的命令行参数指定的指令所覆盖，而且这些命令行参数会被当作参数送给 ENTRYPOINT 指令指定的程序。
- **COPY** 构建时从主机往镜像里放东西。
- **ADD** 类似 COPY ，但是对 tar 文件行为不同。用处不大，官方推荐用 COPY 。
- **EXPOSE** 声明要暴露的端口，在 `docker run -P` 时随机映射端口。用处不大，因为一般的端口映射是在 run 的时候用 `-p` 定义的。**尽量在 run 时配合 `-p` 使用**
- **VOLUME** 文件挂载。`docker run` 时如果没有 `-v` 指定挂载位置，就会使用默认（随机）位置挂载。用处不大，但是可以确保用户数据存在主机中。**尽量在 run 时配合 `-v` 使用**
- **WORKDIR**
- **USER**
- 其它

# Docker-Compose
Docker Compose 不但可以用于启动 docker 容器，还可以进行构建。
## Links

## External-Links

# Volume 挂载
Docker 的 Volume 挂载原则
- 容器被删除，主机内的 Volume 文件不被删除
- `docker run -v` 指定本地目录 Bind Mount
- `docker run -v` 不指定本地目录， 自动生成 volume 于 `/var/lib/docker/volumes/`， 由 Docker 管理
- `docker run --volumes-from` 可以从已有容器共享 Volume

# docker 命令
- `docker run` 新建容器
- `docker exec` 在运行中容器中执行命令
- `docker service` swarm 管理命令
  - 一个 Service 管理多个 Task
  - 一个 Task 管理一个 Container
- `docker attach` 连接到正在运行中的容器
- `docker update` 更改容器配置，volume 除外
- ...