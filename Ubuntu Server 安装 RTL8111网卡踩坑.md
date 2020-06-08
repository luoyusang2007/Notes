# 系统
```
crsn@crsn_r420_3:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.3 LTS
Release:        18.04
Codename:       bionic
```

# 问题
系统可能会自作主张安装RTL8169的驱动。应该安装8168的。因为8168和8111在linux下驱动相同。

https://blog.csdn.net/ldl22847/article/details/8469156

# 下载驱动
https://www.realtek.com/zh-tw/component/zoo/category/network-interface-controllers-10-100-1000m-gigabit-ethernet-pci-express-software

选择 GBE 驱动下载。

# 安装 make 和 GCC



# 卸载错误的内核模块 8169
```
rmmod r8169
```



# 编译安装
解压 `tar.bz2` 文件，进入解压后的目录后：
```
./autorun.sh
```




# 重启






