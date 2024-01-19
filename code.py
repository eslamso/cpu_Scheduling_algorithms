processes=[]
readyQueue=[]
cpu=[]
class Process:
    def __init__(self,name,ariveTime,burstTime):
        self.name = name  ## name of process
        self.ariveTime = ariveTime  ## the time when the process come
        self.burstTime = burstTime  ## burst Time
        self.responseTime = 0  ## the respnse time
        self.outFromCpu = 0  ## the time when the process out from the cpu
        self.waitingTime = 0  ## the time that process wait in the ready Queue
        self.turnAroundTime = 0 ## turn around Time
        self.remainingBurstTime=burstTime  #remaining burst cycle
        self.startTime=[] # the times when the process enter the cpu

    def calcResponseTime(self): # this method used to calculate the response time of a process
        self.responseTime = self.startTime[0]-self.ariveTime
    def setOutFromCpu(self,ot): # this method used to set the attribute outFromCpu to ot
        self.outFromCpu=ot
    def calcTrt(self):     # this method used to calculate the turn Around time of the process
        self.turnAroundTime= self.outFromCpu-self.ariveTime
    def calcWaitingTime(self): # this method used to calculate the watingTime of the process
        self.waitingTime=self.startTime[len(self.startTime)-1]-self.ariveTime
    def decrementBurstTime(self): # in this method the remainmigburstTime is decremented by one which decrease by one each second
        self.remainingBurstTime-=1
    def timeInCpu(self,currentTime): # calculate amount of time for the process in the cpu
        return currentTime-self.startTime[len(self.startTime)-1]
def createProcess(name,at,bt):
    processes.append(Process(name,at,bt))
createProcess('p1',0,5)
createProcess("p2",1,3)
createProcess("p3",2,1)
createProcess("p4",3,2)
createProcess('p5',4,3)



def sortingBurstTime(readyQueue):
        readyQueue.sort(key=lambda el: el.burstTime)
def arrived(time):
    for i in range(len(processes)):
        if processes[i].ariveTime==time:
            readyQueue.append(processes[i])

def printGanntChar(l):
    print("\t\t\t\t GanntChart")
    print_="\t\t\t\t|"
    print__="\t\t\t\t|"
    for i in range(len(l)):
        print_+="--|"
    print(print_)

    for i in range(len(l)):
        print__+=l[i].name+"|"
    print(print__)
    print(print_)
    print('\n')
def result(l):
    ## l is the gannt chart
    total_wt=0
    total_trt=0
    total_rt=0
    results=list(set(l)) # this is to delete the repeatiton of given process
    n=len(results) # number of processes
    results.sort(key=lambda el:el.name) # used to sort the gant chart according the name of the process in it
    print("\t\t\t\t Result Report")
    print("\t\t\t\tname\twt\t\ttrt\t\trt")
    for i in range(n):
        wt = results[i].waitingTime
        rt = results[i].responseTime
        trt = results[i].turnAroundTime
        print("\t\t\t\t"+results[i].name+"\t\t"+str(wt)+"\t\t"+str(trt)+"\t\t"+str(rt))
        total_rt+=rt
        total_trt+=trt
        total_wt+=wt
    print("\t\t\t\tAVG\t\t"+str(total_wt/n)+"\t\t"+str(total_trt/n)+"\t\t"+str(total_rt/n))
def FCFS(processes):
    GanttChart = [] # gannt Chart
    currentProcess=0
    timer=0 # each unit of time (second)
    while (True):
        arrived(timer) ## check if a process arrive in that time or not
        if len( readyQueue) !=0 or currentProcess:## there are processess in ready Queue to be executed or there is current process
            # current process condition mean that its the last process to be executed and the read Queue is empty

                if len(cpu)==1 and cpu[0].remainingBurstTime==0: ## the cpu is busy and the process on it is completed
                        cpu[0].setOutFromCpu(timer)
                        cpu[0].calcWaitingTime()
                        cpu[0].calcTrt()
                        GanttChart.append(cpu.pop(0)) # the process is out from the cpu and placed in the gannt chart


                if len(cpu)==0: ## the cpu is ready to revecive a process
                    if (len(readyQueue) != 0):  ## there are process in the ready queue or not

                        currentProcess = readyQueue.pop(0)
                        currentProcess.startTime.append(timer)
                        currentProcess.calcResponseTime()
                        cpu.append(currentProcess)
                        cpu[0].decrementBurstTime()
                    else:
                        currentProcess = 0  ## there is no current process which mean the cpu is processed all processess
                else  :     ## the process in the cpu is not completed
                    cpu[0].decrementBurstTime() # this condition mean that the current process in the cpu have a remaining busrttime
                                                # and continue in executing
        timer+=1 # ticking the timer
        if (len(GanttChart)==len(processes)):  ## all processess in the processes are processed and that mean to break the loop
           break
    printGanntChar(GanttChart)
    result(GanttChart)
""" 
processes.sort(key=lambda el:el.burstTime)
print(processes[0].name)
print(processes[1].name)
print(processes[2].name)
print(processes[3].name)
"""
def SJF(processes):
    GanttChart = []
    currentProcess=0
    timer=0
    while (True):
        n=len(readyQueue) # the length of the ready Queue before any changing on it
        arrived(timer)
        if len(readyQueue) != n and len(readyQueue)>1: # there are processes enter the readyQueue and the length of the ready not equal 1
            sortingBurstTime(readyQueue) #sorting the process in the ready Queue according the burst Time
        if len( readyQueue) !=0 or currentProcess:

                if len(cpu)==1 and cpu[0].remainingBurstTime==0:
                        cpu[0].setOutFromCpu(timer)
                        cpu[0].calcWaitingTime()
                        cpu[0].calcTrt()
                        GanttChart.append(cpu.pop(0))


                if len(cpu)==0:
                    if (len(readyQueue) != 0):

                        currentProcess = readyQueue.pop(0)
                        currentProcess.startTime.append(timer)
                        currentProcess.calcResponseTime()
                        cpu.append(currentProcess)
                        cpu[0].decrementBurstTime()
                    else:
                        currentProcess = 0
                else  :
                    cpu[0].decrementBurstTime()
        timer+=1
        if (len(GanttChart)==len(processes)):
            break
    printGanntChar(GanttChart)
    result(GanttChart)
"""    
x=str.upper(input('enter FCFS or SJF'))
if x=="FCFS":
 print("FCFS")
 FCFS(processes)
elif x=="SJF":
    print("SJF")
    SJF(processes)
else :
    print('invaid')
"""
def RR(pro,q):
    GanttChart = []
    currentProcess=0
    timer=0
    while (True):
        arrived(timer) ## check if a process arrive in that time or not
        if len( readyQueue) !=0 or currentProcess: ## there are processess in ready Queue to be executed or not

                if len(cpu)==1 : # the cpu is busy
                        if cpu[0].timeInCpu(timer)==q and  cpu[0].remainingBurstTime>0: # check if the process passed time in cpu equal the quantum time Q
                            #and the process has remaining burst Time which mean to out this process from the cpu and put it in the ready Queue and this process isnt completed
                            # and will enter the cpu later
                            cpu[0].setOutFromCpu(timer)

                            p=cpu.pop(0) # out the process from the cpu
                            GanttChart.append(p) # put the process in gannt chart
                            readyQueue.append(p) # put the process
                        elif cpu[0].remainingBurstTime==0: # the process finished its burst time
                            cpu[0].setOutFromCpu(timer)
                            cpu[0].calcTrt()
                            cpu[0].waitingTime=cpu[0].turnAroundTime-cpu[0].burstTime # calculting wating Time
                            p = cpu.pop(0)
                            GanttChart.append(p) # put the process in gantt chart



                if len(cpu)==0: ## the cpu is ready to revecive a process
                    if (len(readyQueue) != 0):  ## there are process in the ready queue
                        currentProcess = readyQueue.pop(0) # take the first process in ready Queue
                        currentProcess.startTime.append(timer) # time when it enter the cpu
                        currentProcess.calcResponseTime() # response Time calculation
                        cpu.append(currentProcess) # put the process in the cpu
                        cpu[0].decrementBurstTime()
                    else:
                        currentProcess = 0  ## there is no current process which mean the cpu is processed all processess
                else  :     ## the process in the cpu is not completed
                    cpu[0].decrementBurstTime()
        timer+=1
        if (currentProcess==0):  ## all processess in the processes are processed and that mean to break the loop
           break
    printGanntChar(GanttChart)
    result(GanttChart)
RR(processes,2)
