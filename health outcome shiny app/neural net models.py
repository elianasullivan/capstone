#imports
import keras
from keras.models import model_from_json
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import scipy
from sklearn.model_selection import train_test_split

## load the anxiety model ##
json_file = open('models/anxiety.json', 'r')
loaded_model_anxiety_json = json_file.read()
json_file.close()
loaded_model_anxiety = model_from_json(loaded_model_anxiety_json)
# load weights into new model
loaded_model_anxiety.load_weights('models/anxiety.h5')
print("Loaded model from disk")
print("anxiety")
    
## load the asthma model ##
json_file = open('models/asthma.json', 'r')
loaded_model_asthma_json = json_file.read()
json_file.close()
loaded_model_asthma = model_from_json(loaded_model_asthma_json)
# load weights into new model
loaded_model_asthma.load_weights('models/asthma.h5')
print("Loaded model from disk")
print("asthma")

## load the binge drinking model ##
json_file = open('models/binge_drinking.json', 'r')
loaded_model_binge_drinking_json = json_file.read()
json_file.close()
loaded_model_binge_drinking = model_from_json(loaded_model_binge_drinking_json)
# load weights into new model
loaded_model_binge_drinking.load_weights('models/binge_drinking.h5')
print("Loaded model from disk")
print("binge_drinking")

## load the depression model ##
json_file = open('models/depression.json', 'r')
loaded_model_depression_json = json_file.read()
json_file.close()
loaded_model_depression = model_from_json(loaded_model_depression_json)
# load weights into new model
loaded_model_depression.load_weights('models/depression.h5')
print("Loaded model from disk")
print("depression")

## load the diabetes model ##
json_file = open('models/diabetes.json', 'r')
loaded_model_diabetes_json = json_file.read()
json_file.close()
loaded_model_diabetes = model_from_json(loaded_model_diabetes_json)
# load weights into new model
loaded_model_diabetes.load_weights('models/diabetes.h5')
print("Loaded model from disk")
print("diabetes")

## load the smoke100 model ## 
json_file = open('models/smoke100.json', 'r')
loaded_model_smoke100_json = json_file.read()
json_file.close()
loaded_model_smoke100 = model_from_json(loaded_model_smoke100_json)
# load weights into new model
loaded_model_smoke100.load_weights('models/smoke100.h5')
print("Loaded model from disk")
print("smoke100")
    
## load the overweight model ##
json_file = open('models/overweight.json', 'r')
loaded_model_overweight_json = json_file.read()
json_file.close()
loaded_model_overweight = model_from_json(loaded_model_overweight_json)
# load weights into new model
loaded_model_overweight.load_weights('models/overweight.h5')
print("Loaded model from disk")
print("overweight")
loaded_model_overweight.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


## load the heart attack model ##
json_file = open('models/heart_attack.json', 'r')
loaded_model_heart_attack_json = json_file.read()
json_file.close()
loaded_model_heart_attack = model_from_json(loaded_model_heart_attack_json)
# load weights into new model
loaded_model_heart_attack.load_weights('models/heart_attack.h5')
print("Loaded model from disk")
print("heart_attack")
loaded_model_heart_attack.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

## load the heart disease model ##
json_file = open('models/heart_disease.json', 'r')
loaded_model_heart_disease_json = json_file.read()
json_file.close()
loaded_model_heart_disease = model_from_json(loaded_model_heart_disease_json)
# load weights into new model
loaded_model_heart_disease.load_weights('models/heart_disease.h5')
print("Loaded model from disk")
print("heart_disease")
loaded_model_heart_disease.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

## load the stroke model ##
json_file = open('models/stroke.json', 'r')
loaded_model_stroke_json = json_file.read()
json_file.close()
loaded_model_stroke = model_from_json(loaded_model_stroke_json)
# load weights into new model
loaded_model_stroke.load_weights('models/stroke.h5')
print("Loaded model from disk")
print("stroke")
loaded_model_stroke.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#make functions for each model
def predict_anxiety_nn(x):
    loaded_model_anxiety.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_anxiety.predict(use_data.transpose()))
    return(float(value[0][0]))

def predict_asthma_nn(x):
    loaded_model_asthma.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_asthma.predict(use_data.transpose()))
    return(float(value[0][0]))
 
def predict_binge_drinking_nn(x):
    loaded_model_binge_drinking.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_binge_drinking.predict(use_data.transpose()))
    return(float(value[0][0]))

def predict_depression_nn(x):
    loaded_model_depression.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_depression.predict(use_data.transpose()))
    return(float(value[0][0]))
    
def predict_diabetes_nn(x):
    loaded_model_diabetes.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_diabetes.predict(use_data.transpose()))
    return(float(value[0][0]))

def predict_overweight_nn(x):
    loaded_model_overweight.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_overweight.predict(use_data.transpose()))
    return(float(value[0][0]))

def predict_smoke100_nn(x):
    loaded_model_smoke100.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_smoke100.predict(use_data.transpose()))
    return(float(value[0][0]))

def predict_heart_attack_nn(x):
    loaded_model_heart_attack.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_heart_attack.predict(use_data.transpose()))
    return(float(value[0][0]))

def predict_heart_disease_nn(x):
    loaded_model_heart_disease.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_heart_disease.predict(use_data.transpose()))
    return(float(value[0][0]))

def predict_stroke_nn(x):
    loaded_model_stroke.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    use_data = pd.DataFrame(data=x)
    value =(loaded_model_stroke.predict(use_data.transpose()))
    return(float(value[0][0]))

