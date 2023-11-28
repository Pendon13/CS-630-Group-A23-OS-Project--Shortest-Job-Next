# Jon Pendon
# A23
#
# For the programming assignment, we would like to implement a process priority protocol called Shortest Job Next.
# It will be a program that first generates a random amount of processes and their times.
# For a process, a simple read/write program will be used.
# Times can be varied using sleep functions to simulate I/O waits.
# The OS simulator will take these programs and sort them from shortest to longest job.
# It will then run the program.
# The programs will be written down in a log file to know which programs were
# generated and which programs ran first.
#

import datetime, time, random
from pathlib import Path

class Job:

    def __init__(self, filename, jobtype, linecount):
        # random burst time variable from 0 to 5000 ms
        # simulates random slow i/o
        randomtime = random.randrange(0,5000)
        # how many lines to write
        self.lines = linecount
        # how long the process will run for
        self.bursttime = linecount + randomtime
        # Job Identifiers
        self.path = "./jobs/"
        self.filename = filename
        self.file = self.path + filename
        self.jobtype = jobtype

        # Check for log and job folder
        Path("./logs").mkdir(parents=True, exist_ok=True)
        Path("./jobs").mkdir(parents=True, exist_ok=True)

        self.log("Job Created")

    # Log function
    def log(self, text):
        logfile = open("./logs/" + str(datetime.date.today()) + ".txt", 'a')
        logfile.write("[" + str(datetime.datetime.now()) +"]: " + "Filename: " + str(self.filename) + ", Line Count: " + str(self.lines) +  ", Time: " + str(self.bursttime) + ", Type: " + str(self.jobtype) + ", " + text)
        logfile.write("\n")
        logfile.close()
    
    # Complete the Job
    def complete(self):
        self.log("Job Started")
        if self.jobtype == "write":
            self.filewrite()
        if self.jobtype == "read":
            self.fileread()
        self.log("Job Ended")

    # Write Function
    # Trys to read the file given. If the file does not exist, it starts the write operation. If it does exist it returns an error.
    def filewrite(self):
        count = 0
        try:
            # The file exists
            file = open(self.file,'r')
            file.close()
            self.log("Job Failure: File Already Written")
            # self.fileread()
        except:
            file = open(self.file, 'w')
            for i in range(self.bursttime):
                file.write(str(i)+"\n")
                count += 1
                time.sleep(0.001)
            file.close()
            self.log("Job Completed")
        # Complete burst time.
        if count < self.bursttime:
            time.sleep(float((self.bursttime/1000 - count/1000)))
    
    def fileread(self):
        count = 0
        try:
            file = open(self.file,"r")
            for line in file:
                count+=1
                time.sleep(0.001)
            file.close()
            self.log("Job Completed")
        except:
            # The file does not exist
            self.log("Job Failure: File Not Found")
            # self.filewrite()
        # Complete Burst Time
        if count < self.bursttime:
            time.sleep(float((self.bursttime/1000 - count/1000)))

jobone = Job("jobone.txt", "write", 100)
jobtwo = Job("jobtwo.txt", "write", 200)

# use this function to get the time it takes to run the job
jobtwotime = jobtwo.__getattribute__("bursttime")
jobtwotimetwo = jobtwo.__getattribute__("bursttime")
print(jobtwotime)
jobtwo.complete()
jobone.complete()
print(jobtwotimetwo)
