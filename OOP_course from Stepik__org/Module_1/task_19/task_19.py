class CPU():
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory():
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard():
    def __init__(self, name, cpu, *mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = total_mem_slots

    def get_config(self):
        res = [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}']


        memory = ['Память:']
        counter = self.total_mem_slots
        for mem in self.mem_slots:
            if not counter:
                break
            memory.append(f'{mem.name} - {mem.volume};')
            counter -= 1

        res.append(' '.join(memory)[:-1])
        return res

mb = MotherBoard('Asus', CPU('asus', 1333), Memory('Kingstone', 4000), Memory('Kingstone', 4000))