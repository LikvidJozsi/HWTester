import json
import random
import JavaSolution


inps = ["1,2,1","1,1","2,3,2,1","1,4,6,1","3,1","2,6,2,3,4,1"] #make sure output count is 1

to_json = []

to_json.append({"input":"2,3,1\n1,0,-0.5\n0,1,-0.5\n1,1,-1\n2,2,-2,0\n1\n0.75,0.75\n\n"})
to_json.append({"input":"1,1,1\n1,1\n1,1\n1\n-1\n\n"})


for inp in inps:
    sample = {}
    to_json.append(sample)

    input = []
    input.append(inp)
    j = -1
    inpc = -1
    for i in inp.split(","):
        k = int(i)
        if j > 0:
            for m in range(k):
                line = []
                for n in range(j):
                    line.append(str(random.uniform(-10, 10)))
                line.append(str(random.uniform(-10, 10)))
                line = ",".join(line)
                input.append(line)
        else:
            inpc = k
        j = k

    input.append("1") #sample count

    line = []
    for n in range(inpc):
        line.append(str(random.gauss(0, 1)))
    line = ",".join(line)
    input.append(line)

    input.append("\n")
    input = "\n".join(input)
    sample["input"] = input

for sample in to_json:
    sol = JavaSolution.JavaSolution("/home/steve/workspace/MI-HF-NN/src/","/home/steve/workspace/MI-HF-NN/bin/")
    sol.prepare()
    runnable, _ = sol.find_runnable("NNSolutionThree")
    (stdout, stderr, extraerr) = sol.run_java(runnable,sample["input"])
    sample["target"] = stdout

with open("iodata_mihf_nn3.json", "w") as file:
    json.dump(to_json, file, sort_keys=True, indent=4)
