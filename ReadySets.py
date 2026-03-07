
import pandas
import pandas as pd
import os
from kaggle.api.kaggle_api_extended import KaggleApi
import tensorflow as tf


api = KaggleApi()
api.authenticate()

class DataHazir():
    def __init__(self, dir_path, data_path):
        self.dir_path = dir_path
        self.data_path = data_path
    def downloader(self):
        os.chdir(self.data_path)
        for a in os.listdir(self.data_path):
            os.remove(a)


        
        api.competition_download_file('ai-and-ml-level-1-kaggle-competition', 'train.csv', os.path.dirname(os.path.realpath(__file__)) + '\\Datasets')
        api.competition_download_file('ai-and-ml-level-1-kaggle-competition', 'test.csv', os.path.dirname(os.path.realpath(__file__)) + '\\Datasets')



        for i in os.listdir(self.data_path):
            self.read_file = pd.read_csv(self.data_path+'\\'+i, encoding='utf-8', on_bad_lines='skip',encoding_errors='ignore', lineterminator='\n')
            os.remove(i)
            self.read_file.to_excel(i.replace('.csv','.xlsx'), index=None, header=True)

        os.chdir(self.dir_path)

    def dataframer(self):
        self.train = pandas.read_excel(self.data_path + '\\train.xlsx', dtype={
    'Age': float,
    'Attrition': str,
    'BusinessTravel': str,
    'DailyRate': float,
    'Department': str,
    'DistanceFromHome': float,
    'Education': str,
    'EducationField': str,
    'EmployeeCount': float,
    'EmployeeNumber': float,
    'EnvironmentSatisfaction': float,
    'Gender': str,
    'HourlyRate': float,
    'JobInvolvement': float,
    'JobLevel': str,
    'JobRole': str,
    'JobSatisfaction': float,
    'MaritalStatus': str,
    'MonthlyIncome': float,
    'MonthlyRate': float,
    'NumCompaniesWorked': float,
    'Over18': str,
    'Overtime': str,
    'PercentSalaryHike': float,
    'PerformanceRating': float,
    'RelationshipSatisfaction': float,
    'StandardHours': float,
    'StockOptionLevel': float,
    'TotalWorkingYears': float,
    'TrainingTimesLastYear': float,
    'WorkLifeBalance': float,
    'YearsAtCompany': float,
    'YearsInCurrentRole': float,
    'YearsSinceLastPromotion': float,
    'YearsWithCurrManager': float,
    })

        self.train.head()


        self.eval = self.train.copy().iloc[800:,:]
        self.atr_eval = self.eval.pop('Attrition')
        self.atr_eval.replace({'Yes': 1.0, 'No': 0.0}, inplace=True)

        self.train = self.train.iloc[:800,:]
        self.atr_train = self.train.pop('Attrition')
        self.atr_train.replace({'Yes': 1.0, 'No': 0.0}, inplace=True)
        print(self.atr_train)
        self.eval.head()

        """NORMALIZATION"""

       
        for b in ['Age','DailyRate','DistanceFromHome','EnvironmentSatisfaction','HourlyRate','JobSatisfaction','MonthlyIncome','MonthlyRate','NumCompaniesWorked',
                  'PercentSalaryHike','PerformanceRating','RelationshipSatisfaction','TotalWorkingYears','TrainingTimesLastYear','WorkLifeBalance','YearsAtCompany',
                  'YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','JobInvolvement','StockOptionLevel',]:
            self.train[b] = ((self.train[b] - self.train[b].min())/(self.train[b].max() - self.train[b].min()))

        for k in ['Age','DailyRate','DistanceFromHome','EnvironmentSatisfaction','HourlyRate','JobSatisfaction','MonthlyIncome','MonthlyRate','NumCompaniesWorked',
                  'PercentSalaryHike','PerformanceRating','RelationshipSatisfaction','TotalWorkingYears','TrainingTimesLastYear','WorkLifeBalance','YearsAtCompany',
                  'YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','JobInvolvement','StockOptionLevel',]:
            self.eval[k] = ((self.eval[k] - self.eval[k].min())/(self.eval[k].max() - self.eval[k].min()))




        """NORMALIZATION"""






        self.test = pandas.read_excel(self.data_path + '\\test.xlsx', dtype={'Age': float,
    'Attrition': str,
    'BusinessTravel': str,
    'DailyRate': float,
    'Department': str,
    'DistanceFromHome': float,
    'Education': str,
    'EducationField': str,
    'EmployeeCount': float,
    'EmployeeNumber': float,
    'EnvironmentSatisfaction': float,
    'Gender': str,
    'HourlyRate': float,
    'JobInvolvement': float,
    'JobLevel': str,
    'JobRole': str,
    'JobSatisfaction': float,
    'MaritalStatus': str,
    'MonthlyIncome': float,
    'MonthlyRate': float,
    'NumCompaniesWorked': float,
    'Over18': str,
    'Overtime': str,
    'PercentSalaryHike': float,
    'PerformanceRating': float,
    'RelationshipSatisfaction': float,
    'StandardHours': float,
    'StockOptionLevel': float,
    'TotalWorkingYears': float,
    'TrainingTimesLastYear': float,
    'WorkLifeBalance': float,
    'YearsAtCompany': float,
    'YearsInCurrentRole': float,
    'YearsSinceLastPromotion': float,
    'YearsWithCurrManager': float,
    })
        self.test.head()

        for j in ['Age','DailyRate','DistanceFromHome','EnvironmentSatisfaction','HourlyRate','JobSatisfaction','MonthlyIncome','MonthlyRate','NumCompaniesWorked',
                'PercentSalaryHike','PerformanceRating','RelationshipSatisfaction','TotalWorkingYears','TrainingTimesLastYear','WorkLifeBalance','YearsAtCompany',
                'YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','JobInvolvement','StockOptionLevel',]:
            self.test[j] = ((self.test[j] - self.test[j].min())/(self.test[j].max() - self.test[j].min()))

        return self.train, self.atr_train, self.eval, self.atr_eval, self.test

    def FeatureSplitter(self,train2):
        self.train = train2

        self.NumericalColumns = ['Age','DailyRate','DistanceFromHome','EnvironmentSatisfaction','HourlyRate','JobSatisfaction','MonthlyIncome','MonthlyRate',
                                 'NumCompaniesWorked','PercentSalaryHike','PerformanceRating','RelationshipSatisfaction','TotalWorkingYears','TrainingTimesLastYear',
                                 'WorkLifeBalance','YearsAtCompany','YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','JobInvolvement',
                                 'StockOptionLevel']

        self.CategoricalColumns = ['BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus','Over18','OverTime','Education','JobLevel']


        self.featureColumns = []

        for features in self.CategoricalColumns:
            self.voc = self.train[features].unique()
            self.featureColumns.append(tf.feature_column.categorical_column_with_vocabulary_list(features, self.voc))

        for features in self.NumericalColumns:
            self.featureColumns.append(tf.feature_column.numeric_column(features, dtype=tf.float32))

        return self.featureColumns

    def DataFrameToTensorFlowFunc(self, data1, atr_data1, num_epochs, shuffle = True, batch_size=32):
        data = data1
        atr_data = atr_data1
        shuffle1 = shuffle
        batch_size1 = batch_size
        num_epochs1 = num_epochs

        def input_function():
            dataset = tf.data.Dataset.from_tensor_slices((dict(data),atr_data))
            if shuffle1:
                dataset = dataset.shuffle(1000)
            dataset = dataset.batch(batch_size1).repeat(num_epochs1)
            return dataset
        return input_function

#Test verisi için input fonksiyon oluşturma methodu. (Test verisi attrition içermediğinden gerekli)
    def TestToTensorFlowFunc(self, data2, shuffle2 = True, batch_size2=32):
        data3 = data2
        shuffle3 = shuffle2
        batch_size3 = batch_size2

        def input_function2():
            dataset3 = tf.data.Dataset.from_tensor_slices(dict(data3))
            if shuffle3:
                dataset3 = dataset3.shuffle(1000)
            dataset3 = dataset3.batch(batch_size3)
            return dataset3
        return input_function2