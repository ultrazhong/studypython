# 项目时间：2022/3/10 9:50
# 浅拷贝：不拷贝子对象
# 深拷贝：拷贝子对象
class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, CPU, Disk):
        self.CPU = CPU
        self.Disk = Disk


cpu1 = CPU()
cpu2 = cpu1
print(cpu1,id(cpu1))
print(cpu2)
