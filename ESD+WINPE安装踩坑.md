# PE 选择
有的PE原生驱动不够，又不支持加载驱动（如微 PE），导致硬盘无法识别。可选择优启 PE ，注意直接用 Rufus 烧录 ISO 即可。它带的工具可能报病毒

# EFI
电脑要设置 UEFI BOOT。

# ESD 文件
win 10 镜像已经不是wim文件，而是esd。

# EFI WIN10 安装

- 把目标硬盘转换为GPT格式
- 用 DiskGenius 新建分区
  - 途中要新建 ESP 分区，4096对齐，
  - MSR 分区是为了防止在旧版系统误删的，可以不建

# 俄罗斯大神版本 Windows 

https://www.52pojie.cn/thread-732968-1-1.html
安装好后，桌面**管理员**运行 `Restart.cmd`


# 激活
https://03k.org/kms.html

```bat



```
