import unittest
import os
import sys
from appium import webdriver



class AppiumAndroidTests(unittest.TestCase):
    "Class to run tests against the Chess Free app"
    def setUp(self):
       desired_caps = {}
       desired_caps['platformName'] = 'Android'
       desired_caps['platformVersion'] = '6.0.1'
       desired_caps['appPackage'] = 'io.selendroid.testapp'
       desired_caps['appActivity'] = '.HomeScreenActivity'
       desired_caps['deviceName'] = 'ZY222ZPZVW'
       desired_caps['app'] = 'C:\\Users\\alam\\Downloads\\selendroid-test-app-0.17.0.apk'

       self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_first(self):
        search_input=self.driver.find_element_by_xpath("//android.widget.EditText[@content-desc='my_text_fieldCD']")
        search_input.send_keys("Appium")


# iOS environment
'''import unittest
from appium import webdriver

desired_caps = {}
desired_caps['app'] = PATH('../../apps/UICatalog.app.zip')

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)'''