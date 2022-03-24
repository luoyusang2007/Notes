# 安装
参考 https://www.yiboard.com/thread-1495-1-1.html
1. Cosmic: STM8 编译器，命令行工具，被 STVD 调用。
   1. https://www.cosmicsoftware.com/download_stm8_free.php
   2. 安装后按照提示注册，提供邮箱后接收 License
   3. STM8 License 放置在 [安装路径]\FSE_Compilers\CXSTM8\License\license.lic
2. STVD: 调试和开发工具，不太好用但是可以调试，带 STLINK 驱动
   1. https://www.st.com/en/development-tools/stvd-stm8.html
   2. 安装路径不带中文和空格
   3. Tools -> Options -> Toolset 设为 `STM8 Cosmic` 路径 `...\FSE_Compilers\CXSTM8`
3. SPL(Standard Peripheral Library)
   1. STM8L10X: https://www.stmicroelectronics.com.cn/en/embedded-software/stsw-stm8012.html
   2. STM8TL5x: https://www.stmicroelectronics.com.cn/en/embedded-software/stsw-stm8030.html
   3. STM8S/A: https://www.stmicroelectronics.com.cn/en/embedded-software/stsw-stm8069.html
   4. Others: https://www.stmicroelectronics.com.cn/en/embedded-software/stsw-stm8016.html


# STVD 项目配置

注意 Workspace 自己新建， 然后再建 Project。 Project 文件夹要手动输入，不要用默认，手动新建在 Workspace 文件夹中。

# 用 SPL （标准外设库）
## 选择设备
In stm8s.h:
```c
#define STM8S103   
```
## 更改中断向量表
`stm8_interrupt_vector.c` 是 STVD 自动生成的，但是向量表是空的，要自己填。向量表在芯片的 Datasheet 找。
还要注意，`stm8_interrupt_vector.c`  里的 `NonHandledInterrupt` 注释掉，因为库里会重新定义。
