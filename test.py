# 作者：g pc
# 开发时间：2023/8/29 17:33
import concurrent.futures

# 协程
# 函数有yield的是生成器函数，返回的就是一个生成器
# 反复跳跃，
# yield这种实现没意义
# def fun1():
#     yield 1
#     yield from fun2()  # 跳到fun2()
#     yield 2
#
#
#
# def fun2():
#     yield 3
#     yield 4
#
#
# f1 = fun1()
# for item in f1:
#     print(item)



#在python3.7之后被替代了（下面一个实例就是替代者），被报错
# import asyncio
# @asyncio.coroutine  # coroutine是协程意思
# def fun1():
#     print(1)
#     # 网路IO请求，下载一张图片
#     yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其他任务，规定写法
#     print(2)
#
#
# @asyncio.coroutine
# def fun2():
#     print(3)
#     # 网络IO请求，下载一张图片
#     # 发送请求，需要等待返回结果，就可以干别的工作
#     yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其他任务
#     print(4)
#
# task = [
#     asyncio.ensure_future(fun1()),
#     asyncio.ensure_future(fun2())
# ]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(task))



# 1.4async&await关键字（推荐）





# import asyncio
#
# async def fun1():
#     print(1)
#     # 网路IO请求，下载一张图片
#     await asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其他任务，规定写法
#     print(2)
#
#
#
# async def fun2():
#     print(3)
#     # 网络IO请求，下载一张图片
#     # 发送请求，需要等待返回结果，就可以干别的工作
#     await asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其他任务
#     print(4)
#
# task = [
#     asyncio.ensure_future(fun1()),
#     asyncio.ensure_future(fun2())
# ]
#
# # 去生成或后去一个事件循环
# loop = asyncio.get_event_loop()
# # 将任务放到任务列表
# loop.run_until_complete(asyncio.wait(task))


# 2.协程意义
# 在一个线程中，如果遇到IO等待时间，线程不会傻傻等，利用空闲时候再去干点其他事
# 


# 快速上手
# 协程函数：定义函数的时候  async def 函数名
# 携程对象，执行协程函数（）得到的协程对象


# # 如果想要运行协程函数内部代码，必须要讲协程对象交给事件循环来处理
# import asyncio
#
# async def fun():
#     print("快来")
#
# result = fun()
#
# # 下面两条等于下下面一条
# loop = asyncio.get_event_loop()
# loop.run_until_complete(result)
#
# asyncio.run(result)  # python3.7可以实现


# 3.3  await
# await+可等待的对象（协程对象、future、task对象->Io等待）
# await就是等待对象的值得到结果之后在继续向下走


# 3.4Task对象
# 白话：在事件循环中添加多个任务
# Tasks用于并发调度协程，通过asyncio。creat_task(协程对象)的方式创建Task对象,这样可以让协程加入实践循环中等待被调度执行，除了使用asyncio。creat_task
# 还可以用loop

# asyncio有future一个对象
# concurrent.futures.Future对象，是使用线程池、进程池实现异步操作时用到的对象

# 以后写代码可能会存在交叉实践，例如：crm项目80%基于协程异步协程 + MySQL(不支持）[线程、进程做异步编程】

# 案例asyncio+不支持异步的模块

# 3.6异步迭代器
# 迭代器：

# 异步上下文管理器
# uvloop  asyncio的事件循环的替代方案，事件循环效率》默认asyncio的实践循环，
# pip install uvloop




# 5.实战案例

# 5.1异步redits
# 在使用python代码操作redis时，链接、操作、断开都是网络IO
# pip install aioredits
# 异步SQL，
# 异步FastAPI框架












































































































