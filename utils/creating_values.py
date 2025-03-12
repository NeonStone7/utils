import pandas as pd
import numpy as np

def return_value(num:int):

    return {'value':num*33,
            'new_value':np.random.random(num)}
