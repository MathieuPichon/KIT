from model import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

steamConPattern1 = np.array([[x for x in range(24)],
                        [5 for x in range(24)]]) # expressed in steam tons
steamConPattern2 = np.array([[10 for x in range(24)],
                    [5, 5, 5, 5, 5, 5, 5, 5, 15, 15, 25, 25, 25, 25, 15, 15, 5, 5, 5, 5, 5, 5, 5, 5],
                    [5, 5, 10, 20, 20, 10, 5, 5, 5, 5, 10, 20, 20, 10, 5, 5, 5, 5, 10, 20, 20, 10, 5, 5,]])
renewablePattern = np.array([0, 0, 0, 0, 5, 5, 5, 5, 15, 15, 30, 30, 30, 30, 15, 15, 5, 5, 5, 5, 0, 0, 0, 0])
renewablePattern = renewablePattern * 3
facto_model = FactoryModel(3, steamConPattern2, renewablePattern, 20)
for i in range(2000):
    facto_model.step()

totalCon = facto_model.datacollector.get_model_vars_dataframe()
totalCon.plot(y=["GenLevel","RampLevel"])
plt.show()

patternEvo = facto_model.datacollector.get_agent_vars_dataframe()
# print(patternEvo[:24])
# print(patternEvo.info())
# print(patternEvo.index)
newPatternEvo = patternEvo.reset_index(level=['AgentID'])
# print(newPatternEvo.info())
# print(newPatternEvo.index)
# print(newPatternEvo.columns)
# newPatternEvo.set_index('Step', inplace=True)
newPatternEvo.groupby('AgentID')['patternChoice'].plot(legend=True)
# print(newPatternEvo[:24])
# newPatternEvo.plot()
plt.show()

absRamp = np.sum(abs(totalCon[totalCon >=0]))
print(absRamp)
