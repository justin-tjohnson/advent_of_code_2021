simulated_list = [3,4,3,1,2]
days = 18


class LanternFishSimulation:

    def __init__(self, simulated_list, days):
        self.simulated_list = simulated_list
        self.days = days
    
    def find_number_of_fish(self):
        current_fish_days = self.simulated_list
        new_fish = 0

        if 0 in current_fish_days:
            new_fish = current_fish_days.count(0)

        # each iteration is calculating the final state after the day specified
        for _ in range(self.days):


            current_fish_days = [6 if timer == 0 else timer-1 for timer in current_fish_days]
            current_fish_days.extend([8]*new_fish)

            if 0 in current_fish_days:
                new_fish = current_fish_days.count(0)
            else:
                new_fish = 0
        
        return len(current_fish_days)
    

lantern_fish = LanternFishSimulation(simulated_list, days)

print(lantern_fish.find_number_of_fish())
