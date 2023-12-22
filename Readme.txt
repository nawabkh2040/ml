# Eye Disease Classifier

## Overview:
Eye Disease Classifier is a program that uses deep learning to classify eye images into different disease categories. The program is built using TensorFlow and Keras, and it leverages the Xception model for image classification.

## Contents:
1. `ml.py`: The main script containing the model architecture, training, and prediction functions.
2. `requirements.txt`: List of required Python packages for running the program.
3. `data/`: Directory to store your training and testing datasets.
4. `images/`: Directory to store images for predictions.

## How to Use:
1. Install the required packages in a Env file :



2. Prepare your dataset:
- Place your eye images in the `data/training` and `data/testing` directories.
- Ensure images are organized into subdirectories based on their classes.

3. Train the model:
- Run the `ml.py` script to train the eye disease classifier model:
  ```
  python ml.py
  ```

4. Make predictions:
- After training, you can use the trained model to make predictions on new eye images. Place the images in the `images/` directory and run:
  ```
  python ml.py predict images/image.jpg
  ```

## Notes:
- Adjust hyperparameters, such as batch size, image size, and model architecture, in `ml.py` based on your specific requirements.
- Experiment with different preprocessing techniques to improve model performance.
- Monitor the training process and adjust early stopping parameters if needed.

Enjoy using the Eye Disease Classifier!
