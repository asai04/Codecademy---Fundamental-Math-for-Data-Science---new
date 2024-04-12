import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data
# print(london_data.head())
# print(len(london_data))
temp = london_data['TemperatureC']
average_temp = np.mean(temp)
temperature_var = np.var(temp)
print(temperature_var)
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)
june = london_data.loc[london_data['month']==6]['TemperatureC']
july = london_data.loc[london_data['month']==7]['TemperatureC']
print('The mean temperature of june is ',np.mean(june),'and july is ',np.mean(july))
print('The standard deviation of temperature of june is ',np.std(june),' and july is ',np.std(july))
