# Write a program to calculate the resources needed 
# to remodel a golf course hole.  
#     See assignment description for details.
# 
# The inputs should be:
#     Enter Course Length: 
#     Enter Course Width: 
# 
# The outputs should be:
#     Total square yards of rough sod:
#     Total square yards of smooth sod:
#     Tons of sand:
#     Number of retaining wall bricks:
#     Number of bushes:
#     Total Mowing Time (mins):
import math

def calc_course_area (course_length, course_width) :
    course_area = round(course_width * course_length)

    return course_area

def calc_course_perim (course_length, course_width) :
    course_perim = (2 * course_length) + (2 * course_width)

    return course_perim

def calc_circle_area (diameter) :
    circle_area = round(pi * ((diameter / 2) ** 2), 2)

    return circle_area

def calc_sand_volume (diameter) :
    sand_volume = pi * (((diameter / 2) * 3) ** 2) * 1

    return sand_volume

def calc_brick_wall (diameter) :
    wall_length = (pi * (diameter * 36)) / 2
    num_bricks = math.ceil((wall_length / 12) * 3)
    return num_bricks
    
pi = 3.1415

def calc_golf_remodel () :
    course_length = float(input("Enter Course Length:"))
    course_width = float(input("Enter Course Width:"))
    

    course_area = calc_course_area(course_length, course_width)
                         
    smooth_sod_diameter = course_width / 2
    sand_trap_diameter = course_width / 3
    
    smooth_sod_area = calc_circle_area(smooth_sod_diameter)
    smooth_sod_tot = round(smooth_sod_area * 2, 2)
    
                         
    sand_trap_area = calc_circle_area(sand_trap_diameter)
    sand_volume = calc_sand_volume(sand_trap_diameter)
    tons_sand = round((sand_volume * 100) / 2000, 2)
    tot_bricks = calc_brick_wall(sand_trap_diameter)
                         
    rough_sod_tot = round(course_area - sand_trap_area - smooth_sod_tot )                     
    tot_bushes = round(calc_course_perim(course_length, course_width) - 2)
    tot_mow_time = round(((rough_sod_tot * .5) + smooth_sod_tot) / 60)
    
                         
                         
    print("Total square yards of rough sod: ", rough_sod_tot)
    print("Total square yards of smooth sod: ", smooth_sod_tot)
    print("Tons of sand: ", tons_sand)
    print("Number of retaining wall bricks: ", tot_bricks)
    print("Numbe of bushes: ", tot_bushes)
    print("Total Mowing Time (mins):", tot_mow_time)
    
calc_golf_remodel()        