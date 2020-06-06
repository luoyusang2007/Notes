# 确保本机没有Java
CMD运行`java`应当报错，并且控制面板-删除程序中看不见JDK。

# 下载JAVA
https://www.oracle.com/java/technologies/javase-downloads.html

# 安装
安装包含两步，JDK是开发工具，JRE是运行环境。

# 设置环境变量
| 变量名    | 操作 | 值              |
| --------- | ---- | --------------- |
| JAVA_HOME | 新建 | JDK安装路径     |
| PATH      | 追加 | %JAVA_HOME%\bin |

# 验证JAVA是否安装成功
```
> java
> javac
```
CMD 输入上述命令，分别看是否有输出。