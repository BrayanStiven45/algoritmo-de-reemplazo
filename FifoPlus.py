import numpy as np

class FifoPlus:

    def __init__(self, list_process, n_frames: int):

        self.table = np.empty((n_frames, len(list_process)))
        self.list_process = np.array(list_process)
        self.n_frames = n_frames

    def calculate(self):

        self.falls = 0
        second_oportunity = None
        visited = []
        memory = np.full(self.n_frames, None)

        for process in self.list_process:
            
            if process in memory:
                second_oportunity = process
            elif np.any(memory == None):
                j = np.where(memory == None)[0][0]
                memory[j] = int(process)
                self.falls += 1
                visited.append(process)
            elif visited[0] != second_oportunity:
                j = np.where(memory == visited[0])[0][0]
                memory[j] = int(process)
                visited.pop(0)
                visited.append(process)
                self.falls += 1
                second_oportunity = None
            else:
                j = np.where(memory == visited[1])[0][0]
                memory[j] = int(process)
                visited.pop(1)
                visited.append(process)
                self.falls += 1
                second_oportunity = None
            
            print(f'process: {process}, memory: {memory}')
            

fifo = FifoPlus([7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0], 3)
fifo.calculate()
print(f'fallos: {fifo.falls}')

