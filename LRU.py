import numpy as np

class LRU:

    def __init__(self, list_process, n_frames: int):

        self.table = np.empty((n_frames, len(list_process)))
        self.list_process = np.array(list_process)
        self.n_frames = n_frames

    def calculate(self):

        self.falls = 0
        memory = np.full(self.n_frames, None)
        list_process = np.array([])

        for process in self.list_process:
            
            if process in memory:
                list_process = np.append(list_process, process)
                print(f'process: {process}, memory: {memory}')
                continue
                
            if np.any(memory == None):
                j = np.where(memory == None)[0][0]
                memory[j] = int(process)
                self.falls += 1
                list_process = np.append(list_process, process)
            else:
                p = []
                j = None
                for mem in memory:
                    p.append(np.where(mem == list_process)[0][-1])
                

                j = np.argmin(p)

                memory[j] = int(process)
                self.falls += 1
                list_process = np.append(list_process, process)
            
            print(f'process: {process}, memory: {memory}')
            

fifo = LRU([7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0], 3)
fifo.calculate()
print(f'fallos: {fifo.falls}')

