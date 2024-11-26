from wolframalpha import Client

app_id = '2ARWPW-8GAHYH5HQH'


dist_km = 305.3
distMiles = round(dist_km / 1.60934, 1)


client = Client(app_id)
res = client.query('distance between Poltava and Kiev in miles')
correct = float(next(res.results).text.split(' ')[0])

if distMiles == correct:
    print('Все правильно! Ви молодець!')
else:
    print(f"Щось не те - має вийти {correct} миль, а у Вас вийшло {distMiles}!")
