
#from testrun import Test
import csv

import pandas as pd
import pandas as pd
f= open("Data.txt","w+")
f.close()
Ano_score =Ano= []
windo =win= []
#win= []
whole = []
step =st= []
#st= []
data = []

def Simple():
	if len(windo) > 0 & len(step)>0:
				Test(int(sum(windo)/len(windo)),int(sum(step)/len(step)),Ano_score)
	print("\n Hello \n")

'''
field = ['window', 'Steps', 'Anomaly']
with open("Data.csv", "w") as f:	 
		write = csv.writer(f)
		write.writerow(field)'''
def Test(arg0,arg1,arg2):
	if arg > 1000:
		win.append(arg0)
	elif arg > 120:
		st.append(arg1)
	else:
		Ano.append(arg2)
	df = pd.DataFrame({'Window_Size':win,
		'Step_Size':st,
		'Anomaly_Score':Ano})
	print("\nDataFrame = ",df,"\n")
class Data_gather():
	def __init__(self, *args, **kwargs):
		super(Data_gather, self)
		#self.Ano_score= Ano
		#self.windo = Win
		#self.step = st
		#Ano_score.append(value)
		#print( "Anovva = ", Ano_score)
	def Anomaly(value):
		if value not in Ano_score:
			Ano_score.append(value)
			data = Ano_score
			print("\n  Ano_score = ",Ano_score)
			Simple()
			f2= open("Anomaly_Score.txt","a+")
			f2.write("%d \n " %value)
			f2.close()			#Two_factor_anova()
			#update(data)
	def window(val):
		if val not in windo:
			windo.append(val)
			#print("\n Win = ",windo)
			win = windo
			 
			f= open("Window_Size.txt","a+")
			f.write("%d \n " %val)
			f.close()

			#with open('Data.csv','a') as fd:
			#	fd.write(str(val))
			#data.append(windo)
	def Step_Size(val1):
		if val1 not in step:
			step.append(val1)
			#print("\n Step = ",step)
			st = step
			f1= open("Step_Size.txt","a+")
			f1.write("%d \n" %val1)
			f1.close()
			#data.append(step)
			#print("\n Data = ",data)
			#Test.Win_step(data)
		#df = pd.DataFrame({'window':windo,'step':step,"Ano_score":Ano_score})
		#print(pd.head())
		#print(set(data))


		# Importing library 
	
	# data to be written row-wise in csv fil 
	
	# opening the csv file in 'w+' mode 
	
	def Two_factor_anova(df):
		
		win_m =df.window.mean()
		step_m = df.step.mean()
		Ano_m = df.Ano_score.mean()
		print("Mean of window : ",win_m)
		print("Mean of step : ", step_m)
		print("Mean of Ano_m : ", Ano_m)
		overall = (win_m + step_m+ Ano_m)/3
		# SST
		lis = ['window', 'step', 'Ano_score']
		sst = ((overall-df[lis])**2).sum()
		print("SST value= ",sst)

		#SSC
		ssc_list = [win_m, step_m, Ano_m]
		for i in ssc_list:
		  ssc0 = ssc0+(overall-i)**2
		print("SSC value = ",ssc0)

		# SSB
		ssb0 = ((AK_df.R_mean - overall)**2).sum()
		print("SSB value = ",ssb0)

		print(sst,"\n", ssc0,"\n \t", ssb)
		err = sst - ssc0 -ssb
		print("Error = ",err)

