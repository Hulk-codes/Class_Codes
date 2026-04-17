import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler


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

    #Step 3: Seperate Independent and dependent variables
    print(Border)
    print("Step 3: Seperate Independent and dependent variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    print(Border)
    print("Input Columns : ", X.columns.to_list())
    print("Output Columns : Class" )

    #Step 4 : Split the Dataset for training and testing
    print(Border)
    print("Step 4 : Split the Dataset for training and testing")
    print(Border)   

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2,random_state=42,stratify=Y) 

    print(Border)
    print("Information of training and testing the data : " )
    print("X_train Shape : ", X_train.shape)
    print("X_test Shape : ", X_test.shape)
    print("Y_train Shape : ", Y_train.shape)
    print("Y_test Shape : ", Y_test.shape)

    #Step 5 : Feature Scaling
    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)   

    scaler = StandardScaler()
    # Independent Variable Scaling
    X_train_scaled = scaler.fit_transform(X_train)    
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature scaling is done")

    #Step 6 : Explore  multiple values of k
    # Hyperparameter tuning (K)
    print(Border)
    print("Step 6 : Explore  multiple values of k")
    print(Border)  

    accuracy_scores = []
    k_values = range(1,21) 

    for k in k_values:                                           # Pipeline in ML
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test, Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    
    print("Accuracy Report of all k values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(Border)

    #Step 7 : Plot graph of K vs Accuracy
    print(Border)
    print("Step 7 : Plot graph of K vs Accuracy")
    print(Border)

    plt.figure(figsize=[8,5])
    plt.plot(k_values, accuracy_scores, marker = 'o')
    plt.title("K Values v/s Accuracy")
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(k_values)
    plt.show()

    #Step 8 : Find best value of K
    print(Border)
    print("Step 8 : Find best value of K")
    print(Border)    

    best_k = list(k_values)[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is : ", best_k)
    print(Border) 

    #Step 9 : Build final model using best value of k
    print(Border)
    print("Step 9 : Build final model using best value of k")
    print(Border)  

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled, Y_train)
    Y_pred = final_model.predict(X_test_scaled)


    #Step 10 : Calculate final Accuracy
    print(Border)
    print("Step 10 : Calculate final Accuracy")
    print(Border)  

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of the model is : ", accuracy*100)

    #Step 11 : Display Confusion Matric
    print(Border)
    print("Step 11 : Display Confusion Matrix")
    print(Border)  

    cm = confusion_matrix(Y_test, Y_pred)
    print(cm)

    #Step 12 : Display Classification report
    print(Border)
    print("Step 12 : Display Classification Report")
    print(Border)  

    print(classification_report(Y_test,Y_pred))

def main():
    Border = "-" * 40
    print(Border) 
    print("Wine Classifier Using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()