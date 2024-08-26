input = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""

REQUIRED_OVERLAPPING_COORDINATES = 12

import copy
import math
from itertools import combinations

def scan_inputs(input):

    scanner_beacon_dict = {}

    for line in input.splitlines():
        if "scanner" in line:
            scanner_id = line.replace('--- scanner ', '').replace(' ---', '')
            scanner_beacon_dict[scanner_id] = []

        elif line == '':
            continue

        else:
            coordinates = line.split(",")
            coordinates = [int(coordinate) for coordinate in coordinates]
            scanner_beacon_dict[scanner_id].append(coordinates)

    return scanner_beacon_dict


def shift_beacon_coordinates(beacon_coordinates, shifts):
    x_shift, y_shift, z_shift = shifts

    new_coordinates = []

    for coordinate in beacon_coordinates:
        new_coordinate = [
            coordinate[0] + x_shift,
            coordinate[1] + y_shift,
            coordinate[2] + z_shift
        ]

        new_coordinates.append(new_coordinate)

    return new_coordinates





def transform_coordinate(point, theta, rotation_axis):
    x,y,z = point
    cos = {
        0: 1,
        90: 0,
        180: -1,
        270: 0
    }
    sin = {
        0:0,
        90:1,
        180:0,
        270:-1
    }


    # cos_theta = math.cos(math.radians(theta))
    # sin_theta = math.sin(math.radians(theta))

    if rotation_axis == "x":
        x_new = copy.deepcopy(x)
        y_new = y*cos[theta] - z*sin[theta]
        z_new = y*sin[theta] + z*cos[theta]

    elif rotation_axis == "y":
        x_new = x*cos[theta] + z*sin[theta]
        y_new = copy.deepcopy(y)
        z_new = z*cos[theta] - x*sin[theta]

    elif rotation_axis == "z":
        x_new = x*cos[theta]- y*sin[theta]
        y_new = x*sin[theta] + y*cos[theta]
        z_new = copy.deepcopy(z)


    return (round(x_new), round(y_new), round(z_new))

def transform_beacon_coordinates(coordinates, theta, rotation_axis):

    new_coordinates = []

    for coordinate in coordinates:

        new_coordinate = transform_coordinate(coordinate, theta, rotation_axis)
        new_coordinates.append(new_coordinate)

    return new_coordinates

def check_overlapping_coordinates(coordinate_list1, coordinate_list2):

    coordinate_list1_hashed = [f"{point[0]},{point[1]},{point[2]}" for point in coordinate_list1]
    coordinate_list2_hashed = [f"{point[0]},{point[1]},{point[2]}" for point in coordinate_list2]

    coordinate_set1 = set(coordinate_list1_hashed)
    coordinate_set2 = set(coordinate_list2_hashed)

    #create set of only overlapping coordinates
    overlapping_coordinates_set = coordinate_set1.intersection(coordinate_set2)

    if len(overlapping_coordinates_set) < REQUIRED_OVERLAPPING_COORDINATES:
        return []

    overlapping_coordinates = []
    for overlapping_coordinate in overlapping_coordinates_set:
        overlapping_coordinate = overlapping_coordinate.split(',')
        overlapping_coordinate = [int(coordinate) for coordinate in overlapping_coordinate]
        overlapping_coordinates.append(overlapping_coordinate)

    return overlapping_coordinates


def look_for_beacon_match(known_scanner_coordinates, analyzed_scanner_coordinates):

    x_shifts_to_check = []
    y_shifts_to_check = []
    z_shifts_to_check = []

    shifts_to_check = []

    for known_beacon_point in known_scanner_coordinates:
        for analyzed_beacon_point in analyzed_scanner_coordinates:
            shifts_to_check.append(
                (
                    known_beacon_point[0] - analyzed_beacon_point[0],
                    known_beacon_point[1] - analyzed_beacon_point[1],
                    known_beacon_point[2] - analyzed_beacon_point[2]
                )
            )
            x_shifts_to_check.append(known_beacon_point[0] - analyzed_beacon_point[0])
            y_shifts_to_check.append(known_beacon_point[1] - analyzed_beacon_point[1])
            z_shifts_to_check.append(known_beacon_point[2] - analyzed_beacon_point[2])



    for shift in shifts_to_check:

        new_scanner_coordinates = shift_beacon_coordinates(analyzed_scanner_coordinates, shift)

        overlapping_coordinates = check_overlapping_coordinates(known_scanner_coordinates, new_scanner_coordinates)
        
        if overlapping_coordinates:
            return shift, overlapping_coordinates

    return (), []


def iterate_through_all_orientations_to_find_overalps(known_scanner_coordinates, analyzed_scanner_coordinates):

    # iterate through all 24 orientations of analyzed_scanner until 12 overlapping beacons are found
    global_rotations = (
        ("z", 0, "z", "pos"),
        ("y", 90, "x", "pos"),
        ("y", 180, "z", "neg"),
        ("y", 270, "x", "neg"),
        ("x", 90, "y", "neg"),
        ("x", 270, "y", "pos"),
    )

    for global_rotation in global_rotations:
        global_rot_axis, theta, normal_axis, _ = global_rotation

        transformed_coordinates = transform_beacon_coordinates(analyzed_scanner_coordinates, theta, global_rot_axis)

        for local_rotation in (0, 90, 180, 270):

            transformed_coordinates = transform_beacon_coordinates(transformed_coordinates, local_rotation, normal_axis)

            csys_shift, overlapping_coordinates = look_for_beacon_match(known_scanner_coordinates, transformed_coordinates)

            if not overlapping_coordinates:
                # print(f"no overlap found for global_rot_axis: {global_rot_axis}, theta: {theta}, normal_axis: {normal_axis}, local_rotation{local_rotation}")
                continue

            return csys_shift, overlapping_coordinates, transformed_coordinates

    return (), [], []


def locate_all_overlapping_coordinates(input):
    
    scanner_beacon_dict = scan_inputs(input)

    scanner_ids = list(scanner_beacon_dict.keys())

    resolved_scanners = ['0']
    all_overlapping_coordinates = []

    discovered_scanner_dict = {'0': scanner_beacon_dict['0']}
    
    # first time overlapping cubes relative to scanner 0 since scanner 0 is the reference frame for other to be based off of
    for scanner_id in scanner_ids:

        # don't compare scanner 0 to itself
        if scanner_id == '0':
            continue
        
        _, overlapping_coordinates, transformed_coordinates = iterate_through_all_orientations_to_find_overalps(scanner_beacon_dict['0'], scanner_beacon_dict[scanner_id])

        if overlapping_coordinates:
            # print(f'0, {scanner_id}')
            all_overlapping_coordinates.extend(overlapping_coordinates)
            resolved_scanners.append(scanner_id)
            discovered_scanner_dict[scanner_id] = transformed_coordinates

    # now search for all other combos of scanners until all are located and found relative to scanner 0
    counter = 0

    # print(discovered_scanner_dict)
    
    known_scanner_ids = list(discovered_scanner_dict.keys())
    unknown_scanner_ids = [scanner_id for scanner_id in scanner_beacon_dict.keys() if scanner_id not in known_scanner_ids]


    while True:

        new_discovered_scanners = []
        # print(f"unknown_scanner_ids{unknown_scanner_ids}")
        # print(f"known_scanner_id{known_scanner_ids}")
        for unknown_scanner_id in unknown_scanner_ids:

            for known_scanner_id in known_scanner_ids:
                
                #already compared to scanner 0 above
                if known_scanner_id == '0':
                    continue
                
                # print(f"known_scanner_id{known_scanner_id}, unknown_scanner_id{unknown_scanner_id}")
                _, overlapping_coordinates, transformed_coordinates = iterate_through_all_orientations_to_find_overalps(discovered_scanner_dict[known_scanner_id], scanner_beacon_dict[unknown_scanner_id])

                if overlapping_coordinates:
                    # print(f'{known_scanner_id}, {unknown_scanner_id}')
                    all_overlapping_coordinates.extend(overlapping_coordinates)
                    new_discovered_scanners.append(unknown_scanner_id)
                    discovered_scanner_dict[unknown_scanner_id] = transformed_coordinates

        # print(f"new_discovered_scanners {new_discovered_scanners}")
        for new_discovered_scanner in new_discovered_scanners:

            if new_discovered_scanner in unknown_scanner_ids:
                unknown_scanner_ids.remove(new_discovered_scanner)

            if new_discovered_scanner not in known_scanner_ids:
                known_scanner_ids.append(new_discovered_scanner)

        # all scanners located, exit loop
        if len(discovered_scanner_dict.keys()) == len(scanner_beacon_dict.keys()):
            break

        counter += 1

        # in case my code is borked
        if counter > 100:
            break

        # print(new_discovered_scanners)
    
    return all_overlapping_coordinates
        

all_overlapping_coordinates = locate_all_overlapping_coordinates(input)
print(all_overlapping_coordinates)
print(len(all_overlapping_coordinates))





# scanner_beacon_dict = scan_inputs(input)

# csys_shift, overlapping_coordinates, transformed = iterate_through_all_orientations_to_find_overalps( scanner_beacon_dict['0'], scanner_beacon_dict['1'])
# print(len(overlapping_coordinates))


# csys_shift1, overlapping_coordinates1, transformed1 = iterate_through_all_orientations_to_find_overalps( transformed, scanner_beacon_dict['4'])
# print(len(overlapping_coordinates1))



# print(csys_shift)
# print(overlapping_coordinates)
# print(len(overlapping_coordinates))