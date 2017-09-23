
#m __future__ import print_function

import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

hello = tf.constant('Initial Code')
sess = tf.Session()
print(sess.run(hello))
