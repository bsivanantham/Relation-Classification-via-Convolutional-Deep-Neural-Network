#
#  Author: Balavivek Sivanantham
#          bsivanantham@techfak.uni-bielefeld.de
#          Universität Bielefeld
#
#  WHAT: This is the official scorer for SemEval-2010 Task #8.
#
#  Last modified: September 16, 2019
#
#  Current version: 1.0
#
#  Use:
#     semeval2010_task8_scorer-v1.1.pl <PROPOSED_ANSWERS> <ANSWER_KEY>
#
#  Example2:
#     semeval2010_task8_scorer-v1.1.pl proposed_answer1.txt answer_key1.txt > result_scores1.txt
#     semeval2010_task8_scorer-v1.1.pl proposed_answer2.txt answer_key2.txt > result_scores2.txt
#     semeval2010_task8_scorer-v1.1.pl proposed_answer3.txt answer_key3.txt > result_scores3.txt
#
#  Description:
#     The scorer takes as input a proposed classification file and an answer key file.
#     Both files should contain one prediction per line in the format "<SENT_ID>	<RELATION>"
#     with a TAB as a separator, e.g.,
#           1	Component-Whole(e2,e1)
#           2	Other
#           3	Instrument-Agency(e2,e1)
#               ...
#     The files do not have to be sorted in any way and the first file can have predictions
#     for a subset of the IDs in the second file only, e.g., because hard examples have been skipped.
#     Repetitions of IDs are not allowed in either of the files.
#
#     The scorer calculates and outputs the following statistics:
#        (1) confusion matrix, which shows
#           - the sums for each row/column: -SUM-
#           - the number of skipped examples: skip
#           - the number of examples with correct relation, but wrong directionality: xDIRx
#           - the number of examples in the answer key file: ACTUAL ( = -SUM- + skip + xDIRx )
#        (2) accuracy and coverage
#        (3) precision (P), recall (R), and F1-score for each relation
#        (4) micro-averaged P, R, F1, where the calculations ignore the Other category.
#        (5) macro-averaged P, R, F1, where the calculations ignore the Other category.
#
#     Note that in scores (4) and (5), skipped examples are equivalent to those classified as Other.
#     So are examples classified as relations that do not exist in the key file (which is probably not optimal).
#
#     The scoring is done three times:
#       (i)   as a (2*9+1)-way classification
#       (ii)  as a (9+1)-way classification, with directionality ignored
#       (iii) as a (9+1)-way classification, with directionality taken into account.
#
#     The official score is the macro-averaged F1-score for (iii).
#