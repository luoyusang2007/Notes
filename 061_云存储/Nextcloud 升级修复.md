# 记一次 Nextcloud 升级和数据库修复
- 升级日期 2021-02-24
- 平台：树莓派 Raspbian + Docker
- https://registry.hub.docker.com/r/arm32v7/nextcloud 和 https://registry.hub.docker.com/r/linuxserver/nextcloud 都是可用的，后者支持多平台，用标签区分。但是不更改源便于维护：
  - 旧版 Nextcloud 版本号：18.0.0.2
  - 新版 Nextcloud 版本号：20.0.5.2
  - 旧版 Nextcloud Docker 镜像：arm32v7/nextcloud 278e1cf9fdeb
  - 新版 Nextcloud Docker 镜像：arm32v7/nextcloud 89e7acd2da8c

# 问题
- 旧版 Nextcloud 手机同步时经常卡死
- 旧版 Nextcloud 无法在网页上更新，已经停止维护

# occ 基本操作
即便 root 也无法操作 occ
- 如果容器内有 sudo，可以 `sudo -u` 
- 否则，需要知道 Owner user id 以连入容器。
  - 如果不知道 user id 可以尝试 root 连入，在 `/var/www/html` 执行 `./occ` 会提示 Owner id
  - 断开容器控制台，使用对应的 user id 连入，这在 portainer 网页中就可实现

# 服务器端解法
## 更新镜像
- `docker pull` 拉取最新镜像，此时若执行 `docker images` 查看镜像就可以看到旧的镜像变为无 tag
- 重新执行 docker-compose 或者在 portainer 中 recreate 容器即可
- 此时 volumes 挂载都没变化，你可以在 portainer 中对应容器的 log 中看到 版本无法升级，进入维护模式的信息。
- 查看最新的版本号
  - 使用正确的用户连入容器，具体查看 `occ 基本操作`
  - 执行 `./occ --version` 获得版本号 但这个不可使用
  - 进入容器内的 `/var/www/html/` 文件夹 `cat version.php`
    - $OC_Version array 中的数字就是最新版本号，如 array(20,0,5,2) 对应版本字符串 `20.0.5.2`
- 编辑 `config.php` 设置最新版本号
  - `'version' => 'XX.X.X.X',` 设置版本字符串
  - `'maintenance' => false,` 退出维护模式
- 进入网页进行更新
- 【可选】数据库修复，详情请见下文更新修复
- 遇到问题参考 https://help.nextcloud.com/t/exception-updates-between-multiple-major-versions-and-downgrades-are-unsupported/107831

## 修复数据库
由于我的数据库存在问题，可能是断电导致的，网页上报错 `oc_file_locks.key` 无法满足 unique 约束。数据库位于容器内的`data/owncloud.db`


在宿主机 sqlite3 执行
```sql
SELECT * FROM oc_file_locks 
    WHERE key IN 
    (SELECT key FROM oc_file_locks 
        GROUP BY key HAVING COUNT (key) = 1);
```
尝试输出导致冲突的行（即 key 重复的行），报错 `Error: database disk image is malformed`


### 证明数据库损坏
- `sqlite3 database_name` 进入数据库
- 运行 `PRAGMA integrity_check;`
- 未损坏报 OK 否则报错

### 尝试修复
- 尝试导出
  ```shell
  $ sqlite3 xx.db       # 打开
  sqlite>.output tmp.sql //有的是 .output "tmp.sql"
  sqlite>.dump
  sqlite>.quit
  ```
- 尝试导入
  ```shell
  $ sqlite3 XX_new.db   # 新建
  sqlite>.read tmp.sql  //有的是 .read "tmp.sql"
  sqlite>.quit
  ```
- 我的情况是 导入时报错，`oc_file_locks.key` 无法满足 unique 约束 ` UNIQUE constraint failed: oc_file_locks.key`
- 此方法失败

### 可行修复步骤
- 确保容器未运行
- 下载数据库到操作机
- 编辑，取消问题索引的 unique ，此后不报 `malformed` 错误
- 删除问题键的冲突行 参考 https://www.cnblogs.com/janehlp/p/10970190.html
- 加回索引 unique
- 上传到宿主机 volume 目录（对应容器的挂载）
- 若报错 `attempt to write a readonly database`，开放权限 666 即可解决。
- 重新导入导出，修复数据库结构

### 更新修复
- 运行容器，连入容器。具体查看 `occ 基本操作`
- `occ db:add-missing-indices` 自动修复丢失的索引
- `occ db:add-missing-primary-keys` 自动修复丢失的主键
- `occ db:add-missing-columns` 自动添加可选列
- `occ db:convert-filecache-bigint` 自动修复长整型问题

# Android 客户端重新上传
- 退出 Nextcloud 客户端
- 系统设置 应用管理，找到对应的 Nextcloud 客户端
- 在存储选项中清除数据所有缓存和数据
- 重新配置自动上传： 删除本地+覆盖服务器





