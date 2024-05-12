simulated_list = [3,4,3,1,2]
days = 18

# taking a different approach since iterating over the list is too every day
# is too computationally expensive

class LanternFishSimulation:

    def __init__(self, simulated_list, days):
        self.simulated_list = simulated_list
        self.days = days

    def fresh_fish_map(self):
        fish_map = {}
        for timer in range(0,9):
            fish_map[timer] = 0
        
        return fish_map

    def update_fish_map(self, fish_map, new_fish):
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

        fish_map = {}
        for timer in range(0,9):
            fish_map[timer] = 0
        
        fish_map = self.fresh_fish_map()

        # only look at one fish with each unique timer in input to reduce memory usage
        current_fish_days = self.simulated_list
        new_fish = 0

        if 0 in current_fish_days:
            new_fish = current_fish_days.count(0)

        # each iteration is calculating the final state after the day specified
        for _ in range(self.days):

            fish_map, new_fish = self.update_fish_map(fish_map, new_fish)

            # subtract one day from all fish timers
            current_fish_days = [6 if timer == 0 else timer-1 for timer in current_fish_days]

            # count number of zeros in list, this will determine number of fish to be
            # generated
            if 0 in current_fish_days:
                new_fish = current_fish_days.count(0)
            else:
                new_fish = 0
    
        return len(current_fish_days) + sum(fish_map.values())


lantern_fish = LanternFishSimulation(simulated_list, days)

print(lantern_fish.find_fish_growth())