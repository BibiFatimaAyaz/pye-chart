#___________PYE.CHART_____________
import matplotlib.pyplot as plt

exp_values=[5000,1400,3000,8000,500]
exp_labels=['BIKE','CAR','RIQSHAW','CHINCHI','TEXI']

plt.pie(exp_values,labels=exp_labels,autopct='0.2f%%',radius=1,explode=[0,0,0,0.05,0],startangle=45)
plt.show()
