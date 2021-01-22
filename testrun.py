import os



import pandas as pd
from Data.Text import Data_gather
Win = []
st=[]
An = []
n=int(input("\n Enter number of iterations: "))
for i in range(n):
	os.system('python run.py -d jibina')
	
	f0 = open("Window.txt", "a")
	f = open("Window_Size.txt", "r")
	m =int(f.readline())
	f0.write("%s \n"%m)
	f.close()
	f0.close()

	f0 = open("Step.txt", "a")
	f = open("Step_Size.txt", "r")
	m = int(f.readline())
	f0.write("%d \n"%m)
	f.close()
	f0.close()

	if os.path.exists("Window_Size.txt"):
		os.remove("Window_Size.txt")
	if os.path.exists("Step_Size.txt"):
		os.remove("Step_Size.txt")




#Data_gather.Two_factor_anova()
class Test(object):
	"""docstring for Test"""
	def __init__(self, arg):
		super(Test, self)
		self.data = 0
		self.data = arg
	def Win_step(val):
		a2 = np.array(val)
		window_list = []
		window_list=a2[:1]
		window = window_list.mean()
		step_list = []
		step_list = a2[1:2]
		step = step_list.mean()
		Res(window,step,self.data)
	def Res(window, step, ano):
		win.append(window)
		st.append(step)
		An.append(ano)
		df = pd.DataFrame({'window':win,
			"Step":st,
			"Anomaly":An})
		print(df)
		#Anova.Two_factor_anova(df)
