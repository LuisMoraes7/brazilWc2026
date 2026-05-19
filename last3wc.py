import pandas as pd
from wsgiref import headers
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
urlwc2022 = "http://www.sofascore.com/api/v1/team/4748/unique-tournament/16/season/41087/statistics/overall"
urlwc2018 = "http://www.sofascore.com/api/v1/team/4748/unique-tournament/16/season/15586/statistics/overall"
urlwc2014 = "http://www.sofascore.com/api/v1/team/4748/unique-tournament/16/season/7528/statistics/overall"

try:
    res = requests.get(urlwc2022, headers=headers)
    res2 = requests.get(urlwc2018, headers=headers)
    res3 = requests.get(urlwc2014, headers=headers)
    if res.status_code != 200 or res2.status_code != 200 or res3.status_code != 200:
        print(res.status_code)
        print(res2.status_code)
        print(res3.status_code)

    dataWc2022 = res.json()
    dataWc2018 = res2.json()
    dataWc2014 = res3.json()
    print(f"✅")
except:
        print(res.status_code)

# df_Wc2022 = pd.DataFrame(dataWc2022)
# df_Wc2018 = pd.DataFrame(dataWc2018)
# df_Wc2014 = pd.DataFrame(dataWc2014)
# df_Wc2022 = df_Wc2022.T.reset_index(drop=True)
# df_Wc2022 = df_Wc2022.drop(columns=["statisticsType", "id"])
# df_Wc2022["year"] = "2022"
# print(df_Wc2022.head())

allWc = ["Wc2022", "Wc2018", "Wc2014"]
dfs = []
for i in allWc:
    data = globals()[f"data{i}"]
    globals()[f"df_{i}"] = pd.DataFrame(data)
    globals()[f"df_{i}"] = globals()[f"df_{i}"].T.reset_index(drop=True)
    globals()[f"df_{i}"] = globals()[f"df_{i}"].drop(columns=["statisticsType", "id"])
    globals()[f"df_{i}"]["year"] = f"{i[-4:]}"
    dfs.append(globals()[f"df_{i}"])

df_final = pd.concat(dfs, ignore_index=True)
df_final.to_excel("brazil_performance_last3wc.xlsx", index=False)