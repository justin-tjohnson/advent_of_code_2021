simulated_list = [3,4,3,1,2]
days = 18

# taking a different approach since iterating over the list every after day
# is too computationally expensive

class LanternFishSimulation:

    def __init__(self, simulated_list, days):
        self.simulated_list = simulated_list
        self.days = days

    def fresh_fish_map(self):
        # initialize fish map.  dict with keys equal to fish age and values
        # equal to quanity that have each respective timer
        fish_map = {}
        for timer in range(0,9):
            fish_map[timer] = 0
        
        return fish_map

    def update_fish_map(self, fish_map):
        new_fish = 0
        current_fish_map = fish_map.copy()

        fish_map = self.fresh_fish_map()
        for timer in current_fish_map.keys():
            
            if timer == 0:
                # fish return back to 6 day life after 0 
                fish_map[6] = current_fish_map[0]
                new_fish += current_fish_map[0]

            else:
                # subtract day from each fish timer
                fish_map[timer-1] += current_fish_map[timer]

        # add new fish to 8 day timer
        fish_map[8] = new_fish

        return fish_map, new_fish


    def find_fish_growth(self):

        fish_map = self.fresh_fish_map()

        # add curent list of fish timers to fish map
        for fish_timer in self.simulated_list:
            fish_map[fish_timer] += 1
        

        # each iteration is calculating the final state after the day specified
        for _ in range(self.days):
            fish_map, _ = self.update_fish_map(fish_map)
    
        return sum(fish_map.values())


lantern_fish = LanternFishSimulation(simulated_list, days)

print(lantern_fish.find_fish_growth())