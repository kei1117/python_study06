import pandas as pd
import inspect
import os
import datetime

EXP_CSV_PATH="results/exp_list_{name}_{datetime}.csv"


def makedir_for_filepath(filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)


def to_csv(data):
    from_func_name = inspect.stack()[1].function
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    
    makedir_for_filepath(EXP_CSV_PATH)

    df = pd.DataFrame(data)
    df.to_csv(EXP_CSV_PATH.format(name=from_func_name, datetime=now), header=False, index=False, encoding='utf_8_sig')
