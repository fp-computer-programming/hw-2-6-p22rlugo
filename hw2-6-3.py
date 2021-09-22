# Ryan Lugo: RJL 9/21/21

free_throw_input = input("How many times did they score free throws?: ")
inside_input = input("How many times did they score inside?: ")
outside_input = input("How many times did they score outside?: ")

free_throw_times_scored = int(free_throw_input)
inside_times_scored = int(inside_input)
outside_times_scored = int(outside_input)

##Hard Coded values
free_throw = 1 * free_throw_times_scored
inside_three_point = 2 * inside_times_scored
outside_three_point = 3 * outside_times_scored

#All points added together for easier printing
final_points = free_throw + outside_three_point + inside_three_point

print("The Player scored",final_points,"points in the game!")