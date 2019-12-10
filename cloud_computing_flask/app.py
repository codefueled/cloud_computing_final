from flask import flash, request, Flask
from flask_restplus import Api, Resource, fields
from keras.utils import to_categorical
from keras.datasets import cifar10
from keras import backend as K
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Flatten, Dropout, Dense
from flask_cors import CORS


flask_app = Flask(__name__)
CORS(flask_app)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "ML Flask App", 
		  description = "Predict results using a trained model")

class PredictModel(Resource):
    def get(self):
        try:
            model_params = request.args.get('data', '')
            (x_train, y_train), (x_test, y_test) = cifar10.load_data()

            y_train = to_categorical(y_train)
            y_test = to_categorical(y_test)
            #Process and Normalize Images
            x_train = x_train.astype('float32')
            x_test = x_test.astype('float32')
            x_train = x_train / 255.0
            x_test = x_test / 255.0

            #ML Model Structure
            model = Sequential()
            model.add(Conv2D(32, kernel_size = (3, 3), activation='relu', input_shape=(32, 32, 1)))
            model.add(MaxPooling2D(pool_size=(2,2)))
            model.add(BatchNormalization())
            model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
            model.add(MaxPooling2D(pool_size=(2,2)))
            model.add(BatchNormalization())
            model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
            model.add(MaxPooling2D(pool_size=(2,2)))
            model.add(BatchNormalization())
            model.add(Conv2D(96, kernel_size=(3,3), activation='relu'))
            model.add(MaxPooling2D(pool_size=(2,2)))
            model.add(BatchNormalization())
            model.add(Conv2D(32, kernel_size=(3,3), activation='relu'))
            model.add(MaxPooling2D(pool_size=(2,2)))
            model.add(BatchNormalization())
            model.add(Dropout(0.2))
            model.add(Flatten())
            model.add(Dense(128, activation='relu'))
            #model.add(Dropout(0.3))
            model.add(Dense(10, activation = 'softmax'))
            
            #Fit data
            model.fit(x_train, y_train, epochs=8, validation_data=(x_test, y_test))
            return 1
        except Exception as e:
            print(e)


app.add_resource(PredictModel, '/model')

if __name__ == "__main__":
    flask_app.run(debug=True)