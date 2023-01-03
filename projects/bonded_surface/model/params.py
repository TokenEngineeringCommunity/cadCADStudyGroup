import model.types as types 
import numpy as np
from decimal import Decimal 
from datetime import timedelta

MONTE_CARLO_RUNS = 1
DAYS_PER_TIMESTEP = 30
SIMULATION_TIMESTEPS = 100
DAYS_PER_TIMESTEP = 30
YEAR = 365.25
SIMULATION_TIME_IN_YEARS = 5
INITIAL_DAYS = 0

action_scenario = types.ActionScenario()

MODEL_SWEEP_PARAMS = types.ModelSweepParams(
    timestep_in_days=[DAYS_PER_TIMESTEP],
    initial_reserve= [0.05],
    action_scenario=[action_scenario]
)


SYS_PARAMS = {
    'parameter': [1]
}

GENESIS_STATES: types.ModelState = {
    'days_passed': INITIAL_DAYS,
    'mcs': 0.0,
    'mcv': 0.0,
    'ps': 0.0,
    'pv': 0.0,
    'r': 0.0,
    'ss': 0.0,
    'sv':0.0
}


SIM_CONFIG= {
    'N': MONTE_CARLO_RUNS,
    'T': range(SIMULATION_TIMESTEPS),
    'M':  MODEL_SWEEP_PARAMS 
}
