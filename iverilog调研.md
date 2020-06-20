# iVerilog
参考自以下：
- https://iverilog.fandom.com/wiki/Developer_Guide
- https://github.com/steveicarus/iverilog/blob/master/developer-quick-start.txt
- https://blog.csdn.net/weixin_38235859/article/details/105478064
- http://exasic.com/article/index.php?md=e-06

# iverilog 编译安装过程剖析
- 预编译入口：`autoconf.sh`
- 引自官方：`You will need autoconf and gperf installed in order for the script to work`
- gperf 是用于生成散列函数的，此处被称为 `pre-compile` 工作。

``` shell
- 
echo "Autoconf in root..."
# 默认加载 configure.in 生成 configure 可执行文件
autoconf -f  

echo "Precompiling lexor_keyword.gperf"
gperf -o -i 7 -C -k 1-4,6,9,\$ -H keyword_hash -N check_identifier -t ./lexor_keyword.gperf > lexor_keyword.cc 

echo "Precompiling vhdlpp/lexor_keyword.gperf"
(cd vhdlpp ; gperf -o -i 7 --ignore-case -C -k 1-4,6,9,\$ -H keyword_hash -N check_identifier -t ./lexor_keyword.gperf > lexor_keyword.cc )

```


- 编译安装：`./configure` & `make` as root & `make install` as root.
- 注意，`./configure` 会生成 `makefile`
- 默认进入第一条 `make all` 即进入所有在变量 `SUBDIRS` 中列出的子文件夹执行 `make` 

```shell

SUBDIRS = ivlpp vhdlpp vvp vpi libveriuser cadpli tgt-null tgt-stub tgt-vvp \
          tgt-vhdl tgt-vlog95 tgt-pcb tgt-blif tgt-sizer driver

```

# 组件

## IVLPP
- 用途：词法与语法分析
- 源码位置：
- 安装后位置：`iverilog/lib/ivl`


| 名称       | 功能           | 实现 | 代码规模 |
| ---------- | -------------- | ---- | -------- |
| driver     |                |      |          |
| ivlpp      | 词法与语法分析 |      |          |
| vhdlpp     |                |      |          |
| vvp        | 仿真虚拟机     |      |          |
| vpi        |                |      |          |
| cadpli     |                |      |          |
| tgt-vvp    | 代码生成器     |      |          |
| tgt-vhdl   | 代码生成器     |      |          |
| tgt-vlog95 | 代码生成器     |      |          |


# 功能


# 规模

iVerilog 这个规模的项目工作量很可能在2000天*人以上。
贴出统计如下：

## Summary

Date : 2020-06-20 18:37:35

Directory e:\iverilog

Total : 595 files,  163947 codes, 37465 comments, 37138 blanks, all 238550 lines

[details](details.md)

### Languages
| language     | files |    code | comment |  blank |   total |
| :----------- | ----: | ------: | ------: | -----: | ------: |
| C++          |   391 | 110,178 |  27,141 | 26,578 | 163,897 |
| C            |   167 |  52,237 |   9,449 | 10,215 |  71,901 |
| Verilog      |    11 |   1,210 |     753 |    254 |   2,217 |
| Shell Script |     6 |     169 |     113 |     65 |     347 |
| Properties   |    19 |     106 |       9 |     19 |     134 |
| YAML         |     1 |      47 |       0 |      7 |      54 |

### Directories
| path          | files |    code | comment |  blank |   total |
| :------------ | ----: | ------: | ------: | -----: | ------: |
| .             |   595 | 163,947 |  37,465 | 37,138 | 238,550 |
| cadpli        |     2 |     115 |      37 |     29 |     181 |
| driver        |     4 |   1,239 |     206 |    239 |   1,684 |
| driver-vpi    |     1 |     454 |      97 |    112 |     663 |
| examples      |    12 |   1,230 |     785 |    262 |   2,277 |
| ivlpp         |     2 |     398 |      73 |     80 |     551 |
| libmisc       |     4 |     286 |     112 |     88 |     486 |
| libveriuser   |    53 |   2,058 |   1,207 |    597 |   3,862 |
| scripts       |     5 |      79 |      87 |     32 |     198 |
| tgt-blif      |    18 |   1,184 |     443 |    297 |   1,924 |
| tgt-fpga      |    19 |   3,497 |     871 |  1,033 |   5,401 |
| tgt-null      |     3 |      38 |      21 |     12 |      71 |
| tgt-pal       |     8 |     412 |     264 |    160 |     836 |
| tgt-pcb       |     9 |     419 |     202 |    114 |     735 |
| tgt-sizer     |     6 |     320 |     134 |    102 |     556 |
| tgt-stub      |    11 |   2,657 |     351 |    534 |   3,542 |
| tgt-verilog   |     1 |     307 |      58 |     75 |     440 |
| tgt-vhdl      |    23 |   5,655 |   1,420 |  1,313 |   8,388 |
| tgt-vhdl\vhpi |     1 |       5 |       0 |      2 |       7 |
| tgt-vlog95    |    12 |   7,121 |   1,287 |    440 |   8,848 |
| tgt-vvp       |    23 |   8,473 |   1,855 |  1,902 |  12,230 |
| vhdlpp        |    59 |  10,541 |   2,107 |  2,751 |  15,399 |
| vpi           |    60 |  27,074 |   4,488 |  5,584 |  37,146 |
| vvp           |   100 |  33,537 |   7,158 |  8,049 |  48,744 |

[details](details.md)






# SDF
iVerilog 支持 `$sdf_annotate` 命令，但是根据相关BUG报告，在遇到三态门时，这样的支持不可靠。














