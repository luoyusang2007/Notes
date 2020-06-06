# 课程来源

https://www.bilibili.com/video/BV1PJ411K7m

# 原理






# 门级后仿真

带延迟信息的仿真。

## 一般的门延迟
- 器件自身的延迟
- 连线的延迟

后仿真关注 Toggle Coverage 。RTL 文件输出给 DC 综合器， DC 按照工艺库输出门级网表。ICC 布局布线工具是有物理信息/寄生参数的。DC 使用线延迟模型/负载模型计算延迟，不知道器件放在具体哪个位置，生成的延迟信息并不准确。ICC 吐出的网表一般比 DC 更加准确。


DC 和布线工具生成 门级网表 .v 和 SDF 延迟文件。DC 综合过程可以保留层次结构，也可不保留。

## 






## Delay Filtering
- Inertial Delay(VCS Default): Pulses shorter than device delay are filtered out.
  - Devices(Components) Only
- Transport Delay: All pulses are propagated through (no filter).







