# 在 MacOS 上使用 win 虚拟机开发 GUI exe

### In MacOS

编写 python 文件

MacOS 调试

    python read-file.py
    # 会出现 GUI

### In windows

1. Install python3 at [here](https://www.python.org/downloads/windows/).
2. Open power shell.
3. cd 到 [read-file.py](http://read-file.py) 共享的文件夹(此处不设置共享文件在 powershell 中也能进入)
4. `pip install pyinstaller`
5. `pyinstaller --onefile read-file.py`
6. 在 dist 文件夹中找到 .exe 文件