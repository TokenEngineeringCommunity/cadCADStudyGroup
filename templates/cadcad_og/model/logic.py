import numpy as np

def s_something(params, 
                substep, 
                state_history, 
                prev_state, 
                policy_input):
    new_value = np.random.randn()
    return ('something', new_value)