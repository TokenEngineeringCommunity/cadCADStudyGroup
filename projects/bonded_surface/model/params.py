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
growth_scenario = types.TraderGrowthScenario(growthType='flat')

MODEL_SWEEP_PARAMS = types.ModelSweepParams(
    timestep_in_days=[DAYS_PER_TIMESTEP],
    initial_reserve= [0.05],
    action_scenario=[action_scenario],
    growth_scenario=[growth_scenario]
)


SYS_PARAMS = {
    'parameter': [1]
}

GENESIS_STATES: types.ModelState = {
    'days_passed': INITIAL_DAYS,
    'mcs': 500000.0,
    'mcv': ,
    'ps': 1.0,
    'pv': 53182.96,
    'r': 1000000.0, 
    'ss': 500000,
    'sv':37.606031,
    'active_traders': []
}


SIM_CONFIG= {
    'N': MONTE_CARLO_RUNS,
    'T': range(SIMULATION_TIMESTEPS),
    'M':  MODEL_SWEEP_PARAMS 
}
