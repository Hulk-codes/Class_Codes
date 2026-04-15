import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report


def MarvellousClassifier(DataPath):
    Border = "-" * 40

    # Step 1 : Load the DataSet from CSV file
    print(Border)
    print("Step 1 : Load the DataSet from CSV file")
    print(Border)

    df = pd.read_csv(DataPath)
    print("Some entries from the Dataset")
    print(df.head())
    print(Border)

    #Step 2 : Clean the Dataset by removing empty rows
    print(Border)
    print("Step 2 : Clean the Dataset by removing empty rows")
    print(Border)

    df.dropna(inplace = True)
    print("Total record : ", df.shape[0])
    print("Total columns : ", df.shape[1])
    print(Border)



def main():
    Border = "-" * 40
    print(Border)
    print("Wine Classifier Using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()