import random
npart=500
side=41  #Should be an odd number
time=0
steps = [(1,0),(-1,0),(0,1),(0,-1)]
maxsteps = 10000      #maximum number of steps the particle can move.
perc = 0
x,y = 0,0
grid=[[0 for x in range(side)] for y in range(side)]

density = float(input("enter a density value between 0.0 and 1.0 that specifies the fraction of cells: "))

#loop over all cells in the grid and set each cell to "1"
while x < len(grid):
    while y < len(grid[x]):
        grid[x][y] = random.choices([0,1],[1.0 - density, density], k=1)[0]
        y += 1
    x+=1
    y=0

for ipart in range(npart):
    # Start particle at center
    x,y = side//2,side//2
    # perform the random walk until particle departs,convert while "1" loop to a for loop over maxsteps
    for istep in range (maxsteps):
        # Randomly move particle
        sx,sy = random.choice(steps)
        #use an if statement to see if the new cell already has a value equal to 1, if it is do not move, use the continue command to go to the next iteration
        if grid[x+sx][y+sy]==1:
          continue
        else:
            x += sx
            y += sy
        #If the particle reaches the edge of the system,then increment perc by one and go to the next particle
        if x<0 or y<0 or x==side-1 or y==side-1:
            perc +=1
            break

print("Probility of the particle percolating out of the system is {}".format(perc/npart))

