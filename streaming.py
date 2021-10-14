from copy import error
import pandas as pd
from faker import Faker
import random
from faker.providers import internet
from datetime import datetime

market1 = ['hammer', 'saw', 'clove', 'paste', 'drill',
           'circular saw', 'screw', 'rope', 'cement']
market2 = ['shoes', 'skirt', 'underwear', 'scarf',
           'socks', 'hat', 'T-Shirt', 'gloves', 'bikini']
market3 = ['dirt', 'flower', 'carrot seeds', 'Clove', 'Rope', 'Drill',
           'apple seeds', 'shovel', 'fertilizer', 'onion seeds']
market4 = ['PC', 'charger smartphone', 'headphones', 'cases', 'selfie stick',
            'Redmi Note 7', 'Redmi Note 8','Redmie Note 9s' ]
market5 = ['redmi note 7', 'redmi note 8', 'redmi note 9', 'Charger SmartPhone',
           'redmie note 9s', 'redmi 7', 'redmi 8', 'redmi 9']

cities = {
    1: ['Med', 'Me', 'MEDELLIN', 'MEDALLO', 'Tierra del aleteo'],
    2: ['Bog', 'Bo', 'BOGOTA', 'tierra de changua', 'Rololandia'],
    3: ['Car', 'Ca', 'CARTAGENA', 'erda', 'La Calor'],
    4: ['Lim', 'Li', 'Lima', 'paloma city', 'machupichu']
}

countries = {
    1: ['Col', 'Co', 'COLOMBIA', 'POLOMBIA', 'Pablito Escobar'],
    2: ['Per', 'Pe', 'PERU', 'Jaime', 'Palomas']
}


def getRandomProductByMarket(market):
    if market == 1:
        return market1[random.randint(0, len(market1)-1)]
    if market == 2:
        return market2[random.randint(0, len(market2)-1)]
    if market == 3:
        return market3[random.randint(0, len(market3)-1)]
    if market == 4:
        return market4[random.randint(0, len(market4)-1)]
    if market == 5:
        return market5[random.randint(0, len(market5)-1)]

# def getProductId(name):
#     if name in market1:
#         return market1.index(name)
#     if name in market2:
#         return market2.index(name) + len(market1)
#     if name in market3:
#         return market3.index(name) + len(market2) + len(market1)
#     if name in market4:
#         return market4.index(name) + len(market3) + len(market2) + len(market1)
#     if name in market5:
#         return market5.index(name) + len(market4) + len(market3) + len(market2) + len(market1)
#     raise Exception("Product not found")


def getProductId(name):
    if name in market1:
        return market1.index(name)+1
    if name in market2:
        return market2.index(name)+1
    if name in market3:
        return market3.index(name)+1
    if name in market4:
        return market4.index(name)+1
    if name in market5:
        return market5.index(name)+1
    raise Exception("Product not found")


def generate_market_batch(market):
    fake = Faker()
    data = []
    for i in range(1000):
        # market = random.randint(2, 5)
        product = getRandomProductByMarket(market)
        birthDate, date, devol, city, country, idClient, marketName, latitude, length = None, None, None, None, None, None, None, None, None
        if market == 1:
            date = fake.date()
            birthDate = fake.date()
        if market == 2:
            date = fake.date()
            date = date.replace('-', '/')
            birthDate = fake.date()
            birthDate = date.replace('-', '/')
        if market == 3:
            date = fake.date()
            date = date.replace('-', ' ')
            birthDate = fake.date()
            birthDate = date.replace('-', ' ')
        if market == 4:
            date = fake.date()
            date = date.replace('-', ',')
            birthDate = fake.date()
            birthDate = date.replace('-', ',')
        if market == 5:
            date = fake.date()
            date = date.replace('-', '.')
            birthDate = fake.date()
            birthDate = date.replace('-', '.')

        if market == 1 or market == 2:
            devol = 'X' if random.randint(1, 10) == 1 else ''
        else:
            devol = str(random.randint(1, 5)) if random.randint(
                1, 10) == 1 else str(0)
        rm = random.randint(1, 4)
        if market == 1:
            city = cities[rm][0]
            country = countries[2][0] if rm == 4 else countries[1][0]
        if market == 2:
            city = cities[rm][1]
            country = countries[2][1] if rm == 4 else countries[1][1]
        if market == 3:
            city = cities[rm][2]
            country = countries[2][2] if rm == 4 else countries[1][2]
        if market == 4:
            city = cities[rm][3]
            country = countries[2][3] if rm == 4 else countries[1][3]
        if market == 5:
            city = cities[rm][4]
            country = countries[2][4] if rm == 4 else countries[1][4]

        if rm == 1:
            latitude = 6.2441988
            length = -75.6
        if rm == 2:
            latitude = 4.648625
            length = -74.1
        if rm == 3:
            latitude = 10.4002813
            length = -75.5
        if rm == 4:
            latitude = -12.037964
            length = -77.0503238

        if market == 1 or market == 3:
            idClient = ''
        else:
            idClient = str(random.randint(1000000, 99999999))

        if market == 1:
            marketName = 'Tienda1'
        if market == 2:
            marketName = 'Tienda2'
        if market == 3:
            marketName = 'Tienda3'
        if market == 4:
            marketName = 'Tienda4'
        if market == 5:
            marketName = 'Tienda5'
        data.append([
            random.randint(1, 100000000),
            getProductId(product),
            product,
            random.randint(1, 100000000),
            date,
            devol,
            city,
            country,
            random.randint(1, 100000000),
            fake.email(),
            latitude,
            length,
            fake.name(),
            birthDate,
            random.randint(1, 1000),
            fake.name(),
            random.randint(1, 1000),
            random.randint(1, 1000),
            marketName
        ]
        )

    df = pd.DataFrame(data, columns=[
        'Order_Id',
        'Product_Id',
        'Product_Name',
        'User_Id',
        'Order_Date',
        'Return',
        'City',
        'Country',
        'Client_Id',
        'Client_Email',
        'Order_Latitude',
        'Order_Length',
        'Client_Name',
        'Birth_Day',
        'Deliver_Man_Id',
        'Name_Deliver_Man',
        'Product_Cost',
        'Product_Value',
        'Market_Name'
    ])

    datajson = df.to_json(orient='columns', index=False)

    # now = str(datetime.now())
    # now = now.replace(' ', '_')
    # now = now.replace(':', '_')
    # now = now.replace('.', '_')
    # now = now.replace('-', '_')
    # print("now =", now)

    # df.to_csv(f'market{market}_{now}.csv', index=False)

    # data es la variable que vas a usar y tiene los valores generados
    # inserte codigo de ingesta de kafka


# Funcion main que no se llama main pero jorge es muy Peruano y se enoja
generate_market_batch(1)
