import math
import matplotlib.pyplot as plt #give nickname plt
def simulate_trajectory(angle_deg, velocity):
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
        y = vy*t - 0.5*g*t**2
    
        if y < 0:
            break                   #projectile has hit the ground
        x_values.append(x)          #add position to list
        y_values.append(y)          #add position to list
        t+=dt                       #move time forward 1 step
    return x_values, y_values

num_launches = int(input("How many launches do you want to compare? "))
for i in range(num_launches):
    angle_deg = float(input(f"Launch {i+1} — angle (degrees): ")) #fstring for inputting variable
    velocity = float(input(f"Launch {i+1} — velocity (m/s): "))
    x_values, y_values = simulate_trajectory(angle_deg, velocity)
    plt.plot(x_values, y_values, label=f"{angle_deg}°, {velocity} m/s")
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion")
plt.legend()
plt.show()