import time
from datetime import datetime
from pytz import timezone


print(time.localtime())
print(time.localtime().tm_year) # é a hora atual

#print(datetime.today())
#print(datetime.now().date())
#print(datetime.now().time())

dt_hr = datetime.now()
fuso_brasil = timezone('America/Sao_Paulo')
fuso_africa = timezone('Africa/Abidjan')

dthrSP = dt_hr.astimezone(fuso_brasil)  # puxa a data e hora do fuso
#dt_hr_formatada = dthrSP.strptime('%d /%m /%Y')   # permite que você formate qualquer data 

print(dthrSP)
#print(dt_hr_formatada)

#PRINT(HELP(RANGE)) #HELP MOSTRA O QUE A FUNÇÃO FAZ 
