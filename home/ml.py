# ml.py
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.applications.xception import preprocess_input
import numpy as np

def load_and_compile_model(batch_size=32, subset_fraction=1.0):
    # Define the ImageDataGenerator for training data
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=1.0 - subset_fraction  # Use a subset of the training data
    )

    # Set the paths to your training and testing directories
    training_dir = r'C:\Users\HP\Desktop\ml_project\eye\preprocessed dataset\preprocessed dataset\training'
    testing_dir = r'C:\Users\HP\Desktop\ml_project\eye\preprocessed dataset\preprocessed dataset\testing'

    # Generate batches of data for training and testing sets
    training_set = train_datagen.flow_from_directory(
        training_dir,
        target_size=(299, 299),
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'  # Use the training subset
    )

    imageSize = [299, 299]
    xception = Xception(input_shape=imageSize + [3], weights='imagenet', include_top=False)

    for layer in xception.layers:
        layer.trainable = False

    x = Flatten()(xception.output)
    prediction = Dense(5, activation='softmax')(x)

    model = Model(inputs=xception.input, outputs=prediction)

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model, training_set

def train_model(model, training_set, epochs=5):
    # Train the model
    model.fit(training_set, epochs=epochs)

def make_predictions(model, img_path):
    # Preprocess the image
    img = load_img(img_path, target_size=(299, 299))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make predictions
    predictions = model.predict(img_array)

    return predictions
