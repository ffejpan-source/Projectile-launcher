import math
import matplotlib.pyplot as plt #give nickname plt

def simulate_trajectory(angle_deg, velocity, start_height):
    angle_rad = math.radians(angle_deg) #convert to radians for sin and cos functions
    vx = velocity*math.cos(angle_rad) #velocity in the horizontal direction
    vy = velocity*math.sin(angle_rad) #velocity in the vertical direction
    g = 9.81 #gravity
    dt = 0.01  #seconds per step
    t = 0      #current time, starting at 0
    x_values = []
    y_values = []
    
    while True:
        x = vx*t
        y = start_height + vy*t - 0.5*g*t**2
    
        if y < 0:
            break                   #projectile has hit the ground
        x_values.append(x)          #add position to list
        y_values.append(y)          #add position to list
        t+=dt                       #move time forward 1 step
    return x_values, y_values

def get_valid_number(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")
            continue

        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}, try again.")
            continue
        if max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}, try again.")
            continue

        return value

num_launches = int(input("How many launches do you want to compare? "))

for i in range(num_launches):
    angle_deg = get_valid_number(f"Launch {i+1} — angle (degrees): ", min_value=0, max_value=90) #fstring for inputting variable 
    start_height = get_valid_number(f"Launch {i+1} — starting height (m): ", min_value=0)
    velocity = get_valid_number(f"Launch {i+1} — velocity (m/s): ", min_value=0.01)
    x_values, y_values = simulate_trajectory(angle_deg, velocity, start_height)
    plt.plot(x_values, y_values, label=f"{angle_deg}°, {velocity} m/s")


plt.xlabel("Horizontal distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion")
plt.legend()
plt.show()
