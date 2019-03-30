# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from LossFunction import *
from WeightsBias import *

# this class is for two-layer NN only
class CParameters(object):
    def __init__(self, n_input, n_hidden, n_output, 
                 eta=0.1, max_epoch=10000, batch_size=5, eps = 0.1, 
                 lossFuncName = LossFunctionName.MSE,
                 initMethod = InitialMethod.Xavier):

        self.num_input = n_input
        self.num_hidden = n_hidden
        self.num_output = n_output

        self.eta = eta
        self.max_epoch = max_epoch
        # if batch_size == -1, it is FullBatch
        if batch_size == -1:
            self.batch_size = self.num_example
        else:
            self.batch_size = batch_size
        # end if
        self.loss_func_name = lossFuncName
        self.init_method = initMethod
        self.eps = eps

    def toString(self):
        title = str.format("bz:{0},eta:{1}", self.batch_size, self.eta)
        return title

