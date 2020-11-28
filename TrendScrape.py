from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
import time

class TrendScraper():

    def __init__(self):
        # options for selenium
        self.options = Options()
        self.options.headless = True  # make the driver headless so that it does not require a browser window

        # path that we want selenium to download file to
        self.downloadPath = 'C:\\Users\\charl\\Desktop\\GoogleTrendMonitor'

        # initializing the webdriver with the executable path of geckodriver
        self.profile = FirefoxProfile()
        self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'text/csv')
        self.profile.set_preference("browser.download.manager.showWhenStarting", False)
        self.profile.set_preference("browser.download.dir", self.downloadPath)
        self.profile.set_preference("browser.download.folderList", 2)

        print("Starting WebDriver")
        self.driver = webdriver.Firefox(options=self.options, firefox_profile=self.profile, executable_path='C:\\Users\\charl\\Desktop\\GoogleTrendMonitor\\geckodriver.exe')

        self.scanStarted = False

        self.initializeWebPage()

    """ Google will deny our first request until we refresh the page.
        do that here."""
    def initializeWebPage(self):
         # launch the driver
        self.driver.get('https://trends.google.com/trends/explore?date=now%201-H&geo=US-NJ-501&q=stock')

        # Wait 10 seconds to ensure that the webpage loads completely
        time.sleep(10)

        self.refreshPage()

        # make sure the site loads completely
        time.sleep(10)

    def getRelatedData(self):

        self.relatedData = []

        self.relatedDataEntry = []

        # all of these xpaths correspond to each related topic on the trend page
        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[1]/div/ng-include/a/div/div[2]')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/\
    div/div[4]/trends-widget/ng-include/widget/div/div/ng-include/div/div[1]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 1st related element")

        self.relatedDataEntry = []

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[2]/div/ng-include/a/div/div[2]/span')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[2]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 2nd related element")

        self.relatedDataEntry = []

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[3]/div/ng-include/a/div/div[2]/span')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[3]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 3rd related element")

        self.relatedDataEntry = []

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[4]/div/ng-include/a/div/div[2]/span')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[4]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 4th related element")

        self.relatedDataEntry = []

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[5]/div/ng-include/a/div/div[2]/span')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[5]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 5th related element")

        # select the next arrow and click it

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/trends-widget/ng-include/widget/div/div/ng-include/div/div[6]/pagination/div/button[2]/md-icon')
            self.relatedElement.click()
        except:
            print('failed to get next arrow element')

        self.relatedDataEntry = []

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[1]/div/ng-include/a/div/div[2]')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/\
    div/div[4]/trends-widget/ng-include/widget/div/div/ng-include/div/div[1]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 6th related element")

        self.relatedDataEntry = []

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[2]/div/ng-include/a/div/div[2]/span')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[2]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 7th related element")

        self.relatedDataEntry = []

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[3]/div/ng-include/a/div/div[2]/span')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[3]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 8th related element")

        self.relatedDataEntry = []

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[4]/div/ng-include/a/div/div[2]/span')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[4]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 9th related element")

        self.relatedDataEntry = []

        try:
            self.relatedElement = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[5]/div/ng-include/a/div/div[2]/span')
            self.relatedDataEntry.append(self.relatedElement.text)
            self.relatedElementRisingValue = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[4]/\
    trends-widget/ng-include/widget/div/div/ng-include/div/div[5]/div/ng-include/a/div/div[3]')
            self.relatedDataEntry.append(self.relatedElementRisingValue.text)

            self.relatedData.append(self.relatedDataEntry)
        except:
            print("Could not get 10th related element")

            
        return self.relatedData
        

    def refreshPage(self):
        self.driver.refresh()

    def closeDriver(self):

        self.driver.quit()

    def startScan(self):

        self.scanStarted = True
        while(self.scanStarted):
            # refresh the page
            self.driver.refresh()
            # wait for a minute for everything to load
            time.sleep(5)
            # click to save csv file
            print(self.getRelatedData())

    def stopScan():
        self.scanStarted = False

    def processCsvFile():
        pass


if __name__ == "__main__":
    tScraper = TrendScraper()
    tScraper.startScan()
