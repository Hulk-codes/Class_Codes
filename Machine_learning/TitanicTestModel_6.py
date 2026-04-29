import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix

#---------------------------------------------------------------
#   Function name : LoadPreserveModel
#   Description   : It is used to load preserve the model                 
#   Parameters    : filename
#   Return        : None
#   Date          : 14/03/2026
#   Author        : Pranav Raosaheb Patil
#---------------------------------------------------------------

def LoadPreserveModel(filename):

    loaded_model = joblib.load(filename)

    print("Model Successfully loaded")

    return loaded_model

#---------------------------------------------------------------
#   Function name : PreserveModel
#   Description   : It is used to preserve the model                 
#   Parameters    : model,filename
#   Return        : None
#   Date          : 14/03/2026
#   Author        : Pranav Raosaheb Patil
#---------------------------------------------------------------

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model Preserved Successfully : ", filename)

#---------------------------------------------------------------
#   Function name : TrainTitanicModel
#   Description   : It does split X,Y, training data,testing data                  
#   Parameters    : df
#   Return        : None
#   Date          : 14/03/2026
#   Author        : Pranav Raosaheb Patil
#---------------------------------------------------------------

def TrainTitanicModel(df):
    X = df.drop("Survived", axis =1)
    Y = df["Survived"]

    print("\nFeatures : ")
    print(X.head())

    print("\nLabels : ")
    print(Y.head())

    print("\nShape of X : ", X.shape)
    print("\nShape of Y : ", Y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=43)

    print("\nX_train shape : ", X_train.shape)
    print("X_test shape : ", X_test.shape)
    print("Y_train shape : ", Y_train.shape)
    print("Y_testn shape : ", Y_test.shape) 

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train,Y_train)

    print("\nModel Trained Successfully")

    print("\nIntercept of model : ")
    print(model.intercept_)

    print("\nCoefficient of model : ")
    for feature,coefficient in zip(X.columns,model.coef_[0]):
        print(feature, " : ", coefficient)

    PreserveModel(model, "MarvellousTitanic.pkl")

    loaded_model = LoadPreserveModel("MarvellousTitanic.pkl")

    Y_pred = loaded_model.predict(X_test)

    accuracy = accuracy_score(Y_pred,Y_test)

    print("\nAccuracy is : ", accuracy)

    cm = confusion_matrix(Y_pred,Y_test)

    print("\nConfusion Matrix is : ", cm)
    

#---------------------------------------------------------------
#   Function name : Displayinfo
#   Description   : It displays the formated title                   
#   Parameters    : title(str)
#   Return        : None
#   Date          : 14/03/2026
#   Author        : Pranav Raosaheb Patil
#---------------------------------------------------------------

def Displayinfo(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


#---------------------------------------------------------------
#   Function name : ShowData
#   Description   : It shows basic information about the dataset
#   Parameters    : df
#                   df ->       Pandas Dataframe object
#                   message 
#                   message ->  Heading text to display
#   Return        : None
#   Date          : 14/03/2026
#   Author        : Pranav Raosaheb Patil
#---------------------------------------------------------------

def ShowData(df,message):
    Displayinfo(message)

    print("\nFirst Five rows of Dataset")
    print(df.head())
    
    print("\nShape of Dataset")
    print(df.shape)

    print("\nColumns name")
    print(df.columns.tolist())

    print("\nMissing Values in each column")
    print(df.isnull().sum())

#---------------------------------------------------------------
#   Function name : CleanTitanicData
#   Description   : It does Preprocessing
#                   It removes unnecessary columns
#                   It handles missing values
#                   It converts text data to numeric format
#                   It does encoding to categorical columns                 
#   Parameters    : DataPath of Dataset file
#   Return        : None
#   Date          : 14/03/2026
#   Author        : Pranav Raosaheb Patil
#---------------------------------------------------------------
    
def CleanTitanicData(df):
    Displayinfo("Step 2 : Original Data")
    print(df.head())

    # Remove Unnecessary columns
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]
    print("\n Colums to be dropped : ")
    print(existing_columns)

    # drop the Unwanted columns
    df = df.drop(columns = existing_columns)
    Displayinfo("\nStep 2 : Data After column removal")
    print(df.head())

    # Handle age column
    if "Age" in df.columns:
        print("\nAge column before filling missing values")
        print(df["Age"].head(10))

        # coerce -> invalid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")      

        age_median = df["Age"].median()

        # Replace Missing Values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge column after preprocessing : ")
        print(df["Age"].head(10))

    # Handle Fare column

    if "Fare" in df.columns: 
        print("\nFare Column before preprocessing")
        print(df["Fare"].head(10))

        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")   

        fare_median = df["Fare"].median()
        print("\nMedian of Fare column is : ", fare_median)

        # Replace Missing Values with median
        df["Fare"] = df["Fare"].fillna(fare_median)

        print("\nFare column after preprocessing : ")
        print(df["Fare"].head(10))

    # Handle Embarked column
    if "Embarked" in df.columns:
        print("\nEmbarked column before preprocessing")
        print(df["Embarked"].head(10))

        # Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Remove Missing Values
        df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

        # Got most frequent Value
        embarked_mode = df["Embarked"].mode()[0]
        print("Mode of Embarked Column : ", embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked column after preprocessing : ")
        print(df["Embarked"].head(10))  

    # Handle Sex column

    if "Sex" in df.columns: 
        print("\nSex Column before preprocessing")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")   

        print("\nSex column after preprocessing : ")
        print(df["Sex"].head(10))  

    Displayinfo("Data After Preprocessing")
    print(df.head())

    print("\nMissing Values after preprocessing")
    print(df.isnull().sum())

    # Encode Embarked Column
    df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)

    print("\nData After Encoding")
    print(df.head())

    print("Shape of Dataset : ", df.shape)

    # convert boolean columns into integer
    for col in df.columns:
        if df[col].dtype == bool :
            df[col] = df[col].astype(int)

    print("\nData After Encoding")
    print(df.head())

    return df


#---------------------------------------------------------------
#   Function name : MarvellousTitanicLogistic
#   Description   : This is main pipeline controller
#                   It loads the dataset , shows raw data
#                   It preprocess the dataset & train the model
#                   
#   Parameters    : DataPath of Dataset file
#   Return        : None
#   Date          : 14/03/2026
#   Author        : Pranav Raosaheb Patil
#---------------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):
    Displayinfo("Step 1 : Loading the Dataset")
    df = pd.read_csv(DataPath)

    ShowData(df,"Initial Datset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)

#---------------------------------------------------------------
#   Function name : main
#   Description   : Starting point of the application
#   Parameters    : None
#   Return        : None
#   Date          : 14/03/2026
#   Author        : Pranav Raosaheb Patil
#---------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()