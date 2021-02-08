# Calling test methods defined in another class (ClassOfTests.py file)

from selenium import webdriver

driver = webdriver.Chrome()

from ClassOfTests import AllTests
mytest = AllTests (driver)

mytest.Test1()
mytest.Test2()
mytest.Test3()

