#This file will contain the class to hold the throughput information and graph it

import matplotlib.pyplot as plt

class Throughput():
    def __init__(self, ScheduleData = []):
        self.heights=[0, 0]
        self.bar_labels= ['green', 'red']
        self.colors = ['green', 'red']
        
        self.updateThroughputGraph()


    def updateThroughputGraph(self):
        f = plt.figure()
        #f.set_figwidth(4)
        #f.set_figheight(3)
        
        plt.bar([1], height = self.heights, tick_label= self.bar_labels, width=0.6, color = self.colors)
        plt.title('Throughput')
        plt.xlabel('Line')
        plt.ylabel('# of Tickets Sold per Hour')
        plt.savefig('CTC/ThroughputGraph.png')

    #Clears the current ticket sale data on the graph
    def clearGraphData(self):
        self.heights=[0]

        self.updateThroughputGraph()
                       

test = Throughput()