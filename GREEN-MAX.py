import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
Green=platform.architecture()[0]
if Green=="32bit":__import__("Green32")
elif Green=="64bit":__import__("Green64")
