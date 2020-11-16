dev_file = "../data/dev_set_task1.txt"
propaganda_techniques_file = "../techniques_list_task1-2.txt" 
task_output_file = "baseline-output-task1-random.txt"

#dev_file = "../data/training_set_task1.txt" 		            # this is to run baseline
#task_output_file = "baseline-output-task1-random-train.txt" 	# on the training set

#
# Baseline task 1: create random labels
#
#

import sys
import json
import random

random.seed(42) # to make runs deterministic

try:
    with open(dev_file, "r") as f:
        jsonobj = json.load(f)
except:
    sys.exit("ERROR: cannot load json file")

with open(propaganda_techniques_file, "r") as f:
    propaganda_techniques_names = [ line.rstrip() for line in f.readlines() if len(line)>2 ]

for example in jsonobj:

    techniques_list = []
    i = 0
    while i < len(propaganda_techniques_names) and random.random() < 0.5:
        techniques_list.append(propaganda_techniques_names[random.randint(0, len(propaganda_techniques_names)-1)])
        i += 1
    example['labels'] = techniques_list
    print("example %s: added %d labels" % (example['id'], i))    

with open(task_output_file, "w") as fout:
    json.dump(jsonobj, fout, indent=4)
print("Predictions written to file " + task_output_file)
