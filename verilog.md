# verilog 中的 always 和 @
- always 后面一般会加 @ 
- 但是 always 后可以没有 @
- @ 也不一定非要有 always 在先

```verilog
always #10 clk = ~clk
```

```verilog
initial forever #10 clk = ~clk
```
以上两种写法仿真效果相同，但是只有 always 可以被综合。


# deassign force release

# 双等号和三等号
- 双等号比较，(x==x) is x; z; z==z is x， 可被综合
- 三等号，x===x is 1; z===z is 1; 不可被综合

# 赋值语句的种类
- 【连续】连续赋值 assign
- 【过程】阻塞赋值 =
- 【过程】非阻塞赋值 <=
- 【过程连续】
  - deassign
  - force
  - release


# task 和 function
## Function
1. 函数定义不能包含有任何的时间控制语句，即任何用#、@、wait来标识的语句。
2. 函数不能调用“task”。
3. 定义函数时至少要有一个输入参数。
4. 在函数的定义中必须有一条赋值语句给函数中与函数名同名、位宽相同的内部寄存器赋值。
5. verilog中的function只能用于组合逻辑；
6. function 可以在assign语句中使用




# wait
不可综合的

# 传播 

# vector
Verilog 中的向量指的是 位宽 不为 1 的量。

# reduce
把一个向量合并成一位。

# receive 

# fork join


# 显式 0 延迟
不同仿真器会有不同的结果。

# 分层事件队列
- 对于每个层，事件执行的先后顺序无关


- Active： 大多数事件。
  - 连续赋值（assign 语句）
  - 非阻塞赋值的右边式计算
  - 阻塞赋值
  - $display
- Inactive： 
  - 显式 0 延迟
- NBAssign 
  - 非阻塞赋值的赋值
- Monitor
  - $monitor

# 内外延迟
## 外延迟
- 写在前面效果和写在上一句一样

## 过程中非阻塞赋值的内延迟
```verilog
always @ (posedge clk) begin
    a <= #10 b;
end
```

## 过程中阻塞赋值的内延迟
```verilog
always @ (posedge clk) begin
    a = #10 b;
end
```


# forever 和 always

# while 和 repeat

# 结束仿真
`$finish`
在非交互模式下 `$stop` is `$finish`

