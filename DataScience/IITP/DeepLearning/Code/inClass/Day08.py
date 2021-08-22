#%%
import keras
from keras import activations
from keras.utils import np_utils
import numpy as np
import keras
from keras.datasets import imdb, reuters
from keras.preprocessing import sequence
from keras.models import Sequential , Input ,Model
from keras.layers import Dense
from scipy.sparse.sputils import matrix


import tensorflow as tf
from tensorflow.python.keras.layers.embeddings import Embedding
from tensorflow.python.keras.layers.merge import Concatenate
from tensorflow.python.keras.layers.recurrent import LSTM, SimpleRNN
from tensorflow.python.keras.layers.recurrent_v2 import GRU


#%%
# imdb 데이터
(X_train,Y_train), (X_test, Y_test) = imdb.load_data(num_words=1000)
X_train = sequence.pad_sequences(X_train,maxlen=1000)
X_test = sequence.pad_sequences(X_test,maxlen=1000)

# %%
# FC Model
model = Sequential([
    Dense
    (
        32,
        input_dim = X_train.shape[1],
        activation='elu',
        kernel_initializer='he_normal'),
    Dense(
        32,
        activations = 'leaky_relu',
        kernel_initializer='he_normal'),
    Dense(
        1,
        activation = 'sigmoid')    
])
#%%
# Sequential를 이용한 Simple RNN

model = Sequential([
    Embedding(
        X_train.shape[1],
        32,
    ),
    SimpleRNN(32),
    Dense(1,activation= 'sigmoid')       
])
model.summary()
#%%
# Input 을 이용한 Simple RNN

input_a  = Input(shape =X_train.shape[1])
embedding_layer = Embedding(X_train.shape[1], 32)(input_a)
rnn_layer = SimpleRNN(32)(embedding_layer)
fc_layer = Dense(10,activation='elu')(rnn_layer)
output_a = Dense(1,activation='sigmoid')(fc_layer)
model = Model(inputs= [input_a],outputs = [output_a])

model.summary()

#%%
# Input 을 이용한 LSTM
input_a  = Input(shape =X_train.shape[1])
embedding_layer = Embedding(X_train.shape[1], 32)(input_a)
LSTM_layer = LSTM(128, kernel_initializer='he_uniform' )(embedding_layer)
fc_layer = Dense(32,activation='elu')(LSTM_layer)
output_a = Dense(1,activation='sigmoid')(fc_layer)
model = Model(inputs= [input_a],outputs = [output_a])

# model.summary()
#%%
# GRU + LSTM
input_a = Input(shape=X_train.shape[1])
embedding_layer = Embedding(X_train.shape[1],32)(input_a)
gru_layer = GRU(32,activation='tanh')(embedding_layer)
lstm_layer = LSTM(32, kernel_initializer='he_uniform' )(embedding_layer)
merge_layer = Concatenate()([gru_layer , lstm_layer])
fc_layer = Dense(32,activation='elu')(merge_layer)
output_a = Dense(1,activation='sigmoid')(fc_layer)



model = Model(inputs= [input_a],outputs = [output_a])
model.summary()

#%%
model.compile(
    loss = 'binary_crossentropy',
    optimizer = keras.optimizers.RMSprop(learning_rate= 1e-6),
    metrics = ['accuracy']
)
model.fit(
    x = X_train,
    y = Y_train,
    epochs= 10,
    batch_size= 64,
    validation_data=(X_test,Y_test),
    validation_split=.2
)
#%%
with tf.device('/device:GPU:0'):
    model.compile(
        loss = 'binary_crossentropy',
        optimizer = keras.optimizers.RMSprop(learning_rate= 1e-6),
        metrics = ['accuracy']
    )
    model.fit(
        x = X_train,
        y = Y_train,
        epochs= 10,
        batch_size= 64,
        validation_data=(X_test,Y_test),
        validation_split=.2
    )
# %%
# reuters

(X_train,Y_train), (X_test, Y_test) = reuters.load_data(num_words= 1000)
reuter_dict = reuters.get_word_index()
X_train = sequence.pad_sequences(X_train,1000)
X_test = sequence.pad_sequences(X_test,1000)
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

def get_key(val):
    for key,value in reuter_dict.items():
        if val == value:
            return key
    return ''
tmp = []
for i in X_train[0]:
    tmp.append(get_key(i))

#%%
input_ = Input(shape = X_train.shape[1])
fc1 = Dense(128,activation='elu')(input_)
fc2 = Dense(64,activation='elu')(fc1)
output_ = Dense(Y_train.shape[1],activation='softmax')(fc2)

fc_model = Model(inputs = [input_], outputs = [output_])

#%% 
# simple RNN
simple_rnn = Sequential([
    Embedding(X_train.shape[1],64),
    SimpleRNN(32, activation = 'tanh'),
    Dense(64, activation='relu'),
    Dense(Y_train.shape[1], activation='softmax'),
])

# %%
fc_model.compile(
    loss = 'categorical_crossentropy',
    optimizer = tf.keras.optimizers.RMSprop(),
    metrics = ['accuracy']
)

fc_model.fit(
    x = X_train,
    y = Y_train,
    epochs = 10,
    batch_size= 64,
    validation_data=(X_test,Y_test),
    validation_split=.2
)


#%%
Y_train.shape