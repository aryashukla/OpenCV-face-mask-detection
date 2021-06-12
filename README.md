# OpenCV-face-mask-detection-using-Haar-Cascade

This Cascade method is quite efficient and theoretically can be used to detect any object. You just have to change the dataset accordinty and train the cascade.

Training description:

Positive Images: Object you want to detect
Negative images: Images of object other than object you want to detect
Given cascade code uses 5000 positive and 2700 negative images to train a Cascade which can detect if a person is wearing a face mask or not.
Images used are just 25X25 in size. Larger dimension images can be used in to increase accuracy but will require more hardware reources.

After training a XML(cascade.xml) file is generated, then mask detection file is used to run that file and detect the object.
