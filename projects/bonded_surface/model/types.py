# Units
from dataclasses import dataclass
from enum import Enum
import enum
from random import randint
import random
from typing import Dict, Optional, TypeAlias, TypedDict, List, Tuple
import numpy as np

Days: TypeAlias = float
Year: TypeAlias = float
PerYear: TypeAlias = float
choices = ['mintV', 'sellV', 'mintboth', 'mintS', 'sellS']

# choices that we can make for taking action
class Choices(Enum):
  mintV = 'mintV'
  sellV = 'sellV'
  mintboth = 'mintboth'
  mintS = 'mintS'
  sellS = 'sellS'

@dataclass
class ActionScenario():
  """
  The action scenario class is used to define the actions that the agent can take.
  It is also used to define the amount of action that the agent can take.
  """
  step: float = 0.1

  def get_action(self) -> Choices:
    return random.choice([ch for ch in Choices]) 

  def get_action_amount(self, stable_coin_supply: float) -> float:
    return np.random.uniform(self.step, stable_coin_supply)

@dataclass
class TraderAgent():
  id: int
  reserveAsset: float
  stableCoinSupply: float
  volatileTokenSupply: float


@dataclass 
class TraderGrowthScenario():
  """
  The trader growth scenario class is used to define the growth of the trader population.
  """
  step: float = 0.1
  growthType: str = 'flat'


  def generateTraders(self) -> List[TraderAgent]:
      return [TraderAgent(id=1,reserveAsset=100,volatileTokenSupply=100,stableCoinSupply=100)]

class ModelState (TypedDict):
  days_passed: Days
  mcv: float #mcap vol token 
  mcs: float #mcap stable token
  r: float  #reserve asset variable
  sv: float # supply of volatile token 
  ss: float # supply of stable coin
  pv: float #price of volatile token
  ps: float #price of stable coin
  active_traders: List[TraderAgent]



class ModelParams(TypedDict):
    timestep_in_days: Days
    ir: float #initial bootstrapped reserve
    action_scenario: ActionScenario
    growth_scenario: TraderGrowthScenario

class ModelSweepParams(TypedDict):
    timestep_in_days: List[Days]
    initial_reserve: List[float]
    action_scenario: List[ActionScenario]
    growth_scenario: List[TraderGrowthScenario]
