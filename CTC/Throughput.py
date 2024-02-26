#This file will contain the class to hold the throughput information and graph it

import matplotlib.pyplot as plt

class Throughput():
    def __init__(self, ScheduleData = []):
        self.left_coordinates=[1]
        self.heights=[0]
        self.bar_labels= ['blue']
        self.colors = ['blue']
        
        self.updateThroughputGraph()


    def updateThroughputGraph(self):
        f = plt.figure()
        #f.set_figwidth(2)
        #f.set_figheight(1)
        
        plt.bar(self.left_coordinates, height = self.heights, tick_label= self.bar_labels, width=0.6, color = self.colors)
        plt.xlabel('Line')
        plt.ylabel('# of Tickets Sold per Hour')
        plt.savefig('CTC/ThroughputGraph.png')

    #Clears the current ticket sale data on the graph
    def clearGraphData(self):
        self.heights=[0]

        self.updateThroughputGraph()
                       

test = Throughput()