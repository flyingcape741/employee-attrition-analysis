
import pandas as pd
import os
from kaggle.api.kaggle_api_extended import KaggleApi

import ReadySets
import tensorflow as tf
import logging
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


api = KaggleApi()
api.authenticate()



dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = dir_path + '\\Datasets'
ObjDataHazir = ReadySets.DataHazir(dir_path,data_path)
ObjDataHazir.downloader()

train, atr_train, eval, atr_eval, test = ObjDataHazir.dataframer()
featureColumns = ObjDataHazir.FeatureSplitter(train)


train_func = ObjDataHazir.DataFrameToTensorFlowFunc(train, atr_train, num_epochs= 100, shuffle=True,batch_size=32)
eval_func = ObjDataHazir.DataFrameToTensorFlowFunc(eval,atr_eval, num_epochs= 1, shuffle = False, batch_size=30)
test_func = ObjDataHazir.TestToTensorFlowFunc(test,shuffle2 = False, batch_size2=20)    #Ayrıca test veriside mevcut ama bu sette "Attrition" değerleri bilinmemektedir.
linear = tf.estimator.LinearClassifier(feature_columns=featureColumns)
linear.train(train_func)

result = linear.evaluate(eval_func)
print(result)



EvalPredictions = linear.predict(eval_func)

result = []

for pred1 in EvalPredictions:
    result.append(pred1['class_ids'][0])

correct = 0
for a in range(0,376):
    if result[a] == atr_eval.iloc[a]:
        correct = correct+1
correctDF = pd.DataFrame({'Correct': [correct] * 376})

correctYes = 0
for u in range(0,376):
    if result[u] == 1:
        if result[u] == atr_eval.iloc[u]:
            correctYes = correctYes+1
correctYesDF = pd.DataFrame({'CorrectYes': [correctYes] * 376})

print(f"CorrectAmount:{correct}")
print(f"CorrectYesAmount:{correctYes}")
print(f"Accuracy: {correct/376}")

kk = 0
for h in range(0,376):
    if atr_eval.iloc[h] == 1:
        kk = kk+1
print(f"YesCountinSet:{kk}" )

YesCount1 = 0
for o in result:
    if o == 1:
        YesCount1 = YesCount1+1
print(f"YesCountinPredictions:{YesCount1}" )


os.chdir(data_path)
TempDF = pd.DataFrame({'Predicted Attrition': result})
atr_eval = pd.DataFrame(atr_eval.reset_index())

D = atr_eval.join(TempDF).drop(['index'],axis=1)
D = D.join(correctDF)
D = D.join(correctYesDF)
D.to_excel('ResultDataSet.xlsx')


os.chdir(dir_path)

#Test verisi için predictionlar istenirse aşağıda gösterilebilir

predictions = linear.predict(test_func)

result2 = []

for pred in predictions:
    result2.append(pred['class_ids'][0])

print(result2)

YesCount = 0
for i in result2:
    if i == 1:
        YesCount = YesCount+1
print(YesCount)










