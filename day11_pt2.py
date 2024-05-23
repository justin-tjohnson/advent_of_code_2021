raw_data = """1224346384
5621128587
6388426546
1556247756
1451811573
1832388122
2748545647
2582877432
3185643871
2224876627"""


class DumboOctopus:
    def __init__(self, raw_data):
        self.formatted_data = self.format_data(raw_data)
        self.row_indexes = range(len(self.formatted_data))
        self.col_indexes = range(len(self.formatted_data[0]))

    def format_data(self, raw_data):
        formatted_data = []

        for line in raw_data.splitlines():
            row = [int(number) for number in line]
            formatted_data.append(row)
        
        return formatted_data
    
    def increase_energy_level(self):

        for row_id in range(len(self.formatted_data)):
            for col_id in range(len(self.formatted_data[0])):
                self.formatted_data[row_id][col_id] += 1

    def find_surrounding_positions(self, row_id, col_id):
        # inputs are the coordinates of the octopus that flashed
        # surrounding coordinates
        surr_octopus_positions= (
            (row_id-1, col_id),
            (row_id+1, col_id),
            (row_id, col_id+1),
            (row_id, col_id-1),
            (row_id-1, col_id-1),
            (row_id+1, col_id-1),
            (row_id-1, col_id+1),
            (row_id+1, col_id+1),
        )

        # surrounding coordinate needs to be within grid
        valid_surr_octopus_position = tuple(
            (pos[0], pos[1]) for pos in surr_octopus_positions 
            if pos[0] in self.row_indexes and pos[1] in self.col_indexes
        )

        return valid_surr_octopus_position

    def update_surrounding_octopus(self, row_id, col_id):
        positions = self.find_surrounding_positions(row_id, col_id)

        for position in positions:
            if self.formatted_data[position[0]][position[1]] != 0:
                self.formatted_data[position[0]][position[1]] += 1

    def search_for_flash(self):
        while True:
            new_flashes_exist = False
            for row_id in range(len(self.formatted_data)):
                for col_id in range(len(self.formatted_data[0])):
                    # energy greater than 9 triggers flash
                    if self.formatted_data[row_id][col_id] > 9:
                        new_flashes_exist = True
                        self.formatted_data[row_id][col_id] = 0
                        self.update_surrounding_octopus(row_id, col_id)

            if not new_flashes_exist:
                break

    def check_for_simulatenous_flash(self):
        all_energies = []
        for row_id in range(len(self.formatted_data)):
            for col_id in range(len(self.formatted_data[0])):
                all_energies.append(self.formatted_data[row_id][col_id])

        if all(energy==0 for energy in all_energies):
            return True

        return False
        
    def find_simultaneous_flash_step(self):
        
        step = 1

        while True:
            # for step in range(1, self.steps+1):

            self.increase_energy_level()
            self.search_for_flash()

            if self.check_for_simulatenous_flash():
                break

            step += 1
        
        return step

octopus_flash = DumboOctopus(raw_data)

print(octopus_flash.find_simultaneous_flash_step())

