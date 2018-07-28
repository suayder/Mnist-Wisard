import glob,json
import math

import Mnist
from Wisard import *

from collections import OrderedDict
from operator import itemgetter

#--------Reading hiper-parameters from json--------#

with open('Network_Settings.json') as jsonfile:
    settings = json.load(jsonfile)

n_inputs_ram = settings['n_inputs_ram']
path_train = settings['training_dataset']
path_test = settings['testing_dataset']
result = settings['result']
train_exemples = settings['examples_samples']

#------------------------Training Routine------------------------#

#Instance of neural network
wisard = {}

controller = 0

for i in range(0,10):
    wisard[i] = Wisard(math.floor(784/n_inputs_ram), n_inputs_ram)

training_dataset =  list(Mnist.read(dataset = 'training', path=path_train))

for i in training_dataset:
    label, array = i
    array = Mnist.binarize_array(array)
    (wisard[label]).train(array)
    if(controller == train_exemples):
        break
    controller+=1

#------------------------Testing Routine------------------------#

testing_dataset =  list(Mnist.read(dataset = 'testing', path=path_test))
triggered_rams = {}

hit_number = 0
failure_number = 0

for i in testing_dataset:
    label, array = i
    array = Mnist.binarize_array(array)
    for j in range(0,10):
        triggered_rams[j] = wisard[j].classify(array)

    sorted_dict = OrderedDict(sorted(triggered_rams.items(), key = itemgetter(1), reverse = True))
    keys = list(sorted_dict.keys())
    if keys[0] == label:
        hit_number+=1
    else:
        failure_number+=1

result = open(result, 'w')
result.write("#Hits\tFailures\n")
result.write("{0}\t{1}".format(hit_number,failure_number))
result.close()

print("Hit Number: ", hit_number)
print("Failure Number: ", failure_number)