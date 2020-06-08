# 系统
CentOS 7 ，安装时勾选了 Gnome 桌面环境。




# 退出图形化
在图形化界面新建终端，执行：
```
init 3
```



# CentOS 7 Enable SSH

```
vim /etc/ssh/sshd_config
```

使能 Permit Root ， 端口 和 IP



# 两个报错文件
nvidia 安装时有两个报错文件，都要看。
```shell
cat /var/log/nvidia-installer.log
cat /var/log/cuda-installer.log
```


# 安装依赖
## DKMS
```
yum install rpmlib
```
装好之后再：
```
 yum install dkms
```
直接装的话提示找不到。


内核头和deve？


# 禁用原驱动 nouveau
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-nouveau

否则会报错`ERROR: Unable to load the kernel module 'nvidia-drm.ko'`

## CentOS
``` shell
# Create File
$ sudo vim /etc/modprobe.d/blacklist-nouveau.conf
```

Content:
```
blacklist nouveau
options nouveau modeset=0
```

```shell
$ sudo dracut --force
```

## Fedora
- Create a file at `/usr/lib/modprobe.d/blacklist-nouveau.conf` with the following contents:
```
blacklist nouveau
options nouveau modeset=0
```
- Regenerate the kernel initramfs:
```
$ sudo dracut --force
```
- Run the below command:
```
$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```
- Reboot the system

# 指定内核路径安装
例如：
```shell
./cuda_10.2.89_440.33.01_linux.run --kernel-source-path=/usr/src/kernels/3.10.0-1127.10.1.el7.x86_64/

```



```
                                                  
               |-------|              \           
               |       |         ======>          
               |-------|              /           
                /  |  \                           
              /    |    \                         
            /      |      \                       
          /        |        \                     
        /          |          \                   
   |-------|   |-------|   |-------|              
   |       |   |       |   |       |              
   |-------|   |-------|   |-------|              



```
