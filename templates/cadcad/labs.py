from cadCAD.configuration.utils import config_sim

from model.experiment import exp
from model.params import SIM_CONFIG, GENESIS_STATES
from model.structure import PARTIAL_STATE_UPDATE_BLOCKS


sim_params = config_sim(SIM_CONFIG)
exp.append_configs(
    sim_configs=sim_params,
    initial_state=GENESIS_STATES,
    partial_state_update_blocks= PARTIAL_STATE_UPDATE_BLOCKS
)

