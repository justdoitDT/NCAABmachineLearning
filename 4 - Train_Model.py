import torch
from torch import nn
from torch.nn import functional as F
import pandas as pd
import numpy as np
import csv
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
from datetime import datetime

rootDirectory = '/Users/dthomas/Desktop/Coding/NCAAB'


inputDF = pd.read_csv(rootDirectory + '/NormalizedInputData/ConcatenatedNormalizedInputDF.csv')
inputArray = inputDF.to_numpy()
x = inputArray[:, 4:].astype('float32')
y = inputArray[:, 3].astype('bool')
print("shape of x: {}\nshape of y: {}".format(x.shape,y.shape))

# define dataset class
class dataset(Dataset):
    def __init__(self, x, y):
        self.x = torch.tensor(x, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)
        self.length = self.x.shape[0]
    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]
    def __len__(self):
        return self.length

# create instance of dataset
trainset = dataset(x, y)

# create instance of DataLoader
trainloader = DataLoader(trainset, batch_size=12, shuffle=True) # reset batch size to 73

# define the network
class Net(nn.Module):
    def __init__(self, input_shape):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_shape, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3 = nn.Linear(512, 256)
        self.fc4 = nn.Linear(256, 16)
        # self.fc5 = nn.Linear(128, 64)
        # self.fc6 = nn.Linear(64, 32)
        # self.fc7 = nn.Linear(32, 16)
        # self.fc8 = nn.Linear(16, 8)
        # self.fc9 = nn.Linear(8, 4)
        # self.fc10 = nn.Linear(4, 2)
        self.fc11 = nn.Linear(16, 1)    # reset to (2, 1)
        # Initialize the weights using Xavier initialization
        nn.init.xavier_uniform_(self.fc1.weight)
    def forward(self,x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc4(x))
        # x = torch.relu(self.fc5(x))
        # x = torch.relu(self.fc6(x))
        # x = torch.relu(self.fc7(x))
        # x = torch.relu(self.fc8(x))
        # x = torch.relu(self.fc9(x))
        # x = torch.relu(self.fc10(x))
        x = torch.sigmoid(self.fc11(x))
        return x

# set hyper parameters
learning_rate = 10**-20
epochs = 700

# Model, Optimizer, Loss
model = Net(input_shape=x.shape[1])
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
loss_fn = nn.BCELoss()


# train model
losses = []
accur = []
for i in range(epochs):
    batchNum = -1
    print('epoch:', i, '   ', str(datetime.now())[:-7])
    for j, (x_train, y_train) in enumerate(trainloader):
        batchNum += 1
        print('batch', batchNum)
        # calculate output
        output = model(x_train)
        # calculate loss
        loss = loss_fn(output, y_train.reshape(-1, 1))
        print('got this far! A')
        # accuracy
        predicted = model(torch.tensor(x, dtype=torch.float32))
        acc = (predicted.reshape(-1).detach().numpy().round() == y).mean()
        # backprop
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    losses.append(loss)
    accur.append(acc)
    print("epoch {}\tloss : {}\t accuracy : {}".format(i, loss, acc))


# plot loss
plt.plot(losses)
plt.title('Loss vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('loss')

# plot accuracy
plt.plot(accur)
plt.title('Accuracy vs Epochs')
plt.xlabel('Accuracy')
plt.ylabel('loss')











# import numpy as np
# import pandas as pd
# from datetime import datetime
# import copy
# import torch
# from torch.utils.data import Dataset
# from torch.utils.data import DataLoader
# from torchvision import datasets, transforms
# import torch.nn.functional as F
# import torch.nn as nn
# import torch.optim as optim
# import tqdm
# from sklearn.model_selection import StratifiedKFold, train_test_split
#
#
# rootDirectory = '/Users/dthomas/Desktop/Coding/NCAAB'
# startingYear = 2006
# endingYear = 2023
#
# listNormalizedInputDF = []
# for year in range(startingYear, endingYear + 1):
#     normalizedInputDF = pd.read_csv(rootDirectory + '/NormalizedInputData/NormalizedInputData' + str(year) + '.csv')
#     listNormalizedInputDF.append(normalizedInputDF)
#
# concatenatedNormalizedInputDF = pd.concat(listNormalizedInputDF)
# # concatenatedNormalizedInputDF.to_csv(rootDirectory + '/GiantNormalizedInputDF.csv')
# # print(rootDirectory + '/GiantNormalizedInputDF.csv written.')
#
# # # Define Dataset class
# # class GamesDataset(Dataset):
# #     def __init__(self, file_name):
# #         gamesDF = pd.read_csv(file_name)
# #
# #         features = gamesDF.iloc[:, 5:].values
# #         labels = gamesDF.iloc[:, 2].values
# #
# #         self.features_train = torch.tensor(features, dtype=torch.float32)
# #         self.labels_train = torch.tensor(labels, dtype=torch.float32)
# #
# #     def __len__(self):
# #         return len(self.labels_train)
# #
# #     def __getitem__(self, itemToGet):
# #         return self.features_train[itemToGet], self.labels_train[itemToGet]
# #
# #
# # # create instance of Dataset and trainloader
# # gamesDataset = GamesDataset(normalizedDFpath)
# # train_loader = DataLoader(gamesDataset, batch_size=10, shuffle=False)
# #
# #
# # # check that data is loaded as intended
# # for index, (data, labels) in enumerate(train_loader):
# #     print('data.shape:', data.shape, ' labels.shape:', labels.shape)
# #     print('data:', data)
# #     print('labels:', labels)
# #     break
#
#
# # define network class
# class Predictor(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.fc1 = nn.Linear(1923, 1024)
#         self.fc2 = nn.Linear(1024, 512)
#         self.fc3 = nn.Linear(512, 256)
#         self.fc4 = nn.Linear(256, 128)
#         self.fc5 = nn.Linear(128, 64)
#         self.fc6 = nn.Linear(64, 32)
#         self.fc7 = nn.Linear(32, 16)
#         self.fc8 = nn.Linear(16, 8)
#         self.fc9 = nn.Linear(8, 4)
#         self.fc10 = nn.Linear(4, 2)
#         self.output = nn.Linear(2, 1)
#         self.sigmoid = nn.Sigmoid()
#     def forward(self, x):
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = F.relu(self.fc3(x))
#         x = F.relu(self.fc4(x))
#         x = F.relu(self.fc5(x))
#         x = F.relu(self.fc6(x))
#         x = F.relu(self.fc7(x))
#         x = F.relu(self.fc8(x))
#         x = F.relu(self.fc9(x))
#         x = F.relu(self.fc10(x))
#         x = self.sigmoid(self.output(x))
#         return x
#
#
# # define training loop
# def model_train(model, X_train, y_train, X_val, y_val):
#     # loss function and optimizer
#     loss_fn = nn.BCELoss()  # binary cross entropy
#     optimizer = optim.Adam(model.parameters(), lr=0.0001)
#
#     n_epochs = 250  # number of epochs to run
#     batch_size = 10  # size of each batch
#     batch_start = torch.arange(0, len(X_train), batch_size)
#
#     # Hold the best model
#     best_acc = - np.inf  # init to negative infinity
#     best_weights = None
#
#     for epoch in range(n_epochs):
#         batchCount = 0
#         print('epoch: ' + str(epoch) + '  ' + str(datetime.now())[:-7])
#         model.train()
#         with tqdm.tqdm(batch_start, unit="batch", mininterval=0, disable=True) as bar:
#             bar.set_description(f"Epoch {epoch}")
#             for start in bar:
#                 # take a batch
#                 batchCount += 1
#                 print('batchCount:', batchCount)
#                 X_batch = X_train[start:start + batch_size]
#                 y_batch = y_train[start:start + batch_size]
#                 # forward pass
#                 y_pred = model(X_batch)
#                 y_pred = y_pred.view(y_batch.shape[0]) # <-----I added this
#                 print('\ny_pred', y_pred, 'min', torch.min(y_pred), 'max', torch.max(y_pred))
#                 print('y_batch', y_batch, 'min', torch.min(y_batch), 'max', torch.max(y_batch))
#                 loss = loss_fn(y_pred, y_batch)
#                 # backward pass
#                 optimizer.zero_grad()
#                 loss.backward()
#                 # update weights
#                 optimizer.step()
#                 # print progress
#                 acc = (y_pred.round() == y_batch).float().mean()
#                 bar.set_postfix(
#                     loss=float(loss),
#                     acc=float(acc)
#                 )
#         # evaluate accuracy at end of each epoch
#         model.eval()
#         y_pred = model(X_val)
#         acc = (y_pred.round() == y_val).float().mean()
#         acc = float(acc)
#         if acc > best_acc:
#             best_acc = acc
#             best_weights = copy.deepcopy(model.state_dict())
#     # restore model and return best accuracy
#     model.load_state_dict(best_weights)
#     return best_acc
#
#
# # execute training loop and check accuracy
#
# #normalizedDF.Labels.replace({True: 1, False: 0})
# normalizedArray = concatenatedNormalizedInputDF.to_numpy()
#
# #X = normalizedDF.iloc[:, 5:]
# X = normalizedArray[:, 5:]
# X = X.astype('float32')
# X = torch.tensor(X, dtype=torch.float32)
# # print('\n X:')
# # print(X)
# #y = normalizedDF.iloc[:, 2]
# y = normalizedArray[:, 2]
# y = y.astype('bool')
# y = torch.tensor(y, dtype=torch.float32)
# # print('\n y:')
# # print(y)
# # print('y shape:', y.shape, ' y ndim:', y.ndim)
#
#
# # train-test split: Hold out the test set for final model evaluation
# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True)
#
# # define 5-fold cross validation test harness
# kfold = StratifiedKFold(n_splits=7, shuffle=True)
# cv_scores = []
# for train, test in kfold.split(X, y):
#     # create model, train, and get accuracy
#     model = Predictor()
#     acc = model_train(model, X[train], y[train], X[test], y[test])
#     print("Accuracy (wide): %.2f" % acc)
#     cv_scores.append(acc)
#
# # evaluate the model
# acc = np.mean(cv_scores)
# std = np.std(cv_scores)
# print("Model accuracy: %.2f%% (+/- %.2f%%)" % (acc * 100, std * 100))
#
#
