#----------------------------------------------------------------------------------------------------------------------
#  Authors: Mohith Bhargav Sunkara, Balavivek Sivanantham and Noureldin Alaa
#          msunkara@techfak.uni-bielefeld.de, bsivanantham@techfak.uni-bielefeld.de, nbadr@techfak.uni-bielefeld.de
#          Bielefeld University
#----------------------------------------------------------------------------------------------------------------------
import sys
import time

import tensorflow as tf

from models import cnn_model
from reader import base as base_reader


flags = tf.app.flags

flags.DEFINE_string("train_file", "data/train.cln", "original training file")
flags.DEFINE_string("test_file", "data/test.cln", "original test file")

flags.DEFINE_string("vocab_file", "data/vocab.txt", "vocab of train and test data")

flags.DEFINE_string("senna_embed50_file", "data/embed50.senna.npy", "senna words embeddding")
flags.DEFINE_string("senna_words_file", "data/senna_words.lst", "senna words list")
flags.DEFINE_string("trimmed_embed50_file", "data/embed50.trim.npy", "trimmed senna embedding")

flags.DEFINE_string("train_record", "data/train.tfrecord", "training file of TFRecord format")
flags.DEFINE_string("test_record", "data/test.tfrecord", "Test file of TFRecord format")

flags.DEFINE_string("relations_file", "data/relations.txt", "relations file")
flags.DEFINE_string("results_file", "data/results.txt", "predicted results file")
flags.DEFINE_string("logdir", "saved_models/", "where to save the model")

flags.DEFINE_integer("max_len", 96, "max length of sentences")
flags.DEFINE_integer("num_relations", 19, "number of relations")
flags.DEFINE_integer("word_dim", 50, "word embedding size")
flags.DEFINE_integer("num_epochs", 200, "number of epochs")
flags.DEFINE_integer("batch_size", 100, "batch size")

flags.DEFINE_integer("pos_num", 123, "number of position feature")
flags.DEFINE_integer("pos_dim", 5, "position embedding size")
flags.DEFINE_integer("num_filters", 100, "cnn number of output unit")

flags.DEFINE_float("lrn_rate", 1e-3, "learning rate")
flags.DEFINE_float("keep_prob", 0.5, "dropout keep probability")

flags.DEFINE_boolean('test', False, 'set True to test')
flags.DEFINE_boolean('trace', False, 'set True to test')

FLAGS = tf.app.flags.FLAGS


def train(sess, m_train, m_valid):
    n = 1
    best = .0
    best_step = n
    start_time = time.time()
    orig_begin_time = start_time

    fetches = [m_train.train_op, m_train.loss, m_train.accuracy]

    while True:
        try:
            _, loss, acc = sess.run(fetches)

            epoch = n // 80
            if n % 80 == 0:
                now = time.time()
                duration = now - start_time
                start_time = now
                v_acc = sess.run(m_valid.accuracy)
                if best < v_acc:
                    best = v_acc
                    best_step = n
                    m_train.save(sess, best_step)
                print("Epoch %d, loss %.2f, TrainingAccuracy %.2f ValidationAccuracy %.2f, time %.2f" %
                      (epoch, loss, acc * 100, v_acc * 100, duration))
                sys.stdout.flush()
            n += 1
        except tf.errors.OutOfRangeError:
            break

    duration = time.time() - orig_begin_time
    duration /= 3600
    print('Done training, best_step: %d, best_acc: %.4f' % (best_step, best))
    print('duration: %.2f hours' % duration)
    sys.stdout.flush()


def test(sess, m_valid):
    m_valid.restore(sess)
    fetches = [m_valid.accuracy, m_valid.prediction]
    accuracy, predictions = sess.run(fetches)
    print('accuracy: %.4f' % accuracy)

    base_reader.write_results(predictions, FLAGS.relations_file, FLAGS.results_file)


def main(_):
    with tf.Graph().as_default():
        train_data, test_data, word_embed = base_reader.inputs()

        m_train, m_valid = cnn_model.build_train_valid_model(word_embed,
                                                             train_data, test_data)

        m_train.set_saver('cnn-%d-%d' % (FLAGS.num_epochs, FLAGS.word_dim))

        init_op = tf.group(tf.global_variables_initializer(),
                           tf.local_variables_initializer())

        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True

        with tf.Session(config=config) as sess:
            sess.run(init_op)
            print('=' * 80)

            if FLAGS.test:
                test(sess, m_valid)
            else:
                train(sess, m_train, m_valid)


if __name__ == '__main__':
    __all__ = [base_reader, cnn_model]
    tf.app.run()
