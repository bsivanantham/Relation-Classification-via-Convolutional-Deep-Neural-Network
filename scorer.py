#----------------------------------------------------------------------------------------------------------------------
#  Authors: Mohith Bhargav Sunkara, Balavivek Sivanantham and Noureldin Alaa
#          msunkara@techfak.uni-bielefeld.de, bsivanantham@techfak.uni-bielefeld.de, nbadr@techfak.uni-bielefeld.de
#          Bielefeld University
#----------------------------------------------------------------------------------------------------------------------
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
import sys

def caluclator(TrueList, PredList):
    y_true = TrueList
    y_pred = PredList

    AllTarget_names = ['Cause-Effect', 'Component-Whole', 'Content-Container', 'Entity-Destination', 'Entity-Origin', 'Instrument-Agency', 'Member-Collection', 'Message-Topic', 'Product-Producer', '_Other']
    final_classificationReport = classification_report(y_true, y_pred, target_names=AllTarget_names)
    Target_names = ['Cause-Effect', 'Component-Whole', 'Content-Container', 'Entity-Destination', 'Entity-Origin', 'Instrument-Agency', 'Member-Collection', 'Message-Topic', 'Product-Producer']
    final_accuracy = accuracy_score(y_true, y_pred)
    final_precision = precision_score(y_true, y_pred, average='macro', labels=Target_names)
    final_recall = recall_score(y_true, y_pred, average='macro', labels=Target_names)
    final_f1score = f1_score(y_true, y_pred, average='macro', labels=Target_names)
    print("-----------------------------------------------")
    print("---------------Result Table--------------------")
    print("-----------------------------------------------")
    print("Classification Report for all the categories including _Other")
    print("-----------------------------------------------")
    print(final_classificationReport)
    print("-----------------------------------------------")
    print("-----------------------------------------------")
    print("Accuracy and Macro-averaged P, R, F1 excluding _Other category")
    print('Accuracy: \t %f \n' % final_accuracy)
    print('Precision: \t %f \n' % final_precision)
    print('Recall: \t %f \n' % final_recall)
    print('F1 score: \t %f \n' % final_f1score)
    print("-----------------------------------------------")
    print("-----------------------------------------------")


def main(argv):
    testkeys_file = argv[0]
    result_file = argv[1]
    print("The given input files are" + ":" + "\t" + "Testkeys_file" + " " + "=" + " " + testkeys_file + " " + "and" + " " + "result_file" + " " + "=" + " " + result_file)

    result_file_list = []
    testkeys_file_list = []

    # opening and reading the file1 - Result file
    file_1 = open(result_file, "r")
    for x in file_1:
        my_string = x
        step_0 = my_string.split('\t')
        step_1 = step_0[1]
        step_2 = step_1.strip('\n')
        if '(e1,e2)' in step_2:
            step_3 = step_2.split('(e1,e2)')
            step_4 = step_3[0]
            step_5 = step_4
            result_file_list.append(step_5)
        if '(e2,e1)' in step_2:
            step_3 = step_2.split('(e2,e1)')
            step_4 = step_3[0]
            step_5 = step_4
            result_file_list.append(step_5)
        if step_2 == 'Other':
            result_file_list.append('_Other')
    file_1.close()

    # opening and reading the file2 - Original Key file
    file_2 = open(testkeys_file, "r")
    for x in file_2:
        my_string = x
        step_0 = my_string.split('\t')
        step_1 = step_0[1]
        step_2 = step_1.strip('\n')
        if '(e1,e2)' in step_2:
            step_3 = step_2.split('(e1,e2)')
            step_4 = step_3[0]
            step_5 = step_4
            testkeys_file_list.append(step_5)
        if '(e2,e1)' in step_2:
            step_3 = step_2.split('(e2,e1)')
            step_4 = step_3[0]
            step_5 = step_4
            testkeys_file_list.append(step_5)
        if step_2 == 'Other':
            testkeys_file_list.append('_Other')
    file_2.close()

    caluclator(testkeys_file_list, result_file_list)

if __name__ == '__main__':
    main(sys.argv[1:])
