simulated_list = [3,4,3,1,2]
days = 18


# taking a different approach since iterating over the list is too every day
# is too computationally expensive

class LanternFishSimulation:

    def __init__(self, simulated_list, days):
        self.simulated_list = simulated_list
        self.days = days

    def zero_time_fish_growth(self):

        fish_map = {}
        # only look at one fish with each unique timer in input to reduce memory usage
        current_fish_days = [0]
        new_fish = 0

        if 0 in current_fish_days:
            new_fish = current_fish_days.count(0)

        # each iteration is calculating the final state after the day specified

        for day in range(1, self.days+1):
            last_8_days = list(range(self.days-8, self.days+1))
            fish_age_range = list(range(0,9))
            fish_age_range.reverse()

            current_fish_days = [6 if timer == 0 else timer-1 for timer in current_fish_days]
            # current_fish_days.extend([8]*new_fish)

            if 0 in current_fish_days:
                new_fish = current_fish_days.count(0)
            else:
                new_fish = 0

            if day in last_8_days:
                index = last_8_days.index(day)
                fish_map[fish_age_range[index]] = len(current_fish_days)
        
        return fish_map
    
    def find_growth_from_one_fish(self, timer):

        fish_map = {}
        # only look at one fish with each unique timer in input to reduce memory usage
        current_fish_days = [timer]
        new_fish = 0

        if 0 in current_fish_days:
            new_fish = current_fish_days.count(0)

        # each iteration is calculating the final state after the day specified
        for day in range(self.days):

            current_fish_days = [6 if timer == 0 else timer-1 for timer in current_fish_days]
            current_fish_days.extend([8]*new_fish)

            if 0 in current_fish_days:
                new_fish = current_fish_days.count(0)
            else:
                new_fish = 0
        
        #     fish_map[day] = len(current_fish_days)
        # print(fish_map)
        return len(current_fish_days)

        #     if day in fish_map_days:
        #         fish_timer = fish_map_days.index(day)+1
        #         fish_map[fish_timer] = len(current_fish_days)
        #         print(fish_map)

        # return fish_map
        # print(current_fish_days)
        # return len(current_fish_days)
        
    def find_number_of_fish(self):
        fish_map = {}
        # unique_timers = set(self.simulated_list)

        fish_map = self.zero_time_fish_growth()
        print(fish_map)

        # for unique_timer in unique_timers:
        #     fish_map[unique_timer] = self.find_growth_from_one_fish(unique_timer)

        total_fish = 0
        for fish_timer in self.simulated_list:
            total_fish += fish_map[fish_timer]
        
        return total_fish

lantern_fish = LanternFishSimulation(simulated_list, days)

print(lantern_fish.find_number_of_fish())