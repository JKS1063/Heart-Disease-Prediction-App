import pandas as pd
import numpy as np
import pickle

loaded_model = pickle.load(open('rg_trained_model.pkl', 'rb'))


input = np.array([54.0, 1.0, 0.0, 120.0, 188.0, 0.0, 1.0, 113.0, 0.0, 1.4, 1.0, 1.0, 3.0]).reshape(1,-1)

prediction = loaded_model.predict(input)

print(prediction)

if prediction[0] == 0:
    print("No Heart disease")
else:
    print("Have Heart disease")