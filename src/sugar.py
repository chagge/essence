
def portal(self, shape = (0,)):
    return self._x('portal', shape)

def variable(self, val, trainable = True):
    return self._x('variable', val, trainable)

def lookup(self, val, pos, trainable = True):
    return self._x('lookup', val, pos, trainable)

def constant(self, val):
    return self._x('const', val)

def conv2d(self, x, kernel, pad = (0, 0), stride = (1, 1)):
    return self._x('conv', x, kernel, pad, stride)

def maxpool2(self, x):
    return self._x('maxpool2', x)

def lstm1(self, x, lens, hidden_size, forget_bias = None):
    return self._x('lstm_uni', x, lens, hidden_size, forget_bias)

def matmul(self, x, w):
    return self._x('dot', x, w)

def relu(self, x):
    return self._x('relu', x)

def plus_b(self, x, b):
    return self._x('bias', x, b)

def softmax_crossent(self, x, t):
    return self._x('softmax_crossent', x, t)

def batch_norm(self, x, gamma, is_training, momentum = .9):
    return self._x('batchnorm', x, gamma, is_training, momentum)

def reshape(self, x, new_shape):
    return self._x('reshape', x, new_shape)

def dropout(self, x, keep_prob):
    return self._x('drop', x, keep_prob)

def sigmoid(self, x):
    return self._x('softmax', x)

def crossent(self, x):
    return self._x('crossent', x)

def softmax(self, x):
    return self._x('softmax', x)

def l2_regularize(self, w, center = 0.):
    return self._x('l2', w, center)

def weighted_loss(self, *pairs):
    losses, weights = zip(*pairs)
    return self._x('weighted_loss', weights, *losses)