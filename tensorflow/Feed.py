import os
import time
import tensorflow as tf
from tensorflow.contrib.compiler import jit
os.environ['CUDA_VISIBLE_DEVICES'] = ''
print (os.getpid())

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
jit_scope = jit.experimental_jit_scope
with jit_scope(compile_ops=True):
	output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print (sess.run([output], feed_dict={input1:[7.,2.0], input2:[2.,3.0]}))
