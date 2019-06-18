一、项目描述

    # web_auto_test
    这是一个基于Python的Selenium WebDriver项目。
    使用selenium和python语言，通过jenkins持续集成，以达到自动化构建项目，自动测试项目的结果。

二、项目中使用的技术简介

    1、安装Python和Selenium包
        安装Python：安装不同平台的Python可以在http://python.org/download/
        安装Selenium：pip3 install -U selenium
        PyCharm设置：使用社区版，配置Python的解释器
    2、Selenium WebDriver基于Python的实例脚本(Demo)
        1）从Selenium包导入WebDriver才能使用Selenium WebDriver的方法；
        2）选用一个浏览器驱动实例，会提供一个几口去调用Selenium命令来跟浏览器交互；
        3）设置10s隐式等待时间来定义Selenium执行步骤的超时时间；
        4）调用driver.get()方法访问该应用程序，方法调用后，WebDriver会等待，一直到页面加载完成才继续执行脚本；
        5）Selenium WebDriver提供多种方法来定位和操作这些元素，例如设置值，单击按钮，在下拉组件中选择选项等；
            这里使用find_element_by_id来定位搜索输入框；这个方法会返回第一个id属性值与输入参数匹配的元素；
            （HTML元素是用标签和属性定义的）
        6）通过send_keys()方法输入新的特定值，调用submit()提交搜索请求；
        7）加载搜索结果页面，我们读取结果列表的内容并打印输出；通过find_elements_by_xpath获取路径满足
            class='c-abstract'的所有div标签，它将返回多于一个的元素列表；
        8）最后我们打印，获取到的标签的文本内容；在脚本的最后，我们可以使用driver.quit()来关闭浏览器；
    3、使用unittest编写单元测试以及写Selenium WebDriver测试
        实现执行测试前置条件、测试后置条件，比对预期结果和实际结果，检查程序的状态，生成测试报告，创建数据驱动测试等功能；
        1）Test Fixture（测试夹具）：
            使用测试夹具，可以定义在单个或多个测试执行之前的准备工作和测试执行之后的清理工作；
        2）Test Case（测试用例）：
            unittest中执行测试的最小单元，通过验证unittest提供的assert方法来验证一组特定的操作和输入以后得到的响应；
            unittest提供了一个名为TestCase的基础类，可以用来创建测试用例；
        3）Test Suit（测试套件）：
            一个测试套件是多个测试或测试用例的集合，是针对被测程序的对应的功能和模块创建的一组测试，一个测试套件内的测试用例将一起执行；
        4）Test Runner（测试执行器）：
            测试执行器负责测试执行调度并且生成测试结果给用户；
            测试执行器可以使用图形界面、文本界面或者特定的返回值来展示测试执行结果；
        5）Test Report（测试报告）：
            测试报告展示所有执行用例的成功或者失败状态的汇总；包括失败的测试步骤的预期结果和实际结果，还有整体运行状况和运行时间的汇总；
        6）一般测试分为三个部分，即3A‘s
            ① Arrange：初始化前置条件，初始化被测试的对象，相关配置和依赖；
            ② Act：执行功能操作；
            ③ Assert：用来校验实际结果与预期结果是否一致；
    4、用TestCase类来实现一个测试
        1）我们将通过集成TestCase类并且 在测试类中为每一个测试添加测试方法来创建单个测试或者一组测试；
            测试用例使用excel维护，并且进行参数化，通过自定义context上下文管理的类，来操作excel，对excel中的参数进行匹配和替换；
        2）TestCase中的常用的assert方法，最主要的任务是：
            调用assertEqual()来校验结果；
            assertTrue()来验证条件；
            assertRaises来验证预期的异常；
            通过使用第三方库pymysql（Mysql）查询SQL，和TestCase的返回值，进行匹配校验；
            操作过程中重要的返回结果将通过调用logger来进行记录，以便快速定位问题；
        3）除了添加测试，还可以添加测试夹具，setUp()方法和tearDown()方法；
        4）一个测试用例是从setUp()方法开始执行，因此可以在每个测试开始前执行一些初始化的任务；此方法无参数，也无返回值；
        5）接着编写test方法，这些测试方法命名为test开头，这种命名约定通知test runner哪个方法代表测试方法；
        6）值得注意的是：test runner能找到的每个测试方法，都会在执行测试方法之前先执行setUp()方法，
            这样有助于确保每个测试方法都能够依赖于相同的环境；
        7）tearDown()方法会在测试执行完成之后调用，用来清理所有的初始值；
        8）最后就是运行测试：为了能通过命令行测试，我们可以在测试中添加对main方法的调用；
        9) 优化：为了能让各个测试方法共用一个实例，我们可以创建类级别的setUp()和tearDown()方法：
            1）通过setUpClass()方法和tearDownClass()方法及@classmethod标识来实现；
            2）这两个方法使在类级别初始化数据，替代了方法级别的初始化；
    5、学习unittest提供的不同类型的assert方法
        断言：unittest的TestCase类提供了很多实用的方法来校验预期结果和实际结果是否一致；以下为常用的集中断言方式：
        assertEqual(a, b [, msg]);
        assertNotEqual(a, b [, msg]);
        assertTrue(x [, msg]); assertFalse(x [, msg]);
        assertIsNot(a, b [, msg]);
        assertRaises(exc, fun, *args, **kwds);
    6、为一组测试创建TestSuite
        应用unittest的TestSuites特性，可以将不同的测试组成一个逻辑组，然后设置统一的测试套件，并通过一个命令来执行；
        具体通过TestSuites、TestLoader和TestRunner类来实现的；
        我们使用TestSuites类来定义和执行测试套件，将多可测试加到一个测试套件中；
        还用TestLoader和TextTestRunner创建和运行测试套件；
    7、使用unittest扩展来生成HTML格式的测试报告
    8、如何进行元素定位
        1）要搜索一个产品，需要先找到搜索框和搜索按钮，接着通过键盘输入要查询的关键字，最后用鼠标单击搜索按钮，提交搜索请求；
        2）Selenium提供了很多find_element_by方法定位页面元素，正常定位的话，相应的WebElement实例会被返回，
            反之将抛出NoSuchElementException的异常；
        3）8种find_element_by方法：
            ——find_element_by_id()
            ——find_element_by_name()
            ——find_element_by_class_name()
            ——find_element_by_tag_name()
            ——find_element_by_xpath()
            ——find_element_by_css_selector()
            ——find_element_by_link_text()#标签之间的文本信息
            ——find_element_by_partial_link_text()
        4）8种find_elements_by方法按照一定的标准返回一组元素：
            ——find_elements_by_id()
            ——find_elements_by_name()
            ——find_elements_by_class_name()
            ——find_elements_by_tag_name()
            ——find_elements_by_xpath()
            ——find_elements_by_css_selector()
            ——find_elements_by_link_text()
            ——find_elements_by_partial_link_text()
        5）值得一提的是class定位：class属性是用来关联CSS中定义的属性的；
            通过对元素ID、name、class属性来查找元素是最为普遍和快捷的方法；
            也可以增加一个测试用例断言元素的可用性：




附件 基础知识

    一、元素操作

    （一）、xpath复杂元素定位

        # 1、//标签名[@属性名称=属性值]   * 匹配所有
        # 2、逻辑运算 and or  //标签名[@属性名称=属性值 and 属性名称=属性值]
        # 3、元素的文本内容  //标签名[text()="元素的文本内容"]  # 文本内容完全匹配
        # 4、部分匹配：文本内容/属性值   contains(text()/@属性,部分值)
        #  //标签名[contains(text(),"部分文本内容")]  # 太长了
        #  //标签名[contains(@属性,"部分属性值")]   # id(不变动+变动) # class有多个。
        # 5、当你不能通过自己的属性唯一找到的时候，就要利用层级关系 。
        # 5.1、层级定位  第一种方式
        #   后一条件，是在前一个得到的结果之内去搜索。//条件1//条件2.....
        #  //div[@id="u1"]//a[@name="tj_login"]
        # 5.2 层级定位 - 轴定位    # 表达式   /轴定位名称::标签名[属性表达]
            # 兄弟姐妹  -  直系的   有比你大的，有比你小的。
            # preceding-sibling: 哥哥姐姐
            # following-sibling：弟弟妹妹
            # //a[@name="tj_trvideo"]/following-sibling::a[@name="tj_login"]
            # //a[@name="tj_settingicon"]/preceding-sibling::a[@name="tj_login"]
            # 爸爸：parent   祖先：ancestor
            # //a[@name="tj_trtieba"]/parent::div/a[@name="tj_login"]
            # //a[text()="百度首页"]/parent::div/following-sibling::div//a[@name="tj_login"]

    （二）、等待-三种等待方式

        1、强制等待
            sleep(秒)
        2、隐性等待
            implicitly_wait(秒)
            设置最长等待时间，在这个时间内加载完成，则执行下一步。
            整个driver的会话周期内，设置一次即可，全局都可以使用。
        3、显性等待
            明确等到某个条件满足之后，再去执行下一步操作。
            程序每隔XX秒看一眼，如果条件成立了，则执行下一步，否则继续等待，知道超过设置的最长时间，
            抛出TimeoutException.--

            WebDriverWait类，显性等待类；
            WebDriverwait(dirver,等待市场，轮询周期).until/until_not()

            expected_conditions模块：提供一系列期望发生的条件。
            presence_of_element_located:元素存在
            visibility_of_element_located:元素可见
            element_to_be_clickable:元素可点击
            ps:这个类有很判断方法。

        例如：
            1、当你的操作带来了页面的变化，请一定要等待
            time.sleep(5)#傻等
            2、隐形等待-智能等待：如果你10秒出现了，我就开始下一步操作。设置上限：30秒 超时TimeoutException
            3、显性等待-智能等待：明确的条件（元素可见，窗口存在）。等待+条件
            （如果你10秒出现了，我就开始下一步操作。）
                from selenium.webdriver.support.wait import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC
                from selenium.webdriver.common.by import By
            元素存在（html里面，能找到）；
            元素可见（存在并且可见-看得见大小-可见才可操作）；
            元素可用（可见之后，才有可用的可能性。只读/不可点击-不可用）
            等待条件表达
            locater = (定位类型，定位表达式)
                locater = (By.ID,'TANGRAM__PSP_10__footerULoginBtn')
            EC.visibility_of_element_located(locater) #条件
            等待元素可见
                WebDriverWait(driver,30).until(EC.visibility_of_element_located(locater))
            使用sleep短暂等待，辅助- 0.5秒
                time.sleep(0.5)
            点击元素
                driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()

    （三）、打开新窗口部分核心代码
        1、
            #step1:获取窗口数
            handles = driver.window_handles # >>> 只有一个 窗口
            # step2:打开新窗口的操作
            driver.find_element(*locator).click()   #本操作带来新窗口的出现  >>> 2个窗口

            ############ 第二种 ###########
            # step3:确认新窗口出现了，我再去操作他，等待新窗口出现
            # EC.new_window_is_opened # 比窗口总数的大小  # 传一个窗口的总数
            WebDriverWait(driver,10).until(EC.new_window_is_opened(handles))   #2>1 确认新窗口出现
            # step4:再次获取 窗口的handles
            handles = driver.window_handles
            # step5:切换 新的窗口
            driver.switch_to.window(handles[-1])
        2、
            driver.find_element(*locator).click()   #本操作带来新窗口的出现
            # 打开新的窗口
            #   1、获取所有的窗口
            handles = driver.window_handles
            print(driver.window_handles)
            #   当前窗口的handle
            print(driver.current_window_handle)
            #   2、切换新的窗口
            driver.switch_to.window(handles[-1])
            print("切换之后的窗口为：",driver.current_window_handle)


    二、项目实战+框架

    （一）、自动化应用场景和用例设计
        1、PO模式--项目  100个web用例 -10个py
            a、元素定位发生了变化...找到元素到底在那些文件当中，需要修改
            b、相同功能-找到哪些地方用到了这些功能
    （二）、PO模式　　PageObject

        测试用例 = 页面对象 + 测试数据
        测试用例与测试对象分离。分层设计　   
        测试对象层：元素定位发生了变化？页面功能变化或者新增？
        测试用例层：用例步骤＼用例数据＼测试数据　变化　   
        容易维护，容易扩展
     
        写web用例的原则：

            1、稳定性最最最重要的。可以牺牲时间来提高稳定性；
            2、用例要保持独立性。不依赖于其它的用例运行结果。
            3、如果用例的流程很长，可以拆成几个用例，它就不独立。 -- 主流程
               申请人 - 审核1 - 审核2 - 审核3
            4、尽量少的依赖环境数据（在任何情况下，都自给自足，自己创建条件）

        PageLocators -> PageObjects
        PageObjects -> TestCases
        TestDatas  ->  TestCases
        元素定位层
        页面对象层
        测试用例层
        测试数据层
        分层设计思想
    
        初衷和目的，应用场景
        
            初衷和目的：解放双手，解放时间，提高反馈效果。
            应用场景：冒烟-(正常场景，不一定要有断言。能不能用？)、
                      回归-(全面覆盖 -异常场景)
                      (准备工作很多很麻烦，清理工作也很多，甚至需要人为干预。稳定性差)
            














