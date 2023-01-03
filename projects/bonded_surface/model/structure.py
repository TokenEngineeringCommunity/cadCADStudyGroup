
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
]