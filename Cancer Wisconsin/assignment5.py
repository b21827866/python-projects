import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
missing_values = ["?"]


df = pd.read_csv("breast-cancer-wisconsin.csv", na_values=missing_values)

#completeing missing values with median Bare_Nuclei
median = df['Bare_Nuclei'].median()
df.fillna(median, inplace=True)
df = df.astype(int)

#creating train and test set
train=df.sample(frac=0.8,random_state=699)
test=df.drop(train.index)

a = train.drop("Code_number", axis=1)
b = a.drop("Class", axis=1)

c = test.drop("Code_number", axis=1)
d = c.drop("Class", axis=1)

corr = b.corr()
fig, ax = plt.subplots()
# create heatmap
def heat_map():
    im = ax.imshow(corr.values)

    # set labels
    ax.set_xticks(np.arange(len(corr.columns)))
    ax.set_yticks(np.arange(len(corr.columns)))
    ax.set_xticklabels(corr.columns)
    ax.set_yticklabels(corr.columns)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                           ha="center", va="center", color="black")


    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("", rotation=-90, va="bottom")
    fig.tight_layout()
    plt.show()



training_inputs = np.array(b)

test_inputs = np.array(d)

classs = np.array(train["Class"])

class_test = np.array(test["Class"])

training_outputs = np.reshape(classs, (-1, 1))

test_outputs = np.reshape(class_test, (-1, 1))


def sigmoid(x):
    return 1 / (1 + np.exp(-0.005*x))


def sigmoid_derivative(x):
    return 0.005 * x * (1 - x )


def run_on_test_set(test_inputs, test_outputs, weights):
    tp = 0
    tn = 0
    #calculate test_predictions
    test_predictions = sigmoid(np.dot(test_inputs, weights))

    test_predictions=np.where(test_predictions > 0.5, 1, 0)

    for predicted_val, label in zip(test_predictions, test_outputs):
        if predicted_val == label:
            tp += 1
        tn += 1

    accuracy = tp / tn

    return accuracy



np.random.seed(1)
weights = 2 * np.random.random((9, 1)) - 1
accuracy_array = []
loss_array = []
for iteration in range(2500):
    input = training_inputs
    outputs = sigmoid(np.dot(input, weights))
    loss = training_outputs - outputs
    loss_array.append(np.mean(loss))
    tuning = loss * sigmoid_derivative(outputs)
    weights += np.dot(training_inputs.T, tuning)

    accuracy_array.append(run_on_test_set(test_inputs, test_outputs, weights))


def plot_maps():

    plt.plot([i+1 for i in range(len(accuracy_array))],accuracy_array)
    plt.xlabel("Iteration Count")
    plt.ylabel("Accuracy")
    plt.title("Accurary Array")
    plt.show()


    plt.plot([i+1 for i in range(len(loss_array))],loss_array)
    plt.xlabel("Iteration Count")
    plt.ylabel("Loss")
    plt.title("Loss Array")
    plt.show()

heat_map()
plot_maps()

