import tensorflow as tf

@tf.custom_gradient
def grad_reverse(x, scale=0.2):
#def grad_reverse(x, scale=1.):
    y = tf.identity(x)
    def custom_grad(dy):
        return -dy * scale
    return y, custom_grad

class GradReverseTR(tf.keras.layers.Layer):
    def __init__(self):
        super(GradReverseTR, self).__init__()

    def call(self, x):
        return grad_reverse(x)
