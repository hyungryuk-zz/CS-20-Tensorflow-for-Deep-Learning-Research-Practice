# pre installed pip list !
# ipdb (0.11)
# lxml (4.2.1)
# matplotlib (2.2.2)
# Pillow (5.1.0)
# scikit-learn (0.19.1)
# scipy (1.0.1)
# tensorflow-gpu (1.4.0)
# tensorflow-tensorboard (0.4.0)

import tensorflow as tf

a = tf.add(3, 5)
sess = tf.Session()
print(sess.run(a))
sess.close()