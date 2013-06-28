ghost-example
=============

Simple test for others to run to replicate possible 'bug' in GhostDriver


This test was created using OSX Lion but also occurs on Ubuntu 12.04

To get the test running you will need the following:

1. Python 2.7
2. PhantomJS
3. Selenium
4. Homebrew

Setup is simple (I would recomend using a virtualenv to keep things nice and tidy):

    pip install selenium
    brew install phantomjs

That should do it provided you have all the other stuff.  Now run the thest:

./tests/click_fail_test.py

You should get the following returned:

    Traceback (most recent call last):
    File "./tests/click_fail_test.py", line 27, in testClick
    self.driver.find_element_by_xpath("//div[@id='hmenus']/div/ul/li/a").click()
    File "/Users/emarty/.virtualenv/ghosttest/lib/python2.7/site-packages/selenium/webdriver/remote/webelement.py", line 54, in click
    self._execute(Command.CLICK_ELEMENT)
    File "/Users/emarty/.virtualenv/ghosttest/lib/python2.7/site-packages/selenium/webdriver/remote/webelement.py", line 228, in _execute
    return self._parent.execute(command, params)
    File "/Users/emarty/.virtualenv/ghosttest/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 165, in execute
    self.error_handler.check_response(response)
    File "/Users/emarty/.virtualenv/ghosttest/lib/python2.7/site-packages/selenium/webdriver/remote/errorhandler.py", line 158, in check_response
    raise exception_class(message, screen, stacktrace)
    WebDriverException: Message: u'Error Message => \'Click succeeded but Load Failed. Status: \'fail\'\'\n caused by Request => {"headers":{"Accept":"application/json","Accept-Encoding":"identity","Connection":"close","Content-Length":"81","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:53239","User-Agent":"Python-urllib/2.7"},"httpVersion":"1.1","method":"POST","post":"{\\"sessionId\\": \\"f195e730-e01e-11e2-88bd-83970cb36711\\", \\"id\\": \\":wdc:1372443428610\\"}","url":"/click","urlParsed":{"anchor":"","query":"","file":"click","directory":"/","path":"/click","relative":"/click","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/click","queryKey":{},"chunks":["click"]},"urlOriginal":"/session/f195e730-e01e-11e2-88bd-83970cb36711/element/%3Awdc%3A1372443428610/click"}' ; Screenshot: available via screen
