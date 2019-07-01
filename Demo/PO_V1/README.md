1、HTML+DOM

    元素定位 - 8  xpath- 多种
    元素操作：4大基本：send_keys,click,text,get_attribute
    等待 - 3种 sleep-助攻   显性等待-主攻   隐性等待-幕后/佯攻
    3种切换 - switch_to     window , iframe ， alert  - 先找到，再切换。
    下拉列表-Select  鼠标操作 - ActionChains  按键操作 - Keys
    js助攻 - 日历 / 修改属性 /滚动条
    上传 - windows - autoit/pywin32 -windows     --mac sikuli

2、画个思维导图。

3、项目实战

    # 项目 - web自动化？ - 一份大概的执行计划。
    为什么要做web自动化测试？接口自动化。
    自动化的目的：前置、步骤、期望结果() - 1点。写一份脚本 - 运行N遍 - 测试N次
    1 - 2个测试 - 10个功能 - 2天 - 上线频率：2周1次
    2 - 2个测试 - 100个功能 - 10天 - 上线频率：2周1次 - 所有功能都得测。
    50个功能 - 重复测试了50遍 - 同样的功能点点点。  -- 枯燥/重复/烦
    -- 重复工作，没有提升。
    -- 每次点的时候，不会覆盖所有的细节功能。
    -- 上线，历史功能出问题。

    尽量避免上线出问题  -- 客户反馈过的问题，适当加入自动化当中。
    解放双手、解放时间  -- 提高一个测试反馈效率。
    每次回归的功能都保持一致 -- 自动化的用例是什么，每次都运行的什么。

    项目周期比较长 - 历史功能(稳定)

    在开发后台接口的阶段，同步做接口自动化测试   -- 70% - 100%  (单接口 + 流程场景)
       -  团队的质量意识/单元测试/测试能力高/沟通要及时
     -- web自动化 - 最接近用户操作。-- 20%  -- 主流程 + 易实现的异常用例


4、用工具和框架的区别？

    # 项目实战  # 前程贷项目 - web自动化？ - 一份大概的执行计划。
    1、了解被测对象 - 业务需求。
    2、功能模块？1000功能用例 - 5大模块。  上线bug率最高的模块 - 核心模块 - 稳定的
    3、测试用例？500个功能用例 - 50-100个左右 主流程业务 + 易实现的异常用例。
    其它测试人员
    实现100个功能用例 - 自动化 -
    4、框架选型  -  自己写 - python+selenium+..... 2周
    整体的测试水平。1个人 - 由你最熟悉的技能来实现。  团队 - 工具(规范)
    框架 - 规定哪些层级里放什么,规定编写规则-文件命名/定位的规则/注释要求等，准备示范的例子。
      - 结构设计+规范。--管理、灵活扩展、维护工作量少
      - 尽早定期评审团队成员脚本  - 发现问题，解决问题，定规则。
    标准就是：较好的可读性、注释量要有以免回头看不懂写的啥。

5、实现脚本 - PO模式

    (1)、PO模式    PageObject

        测试用例 = 页面对象 + 测试数据
        测试用例与测试对象分离
        测试对象层：元素定位发生了变化？ 页面功能变化或者新增?
        测试用例层：用例步骤、用例数据、测试数据   变化

        目的：容易维护、容易扩展

    (2)、写web用例原则：

        1、稳定性最最最重要。可以牺牲时间来提高稳定性;
        2、用例要保持独立性。 不依赖于其他的用例运行结果；
        3、如果用例的流程很长，可以拆成几个用例，它就不独立。
        4、尽量少的依赖环境数据（在任何情况下，都自给自足，自己创建条件）

    (3)、分层设计思想：

        PageLocators - > PageObjects
        PageObjects - > TestCases
        TestDatas - > TestCases

        元素定位层
        页面对象层
        测试用例层
        测试数据层

    (4)、初衷和目的：解放双手，解放时间，提高反馈效果。
    (5)、应用场景：冒烟-(正常场景，不一定要有断言，能不能用？)
            回归-(全面覆盖，异常场景(准备工作很多，甚至需要人为干预))。

6、Pytest

    6.1、Pytest介绍
        基于unittest之上的单元测试框架
        (1)、自动发现测试模块和测试方法；
        (2)、断言使用assert+表达式即可;
        (3)、可以设置会话(从运行所有用例开始-用例结束)级，模块(.py)级，类级(setupClass/teardownClass)，
        函数(测试用例)级的fixtures，数据准备+清理工作
        (4)、有丰富的插件，300+以上。==allure
        (5)、测试用例不一定要放在测试类当中。
        安装命令：pip install pytest
        安装html报告插件：pip install pytest-html
        pytest插件地址：http://plugincompat.herokuapp.com/
        pytest收集测试用例的规则：
            (1)、默认从当前目录中收集测试用例，即在哪个目录下运行pytest命令，则从哪个目录当中搜索；
            (2)、搜索规则：
                a、符合命名规则，test_*.py 或者 *_test.py的文件；
                b、以test_开头的函数名；
                c、以Test开头的测试类，（没有__init__函数）当中，以test_开头的函数；
                d、断言使用基本的assert即可；
        Pytest的特点：
        1、简单灵活，容易上手，文档丰富；
        2、支持参数化，可以细粒度地控制要测试的测试用例；
        3、能够支持简单的单元测试和复杂的功能测试，还可以用来做selenium/appnium等自动化测试、
            接口自动化测试（pytest+requests）;
        4、pytest具有很多第三方插件，并且可以自定义扩展，比较好用的如pytest-selenium（集成selenium）、
            pytest-html（完美html测试报告生成）、pytest-rerunfailures（失败case重复执行）、pytest-xdist（多CPU分发）等；
        5、测试用例的skip和xfail处理；
        6、可以很好的和CI工具结合，例如jenkins

    6.2、pytest之mark功能
        mark机制  4.6
        先注册  pytest.ini  [pytest] markers=标签名:说明
        去给用例打标签
             @pytest.mark.已注册的标签名

             测试类和模块： 类下面设置类属性值，模块下面设置全局变量。
             pytestmarker=pytest.mark.已注册的标签名
             多个标签：pytestmarker=[pytest.mark.已注册的标签名,pytest.mark.已注册的标签名]

    6.3、pytest之命令运行用例

    6.4、pytest之fixture功能
        1、定义fixture
            1.1 创建了一个conftest.py文件
            1.2 在conftest中，创建fixture
            1.3 定义函数，函数前面加上@pytest.fixture(scope=作用域)
                函数内部：yield 隔开前置后后置的代码，之前是前置，之后是后置
                        yield 返回值（后面跟上返回值用于调用）
        2、调用fixture
            在测试用例.测试类 前面加上（@pytest.mark.usefixtures("fixture对应的函数名称")）；
            fixture对应的函数名称=它的返回值；
            fixture对应的函数名称作为测试用例的参数，将返回值传给测试用例；
            fixure  在conftest.py当中，定义的时候，就已经决定了他的用例域，决定了它的命运；
            fixture可以有很多个；
            无论在测试类、测试用例去主动调用fixture,都不能够改变它的命运；
            调用就是决定在哪儿去使用它。在哪个测试类？
            pytest的用例执行顺序：
               基本原则：按照搜索规则，先匹配到的先执行。
               1、文件名称：按名称名称顺序去搜索。先找到的，先去内部找用例。
               2、在py文件内部：按照代码顺序去找用例。先找到的先执行。
        3、fixture暂不支持与unittest同用，断言都用assert.
        4、pytest之fixture参数化-多运行，pytest层级覆盖。测试用例与其同级或者在其子目录
        5、fixture的scope参数
            scope参数有四种，分别是'function','module','class','session'，默认为function。
            function：每个test都运行，默认是function的scope
            class：每个class的所有test只运行一次
            module：每个module的所有test只运行一次
            session：每个session只运行一次
        6、setup和teardown操作
            setup，在测试函数或类之前执行，完成准备工作，例如数据库链接、测试数据、打开文件等
            teardown，在测试函数或类之后执行，完成收尾工作，例如断开数据库链接、回收内存资源等
            备注：也可以通过在fixture函数中通过yield实现setup和teardown功能

        7、fixture定义与调用
            定义  == 定命运。session、modle、class、function
            调用  == 你准备把它在哪儿用？
                session:整个会话都有效。
                module:模块内有效。
                class:类内有效。
                function:测试用例内有效。
                conftest.py文件。 === 定义多个fixture.

    6.5、pytest之参数化---ddt
        参数化  ddt   参数名 = 用例的参数名称
        @pytest.mark.parametrize("参数名",列表)
        @pytest.mark.parametrize("参数1，参数2",[(数1，数2),(数1，数2)])
        排列组合。多个参数的值排列组合。在一个用例前面 ，使用多个@pytest.mark.parametrize
        示例：用例有4个：0,2/0,3/1,2/1,3
            @pytest.mark.parametrize("x", [0, 1])
            @pytest.mark.parametrize("y", [2, 3])
            def test_foo(x, y):
                pass

    6.6、pytest之重运行

    6.7、pytest之HTML报告
        测试报告  = junitxml,html,allure
        1、先装插件
        2、命令行的参数：
           --html=相对路径/report.html   # 相对于pytest命令运行时，所在的根目录。
           --alluredir=相对路径
        3、安装allure命令行工具：下载，解压，配置环境变量
        4、生成allure文件之后，用命令：allure serve alluredir
        os.system("")
        allure与jenkins的集成、重运行机制、pytest中的失败截图。

    6.8、pytest之allure测试（allure测试报告）
         https://docs.qameta.io/allure/#_pytest
    6.9、pytest之jenkins持续集成


    # 用例识别规则

    # Mark 功能

    # fixture功能
        1、定义fixture
            1.1 创建了一个conftest.py文件
            1.2 在conftest中，创建fixture
            1.3 定义函数，函数前面加上@pytest.fixture(scope=作用域)
                函数内部：yield 隔开前置后后置的代码，之前是前置，之后是后置
                        yield 返回值（后面跟上返回值用于调用）
        2、调用fixture
            在测试用例.测试类 前面加上（@pytest.mark.usefixtures("fixture对应的函数名称")）
            fixture对应的函数名称=它的返回值
            fixture对应的函数名称作为测试用例的参数，将返回值传给测试用例

        3、fixture暂不支持与unittest同用，断言都用assert.

