from datetime import date, time, timedelta, datetime

data = date.today()
print(f'Data de hoje: {data}')

#adicionar 1 semana
data = data + timedelta(days=7)
print(f'Data daqui a 1 semana: {data}')

#Horas
hora = time(10, 30, 0)
print(hora)

# Data e hora
dataAtual = datetime.now()
print(f'Data e hora atual: {dataAtual}')


