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


#tf.constant declare it to its graph, therefore if tf.constant has big data, loading graph to session is going to take overhead.

#tf.constant is an op, but tf.Variable is a class with many ops!



# create variables with tf.get_variable(more prefered)
#s = tf.get_variable("scalar", initializer=tf.constant(2))
#m = tf.get_variable("matrix", initializer=tf.constant([[0, 1], [2, 3]]))
#W = tf.get_variable("big_matrix", shape=(784, 10), initializer=tf.zeros_initializer())


# create variables with tf.Variable(less prefered)
#s = tf.Variable(2, name="scalar")
#m = tf.Variable([[0, 1], [2, 3]], name="matrix")
#W = tf.Variable(tf.zeros([784,10]))

#want to use variable in session, have to initialize it
#           : sess.run(tf.global_variables_initializer())

#print(w.eval()) -> similar to print(sess.run(w))




# W = tf.Variable(10)
# W.assign(100)
# with tf.Session() as sess:
# 	sess.run(W.initializer)
# 	print(W.eval()) 				# >> 10
#
# --------
#
# W = tf.Variable(10)
# assign_op = W.assign(100)
# with tf.Session() as sess:
# sess.run(W.initializer)
# sess.run(assign_op)
# print(W.eval()) 				# >> 100




# # create a variable whose original value is 2
# my_var = tf.Variable(2, name="my_var")
#
# # assign a * 2 to a and call that op a_times_two
# my_var_times_two = my_var.assign(2 * my_var)
#
# with tf.Session() as sess:
# 	sess.run(my_var.initializer)
# 	sess.run(my_var_times_two) 				# >> the value of my_var now is 4
# 	sess.run(my_var_times_two) 				# >> the value of my_var now is 8
# 	sess.run(my_var_times_two) 				# >> the value of my_var now is 16
#





# W = tf.Variable(10)
#
# sess1 = tf.Session()
# sess2 = tf.Session()
#
# sess1.run(W.initializer)
# sess2.run(W.initializer)
#
# print(sess1.run(W.assign_add(10))) 		# >> 20
# print(sess2.run(W.assign_sub(2))) 		# >> 8
#
# print(sess1.run(W.assign_add(100))) 		# >> 120
# print(sess2.run(W.assign_sub(50))) 		# >> -42
#
# sess1.close()
# sess2.close()



# # your graph g have 5 ops: a, b, c, d, e
# g = tf.get_default_graph()
# with g.control_dependencies([a, b, c]):
# 	# 'd' and 'e' will only run after 'a', 'b', and 'c' have executed.
# 	d = ...
# 	e = …



# A TF program often has 2 phases:
#   1. Assemble a graph
#   2. Use a session to execute operations in the graph.


# We, or our clients, can later supply their own data when they need to execute the computation.
#   tf.placeholder(dtype, shape=None, name=None)



# # create a placeholder for a vector of 3 elements, type tf.float32
# a = tf.placeholder(tf.float32, shape=[3])
#
# b = tf.constant([5, 5, 5], tf.float32)
#
# # use the placeholder as you would a constant or a variable
# c = a + b  # short for tf.add(a, b)
#
# with tf.Session() as sess:
# 	print(sess.run(c, feed_dict={a: [1, 2, 3]})) 	# the tensor a is the key, not the string ‘a’
#
# # >> [6, 7, 8]


# Quirk:
# tf.placeholder(dtype, shape=None, name=None)
# shape=None means that tensor of any shape will be accepted as value for placeholder.
# shape=None is easy to construct graphs, but nightmarish for debugging


# You can feed_dict any feedable tensor.
# Placeholder is just a way to indicate that something must be fed
# create operations, tensors, etc (using the default graph)
        # a = tf.add(2, 5)
        # b = tf.multiply(a, 3)
        # with tf.Session() as sess:
        # 	# compute the value of b given a is 15
        # 	sess.run(b, feed_dict={a: 15}) 				# >> 45


#do not lazy load op!
#    a = tf.add(2, 5)
#    b = tf.multiply(a, 3)
#    with tf.Session() as sess:
#    	# compute the value of b given a is 15
#         for _ in range(10):
#        	sess.run(tf.add(a,b))           <- lazy loading : graph makes this op 10 times!! it is non-bug bug!!





