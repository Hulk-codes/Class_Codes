import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix
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