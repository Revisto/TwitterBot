from selenium.webdriver.common.keys import Keys
from time import time
from time import sleep
import selenium
import random
Drive = selenium.webdriver.Chrome()
import pickle

class TwitterBot():
    
    def SaveCookieTwitter(UserName,Password):
        '''Drive.get("https://twitter.com/login?lang=en")
        sleep(5)
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input").send_keys(str(UserName))
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input").send_keys(str(Password))
        sleep(5)
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div").click()
        sleep(5)
        # login code'''
        pickle.dump(Drive.get_cookies() , open("TwitterCookies.pkl","wb"))

    def LogInTwitterByCookie(CookieName="TwitterCookies.pkl"):
        Drive.get('https://www.twitter.com')
        sleep(1)
        for cookie in pickle.load(open(CookieName, "rb")):
            Drive.add_cookie(cookie)
        sleep(5)
        print ("DONE Logging In")
        Drive.get('https://www.twitter.com')

    def LogIn(UserName,Password):
        Drive.get("https://twitter.com/login?lang=en")
        sleep(5)
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input").send_keys(str(UserName))
        
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input").send_keys(str(Password))
        
        sleep(5)
            
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div").click()
        
        sleep(5)
    def CheckLenghTweet(TextToBeChecked):
        if len(TextToBeChecked)<=280:
            return True
        else:
            return False
        
    def Tweet(Text):
        Drive.get("https://twitter.com/home")
        sleep(3)
        Extra=random.randint(1,220)
        Extra=chr(Extra)
        Text+=" "+Extra
        
        if not(TwitterBot.CheckLenghTweet(Text)):
            return "Limit Lengh --- It Must Be Maximum 280"
        
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div").send_keys(str(Text))
        
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]").click()
        
        sleep(5)
        
    def TweetWhenYouAreAtMainPage(Text):

        
        if not(TwitterBot.CheckLenghTweet(Text)):
            return "Limit Lengh --- It Must Be Maximum 280"
        
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div").send_keys(str(Text))
        
        Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]").click()
        
        sleep(5)
    def CreateTweetByHashTags():
        Text=""
        for i in range(15):
            Extra=random.randint(66,90)
            Extra=chr(Extra)
            Text+=" "+Extra
        return Text+"  "+"#نه_به_امتحان_حضوری"+" "+"#کمپین_سلامتی_دانش_آموزی"+" "+"#لغو_امتحانات_نهایی_حضوری "+"  ."
    
    def ScrollDown():
        body = Drive.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)
    
    def Retweet(HowManyReTweets,Delay):
        while (len(Drive.find_elements_by_class_name("r-xf4iuw"))//4)-len(Drive.find_elements_by_class_name("r-19ttmw8"))>=HowManyReTweets:
            TwitterBot.ScrollDown()
            sleep(1)
        
        print("Found Enough")
        print ("do SHit")
        sleep(5)
        for i in range (int(HowManyReTweets)):
            Number=i*4+2

            #Drive.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div["+str(Number)+"]/div/div/div/div/article/div/div[2]/div[2]/div[2]/div[3]/div[2]/div").click()
            
            Choices4=Drive.find_elements_by_class_name("r-11cpok1")
            Choices4[Number].click()
            sleep(1)
            print ((str(Drive.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div/div[2]/div/span").text)))
            print ("Haaaaa")
            if "ReTweet" in (str(Drive.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div/div[2]/div/span").text)):
                Drive.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div").click
            print ("DONE")
                

