# 项目时间：2022/3/10 19:43
# with可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，以此来达到释放资源的目的
# with open('logo.png','rb') as src_file:
#       src_file.read()

with open('1.txt', 'r') as file:
    print(file.read())  # 无需手动close
# 离开运行时上下文，自动调用了上下文管理器的特殊方法__exit__()


with open('jxau_logo.png','rb') as src_file:
    with open('copyjxau_logo2.png','wb') as target_file:
        target_file.write(src_file.read())

