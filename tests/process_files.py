#! /usr/bin/env python
import numpy as np
import pandas as pd
import yaml
import pandas

def process_parameters(configname): #noqa: E265
    configparams = yaml.load(open(configname, 'r'), #noqa: E128
	           Loader=yaml.FullLoader) #noqa: E128
    try: #noqa: E501
        dim_of_measurements = configparams["dim_of_measurements"] #noqa: E501
        measured_var = configparams["measured_var"]
        covar = configparams["covar"]
        process_model = configparams["process_model"]
        white_noise_var = configparams["white_noise_var"]
        dt = configparams["dt"]
        sensor_covar = configparams["sensor_covar"]
        measurement_function = configparams["measurement_function"] #noqa: E501

    except Exception as e: #noqa F841
        print("params not given")
        raise OSError("params not given correctly.")

    return dim_of_measurements, measured_var, covar, process_model, white_noise_var, dt, sensor_covar, measurement_function #noqa E501

def process_data_file(dataname):
    df = pd.read_csv(dataname)
    zedd = df.Observations.to_numpy() #noqa: E501

    return zedd

def process_output(x,p, output_loc):
    output = []
    for i in range(len(x)):
        output.append({'x': np.array(x[i][0]), 'c': p[i]})

    import os
    df = pd.DataFrame().append(output)
    df.to_csv(os.path.join(output_loc,r'output.csv'), index=False, columns=['x', 'c']) #noqa: E501
    return df


if __name__ == '__main__': #noqa: F811
    print('No Errors')







