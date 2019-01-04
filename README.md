# Mnist-Wisard
This is a simple WISARD Neural Network implementation and testing with [MNIST](http://yann.lecun.com/exdb/mnist/) dataset. The article about this repo can be found [here](https://www.researchgate.net/publication/330080182_Avaliacao_da_rede_neural_sem_peso_WISARD_na_base_de_dados_MNIST)

## What do i need?

```
- Python 3.6
- numpy 1.14.5
```

# How can i run it?

After check yours dependencies, you will need to set up your input parameters, for this edit an json file named [Network_Settings.json](Network_Settings.json), where it containd the following fields:

    "result":"result/result.dat"
- *n_inputs_ram* -> this is the number of inputs in each WIZARD RAM
- *examples_samples* -> Number of samples to train you would like to train
- *training_dataset* -> Path mnist files to train
- *testing_dataset* -> Path mnist files to test
- *result* -> file name to save the result

then you just need run [Main.py](Main.py)

> **Optionally:** there is a file [test.py](test.py) where you can make the automatic tests with many settins by time, they will create many files of results, this files you can concatenate running [concatenate.py](concatenate.py) and to complite generate a chart with [plot.gnu](plot.gnu) that use [gnuplot](http://www.gnuplot.info/) to generate the graphic with the results.
