from mesa import Agent,  Model
from mesa.time import BaseScheduler
from mesa.datacollection import DataCollector
import random

class ConsumptionUnit(Agent):
    def __init__(self,  unique_id,  model, steamConPattern):
        super().__init__(unique_id, model)
        self.stepNumb = 0
        self.steamConPattern = steamConPattern
        self.steamConPatternEval = {x : 0 for x in range(3)}
        self.patternChoice = random.randint(0,2)
        self.stepSteamCon = 0

    def step(self):
        generator = self.model.schedule.agents[self.model.num_agents]
        # generator.steamGenLevelRequired += self.steamConPattern[self.model.hour]
        generator.agentSteamReq[self] = self.steamConPattern[self.patternChoice][self.model.hour]
        self.stepSteamCon = self.steamConPattern[self.patternChoice][self.model.hour]

        self.stepNumb += 1

    def updatePattern(self):

        if self.model.training == True:
            self.patternChoice = random.randint(0,2)
        else:
            # print(self.unique_id,self.steamConPatternEval)
            self.patternChoice = max(self.steamConPatternEval, key=self.steamConPatternEval.get)
        # self.patternChoice = random.randint(0,2)
        # self.patternChoice = 1

class GenUnit(Agent):
    def __init__(self, unique_id, model, renewablePattern):
        super().__init__(unique_id, model)
        self.stepNumb = 0
        self.steamGenLevel = 20
        # self.steamGenLevelRequired = 0
        self.steamRampLevel = 0
        self.safetyFactor = 5
        self.agentSteamReq = {agent : 0 for agent in model.schedule.agents} # storage of all the agent requirements
        self.renewablePattern = renewablePattern

        self.stepSteamCon = 0
        self.patternChoice = -1 # no use in this class, it's for datacollector homogeneity

    def step(self):
        # if (self.steamGenLevelRequired - self.steamGenLevel)>=0: #if request level is higher than actual level, ramp up
            # self.steamGenLevel += self.steamRampPerHour
        # else: #if request level is lower than actual but inside the safety coef
        # self.steamRampLevel = self.steamGenLevelRequired - self.steamGenLevel + self.safetyFactor
        self.steamRampLevel = sum(self.agentSteamReq.values()) - (self.steamGenLevel + self.renewablePattern[self.model.hour]) + self.safetyFactor
        self.steamGenLevel += self.steamRampLevel

        self.stepNumb += 1

    def updatePattern(self):
        if self.model.training == False:
            # stepNumber = self.model.getStepNumb() #get the current stepnumber

            agentData = self.model.datacollector.get_agent_vars_dataframe()
            modelData = self.model.datacollector.get_model_vars_dataframe()

            dayGen = modelData[self.stepNumb-24:]
            dayGen = dayGen["GenLevel"]
            totalDayGen = sum(dayGen)

            dayStepSteam = agentData["StepSteam"]
            dayStepSteam = dayStepSteam.reset_index(level=['AgentID'])
            # dayStepSteam = dayStepSteam[self.stepNumb-(24*self.model.num_agents):]
            # dayAgent = dayAgent[self.stepNumb-(23*self.model.num_agents):]
            for agentID in range(self.model.num_agents):
                tempDayStepSteam = dayStepSteam[dayStepSteam['AgentID']==agentID]
                tempDayStepSteam = tempDayStepSteam[self.stepNumb-24:]
                tempDayStepSteam = tempDayStepSteam["StepSteam"] - (self.renewablePattern/self.model.num_agents)
                tempDayStepSteam = tempDayStepSteam[tempDayStepSteam>=0]
                dayPercent = sum(tempDayStepSteam) / totalDayGen
                # print(agentID, dayPercent)
                agentPattern = self.model.schedule.agents[agentID].patternChoice
                self.model.schedule.agents[agentID].steamConPatternEval[agentPattern] += (1/(self.model.num_agents-1)) - dayPercent

                # If generator has to ramp higher then his safety factor
                # Give a bad point to the patterns used that day

# def compute_total(model):
#     agent_Consumption = [agent.steamConPattern[model.hour] for agent in model.schedule.agents]
#     total = sum(agent_Consumption)
#     return total

def get_genLevel(model):
    return model.schedule.agents[model.num_agents].steamGenLevel

def get_rampLevel(model):
    return model.schedule.agents[model.num_agents].steamRampLevel

class FactoryModel(Model):
    def __init__(self, N, steamConPattern, renewablePattern, trainingDays):
        self.num_agents = N
        self.training = True
        self.trainingDays = trainingDays
        # ------ Instanciation of the scheduler ------
        # We use the BaseScheduler as we wish for the consuming units to activate before the generating unit
        # Hence, the generator is added last
        self.schedule=BaseScheduler(self)

        for i in range(self.num_agents): # Instanciate the consuming agents and add them to the scheduler
            a = ConsumptionUnit(i, self, steamConPattern)
            self.schedule.add(a)
        self.schedule.add(GenUnit(self.num_agents,self, renewablePattern)) # generator unit is always added at the end so we know how to find him

        # ----- Instanciation of the clock ------
        self.hour = 0
        self.day = 0
        # self.stepNumb = 0

        # ------ Instanciation of the data collector function ------
        # Here we mesure 2 metrics
        # _The GenLevel which corresponds to the current quantity of steam being produced
        # _The RampLevel which corresponds to the ramp applied since the previous day
        self.datacollector = DataCollector(model_reporters={"GenLevel": get_genLevel , "RampLevel": get_rampLevel, "Day":"day", "Hour":"hour"},
                                            agent_reporters={"patternChoice": "patternChoice", "StepSteam":"stepSteamCon"})

    def step(self):
        # begining of the idea that maybe there will be training periods with different behaviour
        if self.day >= self.trainingDays:
            self.training = False

        self.datacollector.collect(self)
        self.schedule.step()

        # clock segments, used to know what time it is in the model
        # increment an hour after each step
        # self.stepNumb += 1
        if self.hour >= 23:
            for agent in reversed(self.schedule.agents):
                agent.updatePattern()
            self.hour = 0
            self.day += 1
        else:
            self.hour += 1

    # def getStepNumb(self):
    #     return self.stepNumb
