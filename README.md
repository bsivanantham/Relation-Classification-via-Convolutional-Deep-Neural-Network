## Relation Classification via Convolutional Deep Neural Network

Implementation of [the paper](http://www.aclweb.org/anthology/C14-1220).

Dataset Used: SemEval2010 task8.

Word Embeddings: senna.


## Environment
- OS: linux.
- Python: python 3.6.
- FrameWork: Tensorflow 1.4.0.
- Virtual Environment: virtualenv 15.1.0
- Installation File: requirements.txt

## Installation:

```bash
1. git clone https://github.com/bsivanantham/Relation-Classification-via-Convolutional-Deep-Neural-Network.git
2. cd Relation-Classification-via-Convolutional-Deep-Neural-Network
3. sudo apt install virtualenv
4. virtualenv --python=python3.6 venv
               or python3 venv
5. source venv/bin/activate
6. pip install -r requirements.txt
- To deactivate the virtual environment:
7. deactivate
```

## Train, Test and Calculate

- To train model

    `python train.py  --num_epochs=200 --word_dim=50`
    
- To test model
 
    `python train.py  --num_epochs=200 --word_dim=50 --test`

    --> This will generate the 'results.txt' file in ```/data/results.txt```.

- To calculate and get Classification Report, Accuracy, Precision, Recall and F1 score

    `python scorer.py data/test_keys.txt data/results.txt`



