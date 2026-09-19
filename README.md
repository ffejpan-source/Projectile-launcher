# Projectile Motion Simulator

A Python simulator that calculates and visualizes projectile trajectories
using basic kinematics — enter a launch angle and velocity, and it plots
the resulting arc. Supports comparing multiple launches on the same graph.

## What it does

- Takes launch angle (degrees) and initial velocity (m/s) as input
- Calculates the trajectory using standard projectile motion equations
  (horizontal/vertical velocity components, gravity, time-stepped position)
- Plots the path with `matplotlib`
- Lets you compare multiple launches on one graph, each labeled in a legend

## The physics

- Velocity is split into horizontal and vertical components:
  `vx = v·cos(θ)`, `vy = v·sin(θ)`
- Horizontal position: `x = vx · t` (constant velocity, no air resistance)
- Vertical position: `y = vy · t − 0.5 · g · t²` (gravity pulls it back down)
- The simulation steps forward in small time increments (`dt = 0.01s`)
  until the projectile returns to ground level (`y < 0`)

## Setup

1. Install the one dependency:
   ```
   pip install matplotlib
   ```

2. Run it:
   ```
   py projectile.py
   ```

3. Enter how many launches you want to compare, then enter an angle and
   velocity for each one. A graph opens showing all trajectories overlaid,
   with a legend identifying each by its angle/velocity.

## Notes

Built to apply concepts from my linear algebra / physics coursework and
to practice AI-assisted development (Claude Code in Action certification) —
Claude was used to explain concepts and review code, with the implementation
written by hand.

## Possible next steps

- Plot real experimental/lab data points alongside the simulated curve for
  comparison
- Display max height, range, and time of flight as text output
- Handle invalid input (negative velocity, angle outside 0-90°) gracefully
