# 项目时间：2022/3/7 14:21
import traceback

try:
    print('----------------------')
    print(1 / 0)
except:
    traceback.print_exc()
