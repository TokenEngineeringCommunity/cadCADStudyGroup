from cadCAD.configuration import Configuration
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from model.experiment import exp
import pandas as pd


def execute_experiment():
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

    simulation = Executor(exec_context=local_mode_ctx,
                      configs=exp.configs)
    raw_system_events, tensor_field, sessions = simulation.execute()
    return pd.DataFrame(raw_system_events)

