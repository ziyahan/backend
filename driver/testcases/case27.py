# ------------------------------------------------------------------------------------------------
#  Copyright (c) mgm security partners GmbH. All rights reserved.
#  Licensed under the AGPLv3 License. See LICENSE.md in the project root for license information.
#-------------------------------------------------------------------------------------------------

from testCase import TestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class Case27(TestCase):

    def __init__(self):
        TestCase.__init__(self)
        self.testCaseNum = 27

    def executeTest(self, webDriver):
        """ Definition of a testcase
            Test result MUST be set to self.data
        """
        self.data = {}
        webDriver.get("https://xss1.test-canitrust.com/xss_get.php?payload=%3Cscript%3Edocument.getElementById(%22headline%22).innerHTML=%22XSS%20exploited%22%3C/script%3E")
        # server returns x-xss-protection header with value: 1; mode=block
        try:
            WebDriverWait(webDriver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            oHeadline = webDriver.find_element_by_id('headline')
            textHeadline = str(oHeadline.get_attribute('innerHTML'))
            if (textHeadline == "XSS exploited"):
                self.data = {'XSS': "exploited"}
            else:
                self.data = {'XSS': "filtered"}
        except:
            self.data = {'XSS': "page blocked"}
        webDriver.close()
        return 1  

    def evaluate(self):
        # 
        if ('exploited' in self.data['XSS']):
            # no XSS protection, XSS exploited
            result = 7 # orange
        if ('filtered' in self.data['XSS']):
            # successful XSS protection, page loaded
            result = 5 # blue
        if ('page blocked' in self.data['XSS']):
            # entire page blocked
            result = 6 # yellow
        self.result = result
