vnd, usd_rate, eur_rate = map(float, input().split())
print("USD:", round(vnd / usd_rate, 2))
print("EUR:", round(vnd / eur_rate, 2))