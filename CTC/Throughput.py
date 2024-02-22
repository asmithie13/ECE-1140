#This file will contain the class to hold the throughput information and graph it

import matplotlib.pyplot as plt

class Throughput():
    def __init__(self, ScheduleData = []):
        self.left_coordinates=[1,2,3]
        self.heights=[10,20,30]
        self.bar_labels= ['blue', 'green', 'red']
        self.colors = ['blue', 'green', 'red']
        
        self.updateThroughputGraph()


    def updateThroughputGraph(self):
        plt.bar(self.left_coordinates, height = self.heights, tick_label= self.bar_labels, width=0.6, color = self.colors)
        plt.xlabel('Line')
        plt.ylabel('# of Tickets Sold per Hour')
        plt.title("Throughput of System")
        plt.savefig('CTC/ThroughputGraph.jpeg')
        #plt.show()

    def clearGraphData(self):
        self.left_coordinates = []
        self.heights=[]
        self.bar_labels= []
        self.colors = []

        self.updateThroughputGraph()
                       

test = Throughput()