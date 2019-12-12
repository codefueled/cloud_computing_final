from flask import flash, request, Flask, jsonify
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
            model_loss = request.args.get('loss', '')
            model_optimizer = request.args.get('optimizer', '')
            model_epochs = request.args.get('epochs', '')
            model_batch_size = request.args.get('batch_size', '')
            model_dropout = request.args.get('dropout', '')
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
            model.add(Conv2D(32, kernel_size = (3, 3), activation='relu', input_shape=(32, 32, 3)))
            model.add(MaxPooling2D(pool_size=(2,2)))
            model.add(BatchNormalization())
            model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
            model.add(MaxPooling2D(pool_size=(2,2)))
            model.add(BatchNormalization())
            model.add(Conv2D(32, kernel_size=(3,3), activation='relu'))
            model.add(MaxPooling2D(pool_size=(2,2)))
            model.add(BatchNormalization())
            model.add(Dropout(float(model_dropout)))
            model.add(Flatten())
            model.add(Dense(128, activation='relu'))
            #model.add(Dropout(0.3))
            model.add(Dense(10, activation = 'softmax'))

            #Compile
            model.compile(loss= model_loss,
            optimizer= model_optimizer,
            metrics=['accuracy'])

            #Fit data
            seqModel = model.fit(x_train, y_train, epochs= int(model_epochs), validation_data=(x_test, y_test), batch_size = int(model_batch_size))
            train_loss = seqModel.history['loss']
            val_loss = seqModel.history['val_loss']
            train_acc = seqModel.history['acc']
            val_acc = seqModel.history['val_acc']
            response_str = "Train Loss: " + str(train_loss) + " Val Loss: " + str(val_loss) + " Train Acc: " + str(train_acc) + " Val Acc: " + str(val_acc)
            response = jsonify({
                "statusCode": 200,
                "status": "Model Created",
                "result": response_str
            })
            return response
        except Exception as e:
            print(e)


app.add_resource(PredictModel, '/model')

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=80, debug=True)
