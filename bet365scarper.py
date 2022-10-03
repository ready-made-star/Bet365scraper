
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import pickle
import re
odds = []
teams = []
results = []


x12 = []
btts = []
over_under = []
odds_events = []

web = 'https://www.bet365.com/#/AVR/B146/R^1/'
options = Options()
options.headless = True

def main():
    euro()

    premiership()

    superleague()

    worldcup()

def premiership():

    driver = uc.Chrome(version=106, options=options)
    driver.implicitly_wait(10)
    driver.get(web)
    driver.maximize_window()

    type_of_play = driver.find_elements(By.CLASS_NAME,
                                        "vrl-MeetingsHeader_ButtonContainer vrl-HorizontalNavBarScroller_ScrollContent")

    for play in type_of_play:
        prm_ = play.find_elements(By.CLASS_NAME, "vrl-MeetingsHeaderButton_Title")
        for prm in prm_:
            prm_play = prm.find_element(By.XPATH, './/span[@text() = "Premiership"]').click()

            for prm_odds in prm_play:
                lst = prm_odds.find_elements(By.CLASS_NAME, "vr-EventTimesNavBarButton")

                for i in lst:
                    lst_time = i.find_element(By.CLASS_NAME, "vr-EventTimesNavBarButton")[-1].click()

                    for oddi in lst_time:
                        team_odds = oddi.find_element(By.CLASS_NAME, 'srb-ParticipantStackedBorderless_Odds')
                        odds = [odd for odd in odds if odd in team_odds]

                        for n, odd in enumerate(odds[:3]):
                            if n == 0:
                                x12.append(odd.text)
                                grandparent = odd.find_element(By.XPATH, './..').find_element(By.XPATH, './..')
                                teams.append(grandparent.find_element(By.CLASS_NAME,
                                                                      'srb-ParticipantStackedBorderless_Name').text)
                            if n == 1:
                                over_under.append(odd.text)
                            if n == 2:
                                btts.append(odd.text)

            driver.quit()
            pd.set_option('display.max_rows', 500)
            pd.set_option('display.max_columns', 500)
            pd.set_option('display.width', 1000)

            dict_gambling = {'Teams': teams, 'btts': btts,
                             'Over/Under': over_under, '3-way': x12}

            df_bet365_prm = pd.DataFrame.from_dict(dict_gambling)
            df_bet365_prm['Over/Under'] = df_bet365_prm['Over/Under'].apply(lambda x: re.sub(',', '.', x))
            df_bet365_prm = df_bet365_prm.applymap(lambda x: x.strip() if isinstance(x, str) else x)

            output = open('df_bet365_prm', 'wb')
            pickle.dump(df_bet365_prm, output)
            output.close()
def superleague():


    driver = uc.Chrome(version=106, options=options)
    driver.implicitly_wait(10)
    driver.get(web)
    driver.maximize_window()

    type_of_play = driver.find_elements(By.CLASS_NAME,
                                        "vrl-MeetingsHeader_ButtonContainer vrl-HorizontalNavBarScroller_ScrollContent")

    for play in type_of_play:
        super_ = play.find_elements(By.CLASS_NAME, "vrl-MeetingsHeaderButton_Title")
        for super in super_:
            super_play = super.find_element(By.XPATH, './/span[@text() = "Superleague"]').click()

            for super_odds in super_play:
                lst = super_odds.find_elements(By.CLASS_NAME, "vr-EventTimesNavBarButton")

                for i in lst:
                    lst_time = i.find_element(By.CLASS_NAME, "vr-EventTimesNavBarButton")[-1].click()

                    for oddi in lst_time:
                        team_odds = oddi.find_element(By.CLASS_NAME, 'srb-ParticipantStackedBorderless_Odds')
                        odds = [odd for odd in odds if odd in team_odds]

                        for n, odd in enumerate(odds[:3]):
                            if n == 0:
                                x12.append(odd.text)
                                grandparent = odd.find_element(By.XPATH, './..').find_element(By.XPATH, './..')
                                teams.append(grandparent.find_element(By.CLASS_NAME,
                                                                      'srb-ParticipantStackedBorderless_Name').text)
                            if n == 1:
                                over_under.append(odd.text)
                            if n == 2:
                                btts.append(odd.text)

            driver.quit()
            pd.set_option('display.max_rows', 500)
            pd.set_option('display.max_columns', 500)
            pd.set_option('display.width', 1000)

            dict_gambling = {'Teams': teams, 'btts': btts,
                             'Over/Under': over_under, '3-way': x12}

            df_bet365_superplay = pd.DataFrame.from_dict(dict_gambling)
            df_bet365_superplay['Over/Under'] = df_bet365_superplay['Over/Under'].apply(lambda x: re.sub(',', '.', x))
            df_bet365_superplay = df_bet365_superplay.applymap(lambda x: x.strip() if isinstance(x, str) else x)

            output = open('df_bet365_superplay', 'wb')
            pickle.dump(df_bet365_superplay, output)
            output.close()

def worldcup():
    

    driver = uc.Chrome(version=106, options=options)
    driver.implicitly_wait(10)
    driver.get(web)
    driver.maximize_window()

    type_of_play = driver.find_elements(By.CLASS_NAME,
                                        "vrl-MeetingsHeader_ButtonContainer vrl-HorizontalNavBarScroller_ScrollContent")

    for play in type_of_play:
        wc_ = play.find_elements(By.CLASS_NAME, "vrl-MeetingsHeaderButton_Title")
        for wc in wc_:
            wc_play = wc.find_element(By.XPATH, './/span[@text() = "World Cup"]').click()

            for wc_odds in wc_play:
                lst = wc_odds.find_elements(By.CLASS_NAME, ".vr-EventTimesNavBarButton")

                for i in lst:
                    lst_time = i.find_element(By.CLASS_NAME, ".vr-EventTimesNavBarButton")[-1].click()

                    for oddi in lst_time:
                        team_odds = oddi.find_element(By.CLASS_NAME, 'srb-ParticipantStackedBorderless_Odds')
                        odds = [odd for odd in odds if odd in team_odds]

                        for n, odd in enumerate(odds[:3]):
                            if n == 0:
                                x12.append(odd.text)
                                grandparent = odd.find_element(By.XPATH, './..').find_element(By.XPATH, './..')
                                teams.append(grandparent.find_element(By.CLASS_NAME,
                                                                      'srb-ParticipantStackedBorderless_Name').text)
                            if n == 1:
                                over_under.append(odd.text)
                            if n == 2:
                                btts.append(odd.text)

            driver.quit()
            pd.set_option('display.max_rows', 500)
            pd.set_option('display.max_columns', 500)
            pd.set_option('display.width', 1000)

            dict_gambling = {'Teams': teams, 'btts': btts,
                             'Over/Under': over_under, '3-way': x12}

            df_bet365_wc = pd.DataFrame.from_dict(dict_gambling)
            df_bet365_wc['Over/Under'] = df_bet365_wc['Over/Under'].apply(lambda x: re.sub(',', '.', x))
            df_bet365_wc = df_bet365_wc.applymap(lambda x: x.strip() if isinstance(x, str) else x)

            output = open('df_bet365_wc', 'wb')
            pickle.dump(df_bet365_wc, output)
            output.close()




def euro():


    driver = uc.Chrome(version=106, options=options)
    driver.implicitly_wait(10)
    driver.get(web)
    driver.maximize_window()

    type_of_play = driver.find_elements(By.CLASS_NAME,"vrl-MeetingsHeader_ButtonContainer vrl-HorizontalNavBarScroller_ScrollContent")

    for play in type_of_play:
        euro_ = play.find_elements(By.CLASS_NAME,"vrl-MeetingsHeaderButton_Title")
        for euro in euro_:
            euro_play = euro.find_element(By.XPATH,'.//span[@class = "Euro Cup"]').click()

            for euro_odds in euro_play:
             lst = euro_odds.find_elements(By.CLASS_NAME, "vr-EventTimesNavBarButton")


             for i in lst:
               lst_time = i.find_element(By.CLASS_NAME, "vr-EventTimesNavBarButton_Time")[-1].click()


               for oddi in lst_time:
                team_odds = oddi.find_element(By.CLASS_NAME, 'srb-ParticipantStackedBorderless_Odds')
                odds = [odd for odd in odds if odd  in team_odds]

                for n, odd in enumerate(odds[:3]):
                  if n == 0:
                      x12.append(odd.text)
                      grandparent = odd.find_element(By.XPATH, './..').find_element(By.XPATH, './..')
                      teams.append(grandparent.find_element(By.CLASS_NAME, 'srb-ParticipantStackedBorderless_Name').text)
                  if n == 1:
                      over_under.append(odd.text)
                  if n == 2:
                      btts.append(odd.text)

            driver.quit()
            pd.set_option('display.max_rows', 500)
            pd.set_option('display.max_columns', 500)
            pd.set_option('display.width', 1000)

            dict_gambling = {'Teams': teams, 'btts': btts,
                             'Over/Under': over_under, '3-way': x12}

            df_bet365_euro = pd.DataFrame.from_dict(dict_gambling)
            df_bet365_euro['Over/Under'] = df_bet365_euro['Over/Under'].apply(lambda x: re.sub(',', '.', x))
            df_bet365_euro = df_bet365_euro.applymap(lambda x: x.strip() if isinstance(x, str) else x)

            output = open('df_bet365_euro', 'wb')
            pickle.dump(df_bet365_euro, output)
            output.close()


if __name__ == "__main__":
    main()