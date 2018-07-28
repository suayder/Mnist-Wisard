import json, import os

data = {
    "n_inputs_ram":0,
    "examples_samples":0,
    "training_dataset":".",
    "testing_dataset":".",
    "result":"result/result.dat"
}
os.system("mkdir result")
for i in range(9,21):
    for j in range(4000, 16000, 1000):
        data["n_inputs_ram"] = i
        data["examples_samples"] = j
        data["result"] = "result/result"+str(i)+"_"+str(j)+".dat"
        with open("Network_Settings.json", 'w') as setup:
            json.dump(data, outfile)

        os.system('python Main.py')

for i in range(9,21):
    for j in range(20000, 60000, 5000):
        data["n_inputs_ram"] = i
        data["examples_samples"] = j
        data["result"] = "result/result"+str(i)+"_"+str(j)+".dat"
        with open("Network_Settings.json", 'w') as setup:
            json.dump(data, outfile)

        os.system('python Main.py')