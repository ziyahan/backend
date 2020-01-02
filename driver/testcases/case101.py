from testcases.testCase import TestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Case101(TestCase):

    def __init__(self):
        TestCase.__init__(self)
        self.testCaseNum = 101

    def executeTest(self, webDriver):
	
        """ The aim of this test case is to understand which browser respect to standard`s definition related to base tag. Most of the major browsers do not obey to standards and do not mind order of base tag. According to standard that define HTML elements, it should be placed at the top of the document (between head elements) and helps browser to resolve following relative URLs to full URL. 
            When browsers don't mind the order of base tag, a malicious actor who can inject input into the page can hijack all relative URLs and force visitors to navigate to the site under his control.
            For more information, please look at the public disclosure written and sent to browser vendors by me.  https://docs.google.com/document/d/1LBbKMbmTaNnVLzCZqHaXcFqtBOrIIfM5M19xJciWHDg/edit
        """
        self.data = {}
        webDriver.get("http://basehref-hijacking.test-canitrust.com/basehref.html")
        WebDriverWait(webDriver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        anchorEl = webDriver.find_element_by_link_text("contact")
        anchorEl.click()
        data = { 'current_url': webDriver.current_url }
        self.data.update(data)
        return 1

    def evaluate(self):
        self.result=0
        print(self.data['current_url'])
        if self.data['current_url'].find('http://www.attacker.com')>=0:
         self.result = 1
        return self
