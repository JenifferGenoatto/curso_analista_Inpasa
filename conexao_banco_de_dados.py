import pandas as pd
import oracledb
import getpass

user = 'ADMIN'
dsn = 'treinamentoinpasa_high'
pw = '14297301tnMS'
wallet_pw = '2410OU2501ja'

config_dir = 'C:/Users/jeniffer.vanzin/Documents/CURSO_ANALISTA_DADOS/Wallet Treinamento Inpasa'
wallet_location = 'C:/Users/jeniffer.vanzin/Documents/CURSO_ANALISTA_DADOS/Wallet Treinamento Inpasa'

connection = oracledb.connect(user=user, password=pw, dsn=dsn,
                            config_dir=config_dir,
                            wallet_location=wallet_location, wallet_password=wallet_pw)

with connection.cursor() as cursor:
    sql = "SELECT * FROM EXCHANGERATES"
    df_exchange = pd.read_sql(sql, con=connection)
    for row in cursor.execute(sql):
        print(row)

connection.close()


COCOA ok
COFFEE ok
COTTON ok
CUSTOMERS ok
EXCHANGERATES
LUMBER
ORANGE_JUICE
PRODUCTS
SALES
STORES
SUGAR



Delivery Date New =     [Delivery Date] = null then [Order Date] else [Delivery Date])





Adiantamento para despesas com viagem para apoio no setor de Manutenção da Inpasa Sinop/MT e Nova Mutum/MT (09/11 a 18/11)



