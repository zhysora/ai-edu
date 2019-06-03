## 测试准备
* 硬件环境：启智机器人以及其配备的各传感器
* 软件环境：启智机器人官配的机载电脑上的Ubuntu系统以及配置好的ROS
* 测试人员：周环宇
* 时间分配：1-2天（5.25-5.26）

## 测试数据准备
* 模拟地图环境写在了clean_module/src/test_dfs.cpp中，是一个4*4的网格图
* 真实环境是在实验室G1027通过Gmapping建图用map_saver保存下来的map.yaml放在目录clean_module/config下

## 输入
模拟地图为4*4的网格图。有三种测试参数的输入，分别为mode=0, level=0; mode=1, level=0; mode=1, level=3。（mode代表扫地模式，level代表扫地强度）

## 预取的输出
期望输出在clean_module/src/test_dfs.out中

## 评价准则
对输出的字符串信息与标准答案test_dfs.out逐行比对

## 测试流程
1. 终端运行 “cd ~/catkin_ws”
2. 终端运行 “catkin_make”
3. 终端运行 “rosrun clean_module test_dfs >> a.out”
4. 终端运行 “diff a.out test_dfs.out”
5. 如果diff没有输出任何信息，表示两文件没有差异，则测试成功，否则失败。

## 输入
向机器人分别说出“stop”与“go” 

## 预取的输出
```
[test_voice]: Stop
[test_voice]: Go
```
## 评价准则
当向机器人说“stop”时，终端打印出“[test_voice]: Stop”记0.5分；当向机器人说“go”时，终端打印出“[test_voice]: Go”，记0.5分。满分1分为通过

## 测试流程
1. 终端运行 “cd ~/catkin_ws”
2. 终端运行 “catkin_make”
3. 开启启智机器人，确认电脑能上网
4. 终端运行 “rosrun clean_module test_voice”
5. 向机器人说“stop”，观察终端输出
6. 向机器人说“go”，观察终端输出

## 输入
clean_module/config下的地图，以及执行启动命令“roslaunch clean_module my_clean.launch [mode:=] [level:=]”的运行参数mode与level，以及对机器人进行的“go”“stop”语音输入。

## 预取的输出
* 当执行“roslaunch clean_module my_clean.launch mode:=0”时，机器人的运行轨迹满足当一个方向可以走时会一致沿着当前方向走下去，直到走不通枚举下一个方向，称为“绕圈型”。遍历完图后返回原点。
* 当执行“roslaunch clean_module my_clean.launch mode:=1”时，机器人的运行轨迹满足优先枚举前后方向，其次枚举左右方向，称为“Z字形”。遍历完图后返回原点。
* 当执行“roslaunch clean_module my_clean.launch level:=1”时，机器人的运行轨迹满足每走一步会重复一个来回，再走下一步。
* 当向机器人说出“stop”时，机器人会停止。
* 当向机器人说出“go”时，机器人会继续。

机器人整体运行过程中会躲避障碍物（包括静态的以及动态的）。

## 评价准则
* 执行“roslaunch clean_module my_clean.launch mode:=0”，机器人的运行轨迹满足当一个方向可以走时会一致沿着当前方向走下去，直到走不通枚举下一个方向，称为“绕圈型”。遍历完图后返回原点。 记0.2分。
* 执行“roslaunch clean_module my_clean.launch mode:=1”，机器人的运行轨迹满足优先枚举前后方向，其次枚举左右方向，称为“Z字形”。遍历完图后返回原点。记0.2分。
* 执行“roslaunch clean_module my_clean.launch level:=1”，机器人的运行轨迹满足每走一步会重复一个来回，再走下一步。记0.2分。
* 向机器人说出“stop”，机器人会停止。记0.1分。
* 向机器人说出“go”，机器人会继续。记0.1分。
* 机器人整体运行过程中会躲避障碍物（包括静态的以及动态的）。记0.2分。

满分1分为通过。

## 测试流程
1. 终端运行 “cd ~/catkin_ws”
2. 终端运行 “catkin_make”
3. 开启启智机器人，确认电脑能上网
4. 终端运行 “roslaunch clean_module my_clean.launch mode:=0”，观察机器人路径
5. 终端运行 “roslaunch clean_module my_clean.launch mode:=1”，观察机器人路径
6. 终端运行 “roslaunch clean_module my_clean.launch level:=1”，观察机器人路径
7. 终端运行 “roslaunch clean_module my_clean.launch”，在机器人运动过程中发出指令“stop”观察机器人行为，发出指令“go”观察机器人行为
8. 终端运行 “roslaunch clean_module my_clean.launch”，在机器人前进过程中添加一些障碍物，观察机器人行为
