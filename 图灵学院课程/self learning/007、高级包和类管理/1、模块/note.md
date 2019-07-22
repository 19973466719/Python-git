# 1.模块
- 一个模块就是一个包含python代码的文件，后缀名.py，模块就是个python文件
- 为什么我们用模块
    - 程序太大，编程维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间，避免命名冲突

- 如何定义模块
    - 模块就是一个模块文件，任何代码可以直接书写
    - 不过根据模块的规范，最好在模块中编写以下内容
    - 函数（单一功能）
    - 类（相似功能的组合，或者类似业务模块）
    - 测试代码
    
- 任何使用模块
    - 模块直接导入
        - 导入的代码直接执行
        - 假如模块名称直接以数字开头，需要借助importlib帮助
    - 语法
        import module_name
        module_name.function_name
        module_name.class_name
    - import 模块 as 别名
    
    - from module_name import fuction_name or class_name
    - 需要什么导入什么
    - 使用的时候不需要前缀
    
    - 导入模块所有内容
    - from module_name import *
    
    if __name__ == '__main__'的使用
    - 可以有效避免模块代码被导入时被动执行的问题
    - 建议作为程序的入口
    
    
    
# 2.模块的搜索路径和存储
- 模块的搜索路径：
    - 加载模块时，系统会在那些地方寻找此模块
- 系统默认的模块搜索路径
    
        import sys
        sys.path 
    
    
- 添加搜索路径
    sys.path.append(dir)

- 模块的加载顺序
    1. 搜索内存中已经加载好的模块
    2. python的内置模块
    3. 搜索sys.python路径
    
    
# 包
- 包是一种组长管理代码的方式，里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

    /---包
    /---/---__init__.py 包的标志文件
    /---/---模块1
    /---/---模块2
    /---/---子包

- 包的导入操作
    - import package_name
    - 直接导入一个包，可以使用__init__.py中的内容
    - 使用方式是：
            
            package_name.func_name
            package_name.class_name.func_name()
    
    - 此种方式的访问内容是
    - 案例 pkg01 p07
    
    - import package.module
        - 导入一个包中某一个具体的模块
        - 使用方法
            
            package.module.func_name
            package.module.class.fun()
            package.module.class.var()
            
    import package.module as pm
    案例 p08
    
    
-from ... import导入
    - from package import module1,module2,module3
    - 此种方法不执行'__init__'的内容
        from pkg01 import p01
        p01.sayHello()
    - from package import *
        - 导入当钱包"__init__.py"文件中的所有函数和类
        - 使用方法
            
            fun_name()
            class_name.func_name
            class_name.var
        - 案例p09
- 在开放环境中，可以在当前包中直接导入其他模块中的内容
    - import 完整的包或者模块的路径
    
    - '__all__'的语法
        - 在使用from package impo * 的时候，* 可以导入的内容
        - "__init__.py"中如果文件为空，或者没有"__all__",那么只可以吧"__init__"中的内容为空
        - "__init__.py"如果设置了"__all__",那么按照"__init__"中的子包或者模块进行调用
        如此就不会载入"__init__"中的内容
        - '__all__'=['module1', 'module2','package']
        
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀

- 作用是防止命名冲突
    
    setName()
    Student.setName()
    Dog.setName()
    
    
     
    