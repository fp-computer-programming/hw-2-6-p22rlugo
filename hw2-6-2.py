# Ryan Lugo: RJL 9/21/21

radius_prompt = input("What's the radius of the cylinder?: ")
height_prompt = input("What's the height of the cylinder?: ")

height = int(height_prompt)
raidus = int(radius_prompt)

surface_area = 2 * 3.14 * raidus * height + 2 * 3.14 * (raidus ** 2)
volume = 3.14 * (raidus **2) * height

print("Surface Area:",surface_area,"Volume:",volume)