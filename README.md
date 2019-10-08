# Develop Windows GUI exe file at MacOS.

### In MacOS

1. setup env

```bash
virtualenv -p python3 .env
source .env/bin/activate
touch read-file.py
```

Write python file as `read-file`...

2. MacOS debug

```bash
python read-file.py
# Will show GUI
```

### In windows

1. Install python3 at [here](https://www.python.org/downloads/windows/).
2. Open power shell.
3. cd the share folder of read-file.py (In fact, powershell can go to folder although it's not shared.)
4. Run `pip install pyinstaller`
5. Run `pyinstaller --onefile read-file.py` to pack exe.
6. Find `.exe` file at `dist/`