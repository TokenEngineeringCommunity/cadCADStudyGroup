from cadCAD.configuration import Experiment
from cadCAD.configuration.utils import config_sim
from model.params import SIM_CONFIG, GENESIS_STATES
from model.structure import PARTIAL_STATE_UPDATE_BLOCKS

import pandas as pd
import numpy as np


exp = Experiment()

sim_params = config_sim(SIM_CONFIG)
exp.append_configs(
    sim_configs=sim_params,
    initial_state=GENESIS_STATES,
    partial_state_update_blocks= PARTIAL_STATE_UPDATE_BLOCKS
)