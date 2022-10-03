
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

def main():
    web = 'https://www.bet365.com/#/AVR/B146/R^1/'
    options = Options()
    options.headless = True

    driver = uc.Chrome(version=106, options=options)
    driver.implicitly_wait(10)
    driver.get(web)
    driver.maximize_window()

    lst = driver.find_elements(By.XPATH, "vr-EventTimesNavBarButton")


    for i in lst:
        lst_time = i[-1].click()

        for odd in lst_time:
          team_odds = driver.find_element(By.CLASS_NAME, 'srb-ParticipantStackedBorderless_Odds')
          odds = [odd for odd in odds if odd  in team_odds]

          for n, odd in enumerate(odds[:3]):  # only the 3 first dropdowns
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

    df_bet365 = pd.DataFrame.from_dict(dict_gambling)
    df_bet365['Over/Under'] = df_bet365['Over/Under'].apply(lambda x: re.sub(',', '.', x))
    df_bet365 = df_bet365.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    output = open('df_bet365', 'wb')
    pickle.dump(df_bet365, output)
    output.close()
    print(df_bet365)




if __name__ == "__main__":
    main()