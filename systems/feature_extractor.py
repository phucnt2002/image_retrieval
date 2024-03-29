import numpy as np

from keras.models import Model
from keras.utils import img_to_array
from keras.applications import xception, inception_resnet_v2, vgg19, densenet, mobilenet_v3, nasnet


class Xception_FE:
    def __init__(self) -> None:
        base_model = xception.Xception()  # Create Xception model

        # Create model based on Xception model above
        # With input is the same as Xception model
        # And output results from avg_pool layer of Xception model
        # (None, 299, 299, 3) --> (None, 2048)
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

    def extract(self, image) -> np.ndarray:
        image = image.resize((299, 299))  # Image must be 299 x 299 pixels
        image = image.convert('RGB')  # Image must be color photo

        array = img_to_array(image)  # Image to np.array with shape (299, 299, 3)
        array = np.expand_dims(array, axis=0)  # (299, 299, 3) --> (1, 299, 299, 3)
        array = xception.preprocess_input(array)  # Subtracting average values for each pixel

        feature = self.model.predict(array)[0]  # Predict with shape (1, 2048) --> (2048, )
        feature = feature / np.linalg.norm(feature)  # Normalize

        return feature

class VGG19_FE:
    def __init__(self) -> None:
        base_model = vgg19.VGG19()  # Create VGG16 model

        # Create model based on VGG19 model above
        # With input is the same as VGG19 model
        # And output results from fc1 layer of VGG19 model
        # (None, 224, 224, 3) --> (None, 4096)
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

    def extract(self, image) -> np.ndarray:
        image = image.resize((224, 224))  # Image must be 224 x 224 pixels
        image = image.convert('RGB')  # Image must be color photo

        array = img_to_array(image)  # Image to np.array with shape (224, 224, 3)
        array = np.expand_dims(array, axis=0)  # (224, 224, 3) --> (1, 224, 224, 3)
        array = vgg19.preprocess_input(array)  # Subtracting average values for each pixel

        feature = self.model.predict(array)[0]  # Predict with shape (1, 4096) --> (4096, )
        feature = feature / np.linalg.norm(feature)  # Normalize feature

        return feature

class InceptionResNetV2_FE:
    def __init__(self) -> None:
        base_model = inception_resnet_v2.InceptionResNetV2()  # Create InceptionResNetV2 model

        # Create model based on InceptionResNetV2 model above
        # With input is the same as InceptionResNetV2 model
        # And output results from avg_pool layer of InceptionResNetV2 model
        # (None, 299, 299, 3) --> (None, 1536)
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

    def extract(self, image) -> np.ndarray:
        image = image.resize((299, 299))  # Image must be 299 x 299 pixels
        image = image.convert('RGB')  # Image must be color photo

        array = img_to_array(image)  # Image to np.array with shape (299, 299, 3)
        array = np.expand_dims(array, axis=0)  # (299, 299, 3) --> (1, 299, 299, 3)
        array = inception_resnet_v2.preprocess_input(array)  # Subtracting average values for each pixel

        feature = self.model.predict(array)[0]  # Predict with shape (1, 1536) --> (1536, )
        feature = feature / np.linalg.norm(feature)  # Normalize feature

        return feature

class DenseNet121_FE:
    def __init__(self) -> None:
        base_model = densenet.DenseNet121()  # Create DenseNet121 model

        # Create model based on DenseNet121 model above
        # With input is the same as DenseNet121 model
        # And output results from global_average_pooling2d layer of DenseNet121 model
        # (None, 224, 224, 3) --> (None, 1024)
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

    def extract(self, image) -> np.ndarray:
        image = image.resize((224, 224))  # Image must be 224 x 224 pixels
        image = image.convert('RGB')  # Image must be color photo

        array = img_to_array(image)  # Image to np.array with shape (224, 224, 3)
        array = np.expand_dims(array, axis=0)  # (224, 224, 3) --> (1, 224, 224, 3)
        array = densenet.preprocess_input(array)  # Subtracting average values for each pixel

        feature = self.model.predict(array)[0]  # Predict with shape (1, 1024) --> (1024, )
        feature = feature / np.linalg.norm(feature)  # Normalize feature

        return feature
class MobileNetV3Small_FE:
    def __init__(self) -> None:
        base_model = mobilenet_v3.MobileNetV3Small()  # Create MobileNetV3 Small model

        # Create model based on MobileNetV3 Small model above
        # With input is the same as MobileNetV3 Small model
        # And output results from the global average pooling layer
        # (None, 224, 224, 3) --> (None, 1024)
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('global_average_pooling2d').output)

    def extract(self, image) -> np.ndarray:
        image = image.resize((224, 224))  # Image must be 224 x 224 pixels
        image = image.convert('RGB')  # Image must be color photo

        array = img_to_array(image)  # Image to np.array with shape (224, 224, 3)
        array = np.expand_dims(array, axis=0)  # (224, 224, 3) --> (1, 224, 224, 3)
        array = mobilenet_v3.preprocess_input(array)  # Subtracting average values for each pixel

        feature = self.model.predict(array)[0]  # Predict with shape (1, 1024) --> (1024, )
        feature = feature / np.linalg.norm(feature)  # Normalize feature

        return feature
    

class NasNetMobile_FE:
    def __init__(self) -> None:
        base_model = nasnet.NASNetMobile()  # Create NasNetMobile model

        # Create a model based on NasNetMobile model above
        # With input the same as NasNetMobile model
        # And output results from the global average pooling layer
        # (None, 224, 224, 3) --> (None, 1056)
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('global_average_pooling2d').output)

    def extract(self, image) -> np.ndarray:
        image = image.resize((224, 224))  # Image must be 224 x 224 pixels
        image = image.convert('RGB')  # Image must be a color photo

        array = img_to_array(image)  # Image to np.array with shape (224, 224, 3)
        array = np.expand_dims(array, axis=0)  # (224, 224, 3) --> (1, 224, 224, 3)
        array = nasnet.preprocess_input(array)  # Subtracting average values for each pixel

        feature = self.model.predict(array)[0]  # Predict with shape (1, 1056) --> (1056, )
        feature = feature / np.linalg.norm(feature)  # Normalize feature

        return feature
