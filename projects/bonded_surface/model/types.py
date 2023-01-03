# Units
from dataclasses import dataclass
from enum import Enum
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


class ModelState (TypedDict):
  days_passed: Days
  mcv: float #mcap vol token 
  mcs: float #mcap stable token
  r: float  #reserve asset variable
  sv: float # supply of volatile token 
  ss: float # supply of stable coin
  pv: float #price of volatile token
  ps: float #price of stable coin

class ModelParams(TypedDict):
    timestep_in_days: Days
    ir: float #initial bootstrapped reserve
    action_scenario: ActionScenario

class ModelSweepParams(TypedDict):
    timestep_in_days: List[Days]
    initial_reserve: List[float]
    action_scenario: List[ActionScenario]
