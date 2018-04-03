import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)

writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())

with tf.Session() as sess:
    # writer = tf.summary.FileWriter('./graphs', sess.graph)
    print(sess.run(x))
writer.close() #close the writer when you're done using it

#this code create summary file which is for tensorboard. so after run it, run tensorboard using :
#               $ tensorboard --logdir="./graphs" --port 6006
# go localhost:6006 and check


#if give name parameter to each tensor then can set name of variables which shows on tensorboard.
# ex) a = tf.constant(2, name='a')