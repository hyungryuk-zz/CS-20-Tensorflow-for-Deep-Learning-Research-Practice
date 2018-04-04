#Linear Regression Starter Tutorial

# STEPS for Linear Regression!!
# 1. Read in date
# 2. Create placeholders for inputs and labels



import tensorflow as tf

def read_birth_life_data(filename):
    """
    Read in birth_life_2010.txt and return:
    data in the form of NumPy array
    n_samples: number of samples
    """
    text = open(filename, 'r').readlines()[1:]
    data = [line[:-1].split('\t') for line in text]
    births = [float(line[1]) for line in data]
    lifes = [float(line[2]) for line in data]
    data = list(zip(births, lifes))
    n_samples = len(data)
    data = np.asarray(data, dtype=np.float32)
    return data, n_samples

DATA_FILE = 'data/birth_life_2010.txt'

data, n_samples = read_birth_life_data(DATA_FILE)


X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')

w = tf.get_variable("weights", initializer=tf.constant(0.0))
b = tf.get_variable("bias", initializer=tf.constant(0.0))

Y_predicted =