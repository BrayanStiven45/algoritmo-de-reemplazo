import numpy as np

# class Fifo:

#     def __init__(self, list_process, n_frames: int):

#         self.table = np.empty((n_frames, len(list_process)))
#         self.list_process = np.array(list_process)
#         self.n_frames = n_frames

#     def calculate(self):

#         self.falls = 0
#         visited = []
#         memory = np.full(self.n_frames, None)

#         for process in self.list_process:

#             if process in memory:
#                 print(f'process: {process}, memory: {memory}')
#                 continue
            
#             if np.any(memory == None):
#                 j = np.where(memory == None)[0][0]
#                 memory[j] = int(process)
#                 self.falls += 1
#                 visited.append(process)
#             else:
#                 j = np.where(memory == visited[0])[0][0]
#                 memory[j] = int(process)
#                 visited.pop(0)
#                 visited.append(process)
#                 self.falls += 1
            
#             print(f'process: {process}, memory: {memory}')
            

# fifo = Fifo([6, 1, 7, 1, 2, 1, 5, 6, 0, 1, 7, 1, 1, 6, 0, 7, 0, 1, 2, 6, 1], 4)
# fifo.calculate()
# print(f'fallos: {fifo.falls}')

class Fifo:
    def __init__(self, list_process, n_frames: int):
        self.list_process = np.array(list_process)
        self.n_frames = n_frames
        self.table = [[] for _ in range(n_frames)]
        self.fallos = []
        self.falls = 0

    def calculate(self):
        memory = np.full(self.n_frames, None)
        visited = []
        self.falls = 0
        self.fallos = []
        self.table = [[] for _ in range(self.n_frames)]

        for process in self.list_process:
            fallo = False

            if process in memory:
                pass  # hit, no fallo
            elif None in memory:
                j = np.where(memory == None)[0][0]
                memory[j] = process
                visited.append(process)
                fallo = True
                self.falls += 1
            else:
                j = np.where(memory == visited[0])[0][0]
                memory[j] = process
                visited.pop(0)
                visited.append(process)
                fallo = True
                self.falls += 1

            for i in range(self.n_frames):
                self.table[i].append("" if memory[i] is None else memory[i])
            self.fallos.append("*" if fallo else "")
