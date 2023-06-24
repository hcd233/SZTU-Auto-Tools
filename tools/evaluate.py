import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import *

# urls
authUrl = "https://auth.sztu.edu.cn/idp/authcenter/ActionAuthChain?entityId=jiaowu"
iframe = "https://jwxt.sztu.edu.cn/jsxsd/xspj/xspj_find.do"


class EvaluatingSystem:
    def __init__(self, sep=0.5):
        # selenium
        opt = Options()
        opt.headless = False  # True

        self.sep = sep
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=opt)
        self.driver.minimize_window()
        self.current_score_maps = None
        self.PrintDoc()

    @staticmethod
    def PrintDoc():
        print(RED + "User Instructions\n" + RESET)
        print(YELLOW + "Copyright (C) [2023-] [Chengdong Huang]. All rights reserved.\n" + RESET)

        print(GREEN + '*' * 72 + RESET)

        print(GREEN + "Important Notice:" + RESET)
        print("Before using this program, you must read and comply with the following rules."
              "By using this program, you agree to accept these rules. "
              "If you do not agree with these rules, do not use this program.\n"
              )
        _ = input(RED + "Press Enter To Continue" + RESET)

        print(GREEN + "\nInstructions for Use:" + RESET)
        print(" This program will automatically score, "
              "but after the program has finished clicking, "
              "you must manually check the web page and click the 'Agree' button.\n"
              )
        _ = input(RED + "Press Enter To Continue" + RESET)

        print(GREEN + "\nDisclaimer:" + RESET)
        print("1. The scores entered by this program are not randomly generated, "
              "but are specified by the user, and the scores have nothing to do with this program.")
        print("2. The user is fully responsible for the results and consequences of using this program. "
              "The developer of this program disclaims all responsibility.")
        print("3. In the process of using this program, "
              "please ensure that your equipment and network connection are safe and stable, "
              "so as to avoid unnecessary mistakes.")
        print("4. This program will not modify any files in the user's computer system\n")
        _ = input(RED + "Press Enter To Continue" + RESET)

        print(GREEN + "\nReporting Issues:" + RESET)
        print("If you encounter any problems or need technical support, please contact us:"
              "\n\t- Email: lvlvko233@qq.com"
              "\n\t- GitHub: github.com/hcd233\n")
        print(GREEN + '*' * 72 + RESET)

        while True:
            user_input = input("Input 'I AGREE' to continue..[I AGREE/Q]").strip()
            if user_input == "I AGREE":
                return
            elif user_input == "Q":
                print(GREEN+"Nice Choice Maybe."+RESET)
                sleep(3)
                exit(0)
            else:
                print(f"Invalid Input: {user_input}")
                sleep(1)

    def Auth(self):
        """login the authorization page."""
        AccXpath = '//*[@id="j_username"]'
        PwdXpath = '//*[@id="j_password"]'
        LoginXpath = '//*[@id="loginButton"]'

        self.driver.minimize_window()
        acc, pwd = getJWXTConfig()

        self.driver.get(authUrl)
        self.driver.find_element(By.XPATH, AccXpath).send_keys(acc)
        self.driver.find_element(By.XPATH, PwdXpath).send_keys(pwd)
        self.driver.find_element(By.XPATH, LoginXpath).click()

    def getCatalog(self):
        """
        go to the main catalog
        arouse exit code 514
        """
        TableXpath = '//*[@id="Form1"]/table'

        self.driver.get(iframe)
        table = self.driver.find_element(By.XPATH, TableXpath).text
        table = parseCatalogTable(table)
        choices = list(map(str, range(len(table))))
        while True:
            print(table)
            table_idx = input(f"Choose from the table [{'/'.join(choices)}/Q]:")
            if table_idx in choices:
                if table["title"][eval(table_idx)][-4:] == "德国模式":
                    self.current_score_maps = germany_score_map
                else:
                    self.current_score_maps = chinese_score_map
                self.getSubCatalog(table_idx)
            elif table_idx == "Q":
                while True:
                    user_input = input(RED + "Remember save manually?"
                                             "[Press Enter will quit the program and close the browser]"+RESET)
                    time.sleep(5)
                    exit(514)
            else:
                print(f"Invalid Input: {table_idx}")

    def getSubCatalog(self, _table_idx):
        SubTableXpath = '//*[@id="Form1"]'

        if isinstance(_table_idx, str):
            _table_idx = eval(_table_idx)  # /html/body/div/div/form/table/tbody/tr[2]/td[8]/a
        sub_catalog = self.driver.find_element(By.XPATH, f'//*[@id="Form1"]/table/tbody/tr[{_table_idx + 2}]/td[8]/a') \
            .get_attribute("href")
        self.driver.get(sub_catalog)
        sub_table = self.driver.find_element(By.XPATH, SubTableXpath).text
        sub_table = parseSubCatalogTable(sub_table)
        print(sub_table, "\n")
        for course_idx in range(len(sub_table)):
            if sub_table["done"][course_idx] != "否":
                continue
            print(f"course: {sub_table['course'][course_idx]} teacher: {sub_table['teacher'][course_idx]}")
            self.evaluation(course_idx)
        time.sleep(2)
        self.driver.back()

    def evaluation(self, _course_idx):
        if isinstance(_course_idx, str):
            _table_idx = eval(_course_idx)

        course_catalog = self.driver.find_element(By.XPATH, f'//*[@id="dataList"]/tbody/tr[{_course_idx + 2}]/td[8]/a') \
            .get_attribute("href")

        self.driver.get(course_catalog)
        score_range = list(map(str, range(1, 6)))
        while True:
            score = input(f"Take a score for this course.[{'/'.join(score_range)}/Q]:")
            if score in score_range:
                self.takeScore(score)
                break
            elif score == "Q":
                return
            else:
                print(f"Invalid Input: {score}")

    def takeScore(self, _score):
        if isinstance(_score, str):
            _score = eval(_score)
            score_list = self.current_score_maps.get(_score)
            for idx in range(len(score_list)):
                self.driver.find_element(By.XPATH,
                                         f'//*[@id="table1"]/tbody/tr[{idx + 2}]/td[2]/label[{score_list[idx]}]').click()
            self.driver.find_element(By.XPATH, f'//*[@id="bc"]').click()
            self.driver.back()

    def run(self):
        self.Auth()
        sleep(self.sep)
        self.getCatalog()
        sleep(self.sep)

