# from cs231 class notes of Stanford University
# Stanford Universitesinin cs231 dersinin notlarindan

from data_utils import load_CIFAR10
import numpy as np

class NearestNeighbor(object):
    def __init__(self, data_limit):
    	self.data_limit = data_limit
        pass

    def train(self, X, y):
        """ X is N x D where each row is an example. Y is 1-dimension of size N """
        # the nearest neighbor classifier simply remembers all the training data
        self.Xtr = X
        self.ytr = y

    def predict(self, X):
        """ X is N x D where each row is an example we wish to predict label for """
        num_test = X.shape[0]
        # lets make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype = self.ytr.dtype)

        # for a quicker experiment (also note the change in the accuracy line Yte[:data_limit])
        if data_limit != 0:
        	num_test = self.data_limit
        # loop over all test rows
        for i in xrange(num_test):
            print(i)
            # find the nearest training image to the i'th test image
            # using the L1 distance (sum of absolute value differences)
            distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)
            min_index = np.argmin(distances) # get the index with smallest distance
            Ypred[i] = self.ytr[min_index] # predict the label of the nearest example

        return Ypred

data_limit = 100

Xtr, Ytr, Xte, Yte = load_CIFAR10('/home/ubuntu/data/cifar/cifar-10-batches-py')
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3) # Xtr_rows becomes 50000 x 3072
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3) # Xte_rows becomes 10000 x 3072

nn = NearestNeighbor(data_limit) # create a Nearest Neighbor classifier class
nn.train(Xtr_rows, Ytr) # train the classifier on the training images and labels
Yte_predict = nn.predict(Xte_rows) # predict labels on the test images
# and now print the classification accuracy, which is the average number
# of examples that are correctly predicted (i.e. label matches)
print 'accuracy: %f' % ( np.sum(Yte_predict[:data_limit] == Yte[:data_limit]) )