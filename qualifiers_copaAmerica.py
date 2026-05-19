from wsgiref import headers
import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
url = f"http://www.sofascore.com/api/v1/team/4748/unique-tournament/295/season/53820/statistics/overall"
url2 = f"http://www.sofascore.com/api/v1/team/4748/unique-tournament/133/season/57114/statistics/overall"

try:
    res = requests.get(url, headers=headers)
    res2 = requests.get(url2, headers=headers)
    if res.status_code != 200 or res2.status_code != 200:
        print(res.status_code)
        print(res2.status_code)

    dataWcQualif = res.json()
    dataCopaAmerica = res2.json()
    print(f"✅")
    

except:
    print(res.status_code)

# transformar em tabela
dfWc = pd.DataFrame(dataWcQualif)
dfCopaAmerica = pd.DataFrame(dataCopaAmerica)

#ajustando tabela world cup qualifiers
dfWc = dfWc.T.reset_index(drop=True)
dfWc = dfWc.drop(columns=["statisticsType", "id"])
dfWc["competition"] = "WC Qualifiers"


#ajustando tabela copa america
dfCopaAmerica = dfCopaAmerica.T.reset_index(drop=True)
dfCopaAmerica = dfCopaAmerica.drop(columns=["statisticsType", "id"])
dfCopaAmerica["competition"] = "Copa America"
dfBrazilPerform26 = pd.concat([dfWc, dfCopaAmerica], ignore_index=True)

# exportar para excel
# dfBrazilPerform26.to_excel("brazil_performance_2026.xlsx", index=False)

df_favoritesAgainstMatchs = pd.DataFrame({
    "Adversário": ["França", "Espanha", "Argentina"],
    "Gols Marcados": [7, 7, 2],
    "Gols Sofridos": [5, 6, 7],
    "Vitórias": [2, 2, 0],
    "Derrotas": [3, 1, 4],
    "Empates": [0, 2, 1]
})
df_favoritesAgainstMatchs.to_excel("brazil_favorites_against_matchs.xlsx", index=False)