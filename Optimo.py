import numpy as np

# class Optimo:

#     def __init__(self, list_process, n_frames: int):

#         self.table = np.empty((n_frames, len(list_process)))
#         self.list_process = np.array(list_process)
#         self.n_frames = n_frames

#     def calculate(self):

#         self.falls = 0
#         memory = np.full(self.n_frames, None)
#         list_process = self.list_process

#         for process in self.list_process:
            
#             if process in memory:
#                 list_process = np.delete(list_process,0)
#                 print(f'process: {process}, memory: {memory}')
#                 continue
                
#             if np.any(memory == None):
#                 j = np.where(memory == None)[0][0]
#                 memory[j] = int(process)
#                 self.falls += 1
#                 list_process = np.delete(list_process,0)
#             else:
#                 p = []
#                 j = None
#                 for mem in memory:
#                     if mem in list_process:
#                         p.append(np.where(list_process == mem)[0][0])
#                     else:
#                         p.append(len(list_process))
#                         break
                
#                 j = np.argmax(p)

#                 memory[j] = int(process)
#                 self.falls += 1
#                 list_process = np.delete(list_process,0)
            
#             print(f'process: {process}, memory: {memory}')
            

# fifo = Optimo([6, 1, 7, 1, 2, 1, 5, 6, 0, 1, 7, 1, 1, 6, 0, 7, 0, 1, 2, 6, 1], 4)
# fifo.calculate()
# print(f'fallos: {fifo.falls}')

class Optimo:
    def __init__(self, list_process, n_frames: int):
        self.table = []
        self.list_process = np.array(list_process)
        self.n_frames = n_frames
        self.falls = 0
        self.fallos = []

    def calculate(self):
        self.falls = 0
        self.fallos = []
        self.table = [[] for _ in range(self.n_frames)]
        memory = np.full(self.n_frames, None)
        list_process = self.list_process.copy()

        for idx, process in enumerate(self.list_process):
            fallo = False
            if process in memory:
                pass
            elif None in memory:
                j = np.where(memory == None)[0][0]
                memory[j] = int(process)
                self.falls += 1
                fallo = True
            else:
                future = []
                for mem in memory:
                    if mem in list_process[idx + 1:]:
                        future.append(list_process[idx + 1:].tolist().index(mem))
                    else:
                        future.append(float('inf'))
                j = np.argmax(future)
                memory[j] = int(process)
                self.falls += 1
                fallo = True

            for i in range(self.n_frames):
                self.table[i].append("" if memory[i] is None else memory[i])
            self.fallos.append("*" if fallo else "")

