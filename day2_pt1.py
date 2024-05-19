movement_string ="""forward 5
down 5
forward 8
up 3
down 8
forward 2"""




def analyze_movement_history(movement_string):
    horizontal_position = 0
    vertical_position = 0

    movement_list = movement_string.splitlines()

    for line in movement_list:
        if "forward" in line:
            vertical_position += int(line.replace("forward ", ""))
        elif "up" in line:
            horizontal_position -= int(line.replace("up ", ""))
        elif "down" in line:
            horizontal_position += int(line.replace("down ", ""))

    return vertical_position * horizontal_position


print(analyze_movement_history(movement_string))




