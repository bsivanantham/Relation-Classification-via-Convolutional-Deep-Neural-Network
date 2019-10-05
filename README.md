## Relation Classification via Convolutional Deep Neural Network

TensorFlow implementation of [the paper](http://www.aclweb.org/anthology/C14-1220),

dataset: SemEval2010 task8

word embeddings: senna


## Environment
- tensorflow 1.4.0
- python 3.5
- linux,macOs or windows

## How to run ?

- to train model

    `python3 train.py  --num_epochs=200 --word_dim=50`
    
-  to test model
 
    `python src/train.py  --num_epochs=200 --word_dim=50 --test`

    then you can get a 'results.txt'  file in ```/data/resuts.txt```

- to calculate F1 score

    ```python scorer.py data/test_keys.txt data/results.txt```



