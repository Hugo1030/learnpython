# learn python in hard way
### 练习0 安装python和atom
1. 下载atom,网址https://atom.io/
2. 把atom放到dock
3. 找到terminal终端
4. 把它放到dock
5. 在terminal里面打python
6. 输入quit()加回车退出Python
7. 在GitHub上创建一个仓库，learnpython
8. 将仓库clone到本地
9. cd learnpython进入本地仓库
10. 使用atom编辑python文档，保存在learnpython仓库
11. 以后完成的练习通过git上传到GitHub上保存

### 练习1 Hello world
1. 在atom里面输入代码
2. 练习print
3. 练习””和’’输出str
4. 练习在terminal中查看程序运行结果
5. 打开terminal,首先进入cd learnpython
6. 然后输入python ex1.py

### 练习2  注释
1. #后面是注释内容，不在程序内运行

### 练习3 数字和数学计算
1. 练习基本+ - * / %(求余数)
2. 练习Print 用,（逗号）隔开，会在同一行输出，中间空格
3. 如果要换行，需要在另一行重新输入print

### 练习4 变量
1. 学习给变量赋值 用‘=’
2. 学习分析错误原因，未给变量赋值
3. 学会变量之间做数学计算
4. 学习输入让阅读更美观，运算符号后面加个空格

### 练习5 格式化输入
1. 变量既可以赋值为数字，又可以赋值为str
2. Print 一句话中，可以先用格式化字符占位，后面再进行填充。
3. 格式是%s(代表这个位置是一个str)，后面%字符串
4. %d（代表这是一个整数）
5. 如何要输出多个格式化字符，后面需用()中间用,隔开
6. 句子和%之间没有逗号，注意

### 练习6 更多格式化输入
1. 格式化字符可以嵌套使用
2. %r表示不带格式的完全输出
3. 两个str中间用+连起来，等于两句话连起来在同一行输出

### 练习7 更多的Print输出
1. Str通过*可以重复N次
2. 一句话以,逗号结尾，下一句可以和上一句在同一行输出，中间空一格

### 练习8 更多的print
1. 在双引号里面再出现双引号，输出时，里面的双引号变成单引号
2. 格式化输出可以调用自身，注意输出里面是没有逗号

### 练习9 更多的Print
1. \n代表换行符
2. 打印多个内容在同一行，中间用，逗号隔开
3. “”“ ”“”三引号之间的内容，可以输入多行str文本，原样输出
4. ‘’和“”只能输出单行文字

### 练习10 转义字符
1. \t为制表符，代表一个缩进
2. \n为换行符，\\为一个\

### 练习11  输入
1. raw_input—>string
2. Input = eval(raw_input())—>int
3. Pydoc和help()不同，前者功能更强，help只能用于函数

### 练习12 提示
1. raw_input(string)

### 练习13 参数解包变量
1. 引入sys模组，里面argv函数，为程序添加变量
1. argv[0]为程序名，后面才是参数
2. 为了让输出美观点，注意中间空行

### 练习14 解包参数和输入
1. 参数解包是事先输入的，更多用于固定情况，比如程序名，人名
2. raw_input更多是用于与用户的交互，界面更友好，更多提示

### 练习15 读文件
1. 可以用argv解开文件名，因为文件名是固定的，不需要用户交互。
2. open(name[, mode[, buffering]]) -> file object
  * 例如：open(filename,'w')
3. open函数如果不指定打开方式的话，默认为read
4. 文件要先打开为file object，然后才能使用write,read等操作。

### 练习16 读写文件
1. 基本文件操作
  * read
  * write('stuff')
  * close
  * readline
  * truncate
2. 使用一个无实际作用的raw_input来让用户控制程序进程。一个是回车继续，一个是CTRL-C退出，巧妙。

### 练习17 更多的文件操作
1. 引入了新的os.path模组里面的exists函数，判断文件是否存在
