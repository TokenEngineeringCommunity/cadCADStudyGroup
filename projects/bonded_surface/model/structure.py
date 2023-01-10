
from typing import Tuple, TypeAlias
import numpy as np
import random
import copy
from model.types import ModelParams, ModelState

#policies
def p_evolve_time(params: ModelParams,
                  _2,
                  _3,
                  _4):
    return {'delta_in_days': params['timestep_in_days']}

def p_growth_policy(params: ModelParams,
_2,
_3,
state: ModelState): 
    rm_traders= []
    add_traders= []
    if(len(state['active_traders'])) < 0:
      add_traders = params['growth_scenario'].generateTraders()
    return {'rm_traders': rm_traders, 'add_traders': add_traders}

#state updates 
def s_days_passed(_1,
                  _2,
                  _3,
                  state: ModelState,
                  signal):
    value = state['days_passed'] + signal['delta_in_days']
    return ('days_passed', value)

def s_delta_days(_1,
                 _2,
                 _3,
                 state: ModelState,
                 signal):
    value = signal['delta_in_days']
    return ('delta_days', value)


PARTIAL_STATE_UPDATE_BLOCKS = [
    {
        'label': 'Time Tracking',
        'policies': {
            'evolve_time': p_evolve_time,
        },
        'variables': {
            'days_passed': s_days_passed,
            'delta_days': s_delta_days,
        }
    },
    {
      'label': 'Trader Population Management',
      'policies': {
          'growth_policy': p_growth_policy,
      },
      'variables': {
      }
    }
]