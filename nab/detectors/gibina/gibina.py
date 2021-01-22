#---------------------------------------------------

import math
import numpy
import random
from nab.detectors.base import AnomalyDetector
from Data.Text import Data_gather


def normalProbability1(x, mean, std):
  
  if x < mean:
    # Gaussian is symmetrical around mean, so flip to get the tail probability
    xp = 2*mean - x
    return normalProbability1(xp, mean, std)

  # Calculate the Q function with the complementary error function, explained
  # here: http://www.gaussianwaves.com/2012/07/q-function-and-error-functions
  z = (x - mean) / std
  return 0.5 * math.erfc(z/math.sqrt(2))

class JibinaDetector(AnomalyDetector):
  

  def __init__(self, *args, **kwargs):
    super(JibinaDetector, self).__init__(*args, **kwargs)

    self.windowSize = random.randint(800,1500)
    self.windowData = []
    self.stepBuffer = []
    self.stepSize = random.randint(500,800)
    self.mean = 0
    self.std = 1


  def handleRecord(self, inputData):
    """Returns a tuple (anomalyScore).
    The anomalyScore is the tail probability of the gaussian (normal) distribution
    over a sliding window of inputData values. The tail probability is based on the
    Q-function. The windowSize has been tuned to give best performance on NAB.
    """
    tempt = 0
    anomalyScore = 0.0
    inputValue = inputData["value"]
    if len(self.windowData) > 0:
      anomalyScore = 1 - normalProbability1(inputValue, self.mean, self.std)

    if len(self.windowData) < self.windowSize:
      self.windowData.append(inputValue)
      self._updateWindow()
    else:
      self.stepBuffer.append(inputValue)
      if len(self.stepBuffer) == self.stepSize:
        # slide window forward by stepSize
        self.windowData = self.windowData[self.stepSize:]
        self.windowData.extend(self.stepBuffer)
        # reset stepBuffer
        self.stepBuffer = []
        self._updateWindow()
    
    Data_gather.window(self.windowSize)
    Data_gather.Step_Size(self.stepSize)
    tempt = 1
    return (anomalyScore, )


  def _updateWindow(self):
    self.mean = numpy.mean(self.windowData)
    self.std = numpy.std(self.windowData)
    if self.std == 0.0:
      self.std = 0.000001

