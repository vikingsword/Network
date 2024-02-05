## pyinstaller 相关命令
### 1. pip install pyinstaller
### 2. pyinstaller your_script.py   :   直接编译脚本
### 3. pyinstaller --noconsole your_script.py   ：   取消启动exe的控制台
### 4. pyinstaller --onefile your_script.py     ：   生成单个文件



## cx_Freeze 相关命令
### 1. 配置 setup.py
### 2. 取消 cmd 窗口在 executables 添加 base 参数
### 3. 生成单个文件在 executables 添加 target_name 参数