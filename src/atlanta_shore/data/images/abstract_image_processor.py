"""An abstract image processing class.

We need to extract different things from the images, such as the amount of canopy cover
or ground cover.  This list of things is likely to increase to so keep them all
separate I plan to use a strategy pattern."""
import abc

import numpy


class AbstractImageProcessing(abc.ABC):
    """"""

    def __init__(self, image: numpy.array):
        """Initialize the processor with the image as an a"""
        self.image = image

    @abc.abstractmethod
    def extract(self):
        """Extract the information of interest from the image."""
        pass
