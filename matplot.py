import matplotlib.pyplot as plt

days = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ]
tempreture = [20, 24, 23, 35, 19, 15, 29]

plt.plot (days, tempreture, marker = '0')
plt.title ('tempreture for the week')
plt.xlabel('days of the week')
plt.ylabel('tempretures in celcius')
plt.grid(True)
plt.show()

