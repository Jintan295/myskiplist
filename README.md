# 一个跳表数据库的可视化项目

## 说明

跳表实现是学习了carl哥的项目，地址为[https://github.com/youngyangyang04/Skiplist-CPP](https://github.com/youngyangyang04/Skiplist-CPP)



## 使用说明

1. 所需环境

   ```
   ubuntu
   django
   thrift
   ```

2. `python3 manage.py runserver 0.0.0.0:9999`启动django服务器

3. 在`database/src`目录下编译`g++ -c main.cpp crud/*.cpp`，然后链接`g++ -o main *.o -lthrift`

4. 运行`./main`，启动thrift服务

5. 测试，这是我的测试页面[182.92.85.127:9999](http://182.92.85.127:9999/)

## 不足

跳表锁还可以优化









