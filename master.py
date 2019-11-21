import pandas as pd 
from datetime import datetime
from time import sleep
# supertrend15=pd.read_csv("supertrend15.csv")
supertrend5=pd.read_csv("supertrend5.csv")
minute=pd.read_csv("minute.csv")
ltp=pd.read_csv("minute.csv")
def masters():
    for x in range(0,len(ltp)):
        if str(datetime.now())[18] =='0' and str(datetime.now())[17]==0 and str(datetime.now())[15]/5==0:
            supertrends5=supertrend5['SuperTrend'][len(supertrend5["SuperTrend"])-1] 
        else:
            supertrends5=0
        if str(datetime.now())[18] =='0' and str(datetime.now())[17]==0 and str(datetime.now())[15]/15==0:
            supertrends15=supertrend5['SuperTrend'][len(supertrend15["SuperTrend"])-1]     
        else:
            supertrends15=0
        final=[supertrends15, supertrends5]
        final=pd.DataFrame(final)
        final.to_csv("master.csv")

while True:
    sleep(1)
    masters()