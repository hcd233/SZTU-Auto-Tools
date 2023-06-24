import pandas as pd
from time import sleep


def getJWXTConfig():
    """
    get the account and password
    arouse exit code 114
    """
    while True:
        acc = input("JWXT Account: ")
        pwd = input("JWXT Password: ")
        check = input(f"Check again:[Y/N/Q]:\n\tAcc: {acc}\n\tPwd: {pwd}\n")
        while True:
            if check not in ["Y", "N", "Q"]:
                print(f"Invalid input: {check}")
            else:
                if check == "Y":
                    return acc, pwd
                elif check == "N":
                    print("Input Again.")
                    sleep(2)
                    break
                else:
                    exit(114)


def parseCatalogTable(_table: str):
    _table = _table.split("\n")[1:-1]
    _table = [td.split()[3:-1:2] for td in _table]
    _table = pd.DataFrame(_table)
    _table.columns = ["title", "begin_date", "end_date"]
    return _table


def parseSubCatalogTable(_sub_table: str):
    _sub_table = _sub_table.split("\n")[1:-1]
    _sub_table = [td.split()[1:-1] for td in _sub_table]
    for td in _sub_table:
        if len(td) > 6:
            td[1] = td[1] + td[2]
            del td[2]
        del td[-2]
    _sub_table = pd.DataFrame(_sub_table)
    _sub_table.columns = ["id", "course", "teacher", "type", "done"]
    return _sub_table


chinese_score_map = {
    1: [5] * 16 + [4],
    2: [4] * 16 + [5],
    3: [3] * 16 + [4],
    4: [2] * 16 + [3],
    5: [1] * 16 + [2],
}

germany_score_map = {
    1: [5] * 5 + [4, 1, 1],
    2: [4] * 5 + [5, 1, 1],
    3: [3] * 5 + [4, 1, 1],
    4: [2] * 5 + [3, 2, 2],
    5: [1] * 5 + [2, 3, 2],
}

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
