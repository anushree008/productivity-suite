trial_file = open("/Users/anushreegovilkar/Documents/SRHIC/UG08/portfolio/trial file.txt","w")
for i in range(10):
    trial_file.write("hi\n")
trial_file = open("/Users/anushreegovilkar/Documents/SRHIC/UG08/portfolio/trial file.txt","r")
print(trial_file.read())
