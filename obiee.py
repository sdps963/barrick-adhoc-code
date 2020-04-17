from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class obiee:
    """Class for scraping OBIEE GUI"""

    def __init__(self, chromedrive, url, user, password,reportName):
        self.chromedriver = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.url = url
        self.user = user
        self.password = password
        self.reportName = reportName

    def get_url(self):
        self.driver.get(self.url)
        self.login()

    def login(self):
        self.driver.find_element_by_id("sawlogonuser").send_keys(self.user)
        self.driver.find_element_by_id("sawlogonpwd").send_keys(self.password, Keys.ENTER)
        time.sleep(10)
        self.search_report()

    def search_report(self):
        self.driver.find_elements_by_id("idHeaerQuickSearchNameInput")[0].send_keys(self.reportName, Keys.ENTER)
        time.sleep(5)
        self.driver.find_elements_by_xpath('//*[@id="idCatalogItemsAccordion"]/div[1]/div[2]/table/tbody/tr/td/div/table/tbody/tr[3]/td/table/tbody/tr/td[3]/a')[0].click()
        time.sleep(5)
        self.dropdown()

    def dropdown(self):

        """ this method needs little bit of manually updates according to the webpage"""

        for A in range(1,6):

            #if A ==1:

            self.driver.find_element_by_xpath('/html/body/div[8]/div/table[1]/tbody/tr[1]/td[2]/div/table[1]/tbody/tr/td[2]/div[1]/div[2]/table/tbody/tr/td[1]/div/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div/div/div/table/tbody/tr/td/div/form/div/table/tbody/tr[2]/td/table/tbody/tr/td['+str(A)+']/table/tbody/tr/td/table/tbody/tr[2]/td/span/span/div/div[1]/img').click()
            time.sleep(2)
            listt = self.driver.find_element_by_css_selector('body > div.floatingWindowDiv > div > div.masterMenu.DropDownValueList').find_elements_by_tag_name("input")
            num = len(listt)
            lists = ['/html/body/div[9]/div/div[2]/div[4]/div/input', '/html/body/div[9]/div/div[2]/div[7]/div/input']
            for x in range(1,num+1):
                self.driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div['+str(x)+']/div/input').click()
            self.driver.find_element_by_xpath('/html/body/div[8]/div/table[1]/tbody/tr[1]/td[2]/div/table[1]/tbody/tr/td[2]/div[1]/div[2]/table/tbody/tr/td[1]/div/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div/div/div/table/tbody/tr/td/div/form/div/table/tbody/tr[2]/td/table/tbody/tr/td['+str(A)+']/table/tbody/tr/td/table/tbody/tr[2]/td/span/span/div/div[1]/img').click()
        self.driver.find_element_by_xpath('/html/body/div[8]/div/table[1]/tbody/tr[1]/td[2]/div/table[1]/tbody/tr/td[2]/div[1]/div[2]/table/tbody/tr/td[1]/div/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div/div/div/table/tbody/tr/td/div/form/div/table/tbody/tr[2]/td/table/tbody/tr/td[6]/input').click()
        time.sleep(15)
        self.driver.find_element_by_xpath('/html/body/div[8]/div/table[1]/tbody/tr[1]/td[2]/div/table[1]/tbody/tr/td[2]/div[1]/div[2]/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/div/div/table/tbody/tr/td[5]/a').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#popupMenuItem > table > tbody > tr > td.MenuItemRightArrowCell').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[contains(text(), 'CSV Format')]").click()

    def select_all(self):
        self.driver.find_element_by_css_selector(
            'body > div.floatingWindowDiv > div > div.masterMenu.DropDownSearch > span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[10]/div/table/tbody[1]/tr/td/div[2]/div/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td').click()

if '__main__' == __name__:
    chromedriver = "C:/Users/dsaladi/Desktop/alertapp/BarrickGoldStrike_Root/chromedriver_win32 (2)/chromedriver"
    url = "http://usaglbobip1.goldbar.barrick.com:9502/analytics/saw.dll?bieehome&startPage=1"
    user = ''
    password = ''
    reportName="Barrick Sub-Ledger Reporting"
    x = obiee(chromedriver, url, user, password, reportName)
    x.get_url()

