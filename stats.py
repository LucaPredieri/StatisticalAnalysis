from scipy import stats as st
import matplotlib.pyplot as plt
import numpy as np

# Importing data from the two programs.

with open("collision.txt") as f:
    timestamp_s = f.read().splitlines() 
timestamp = list(map(float, timestamp_s))
print(timestamp)
print(len(timestamp))

with open("trajectory.txt") as f:
    collision_s = f.read().splitlines() 
collision = list(map(int, collision_s))
print(collision)
print(len(collision))

with open("collisionp.txt") as f:
    timestampp_s = f.read().splitlines() 
timestampp = list(map(float, timestampp_s))
print(timestampp)
print(len(timestampp))

with open("trajectoryp.txt") as f:
    collisionp_s = f.read().splitlines() 
collisionp = list(map(int, collisionp_s))
print(collisionp)
print(len(collisionp))

# Calculate the average
collision_mean = np.mean(collision)
timestamp_mean = np.mean(timestamp)
collisionp_mean = np.mean(collisionp)
timestampp_mean = np.mean(timestampp)

# Calculate the standard deviation
collision_std = np.std(collision)
timestamp_std = np.std(timestamp)
collisionp_std = np.std(collisionp)
timestampp_std = np.std(timestampp)

# Define labels, positions, bar heights and error bar heights
labels = ['Mine', 'Professor']
x_pos = np.arange(len(labels))
CTEs = [collision_mean, collisionp_mean]
error = [collision_std, collisionp_std]

# Build the plot
fig, ax = plt.subplots()
ax.bar(x_pos, CTEs,
       yerr=error,
       align='center',
       alpha=0.5,
       ecolor='black',
       capsize=10)
ax.set_ylabel('Number of times the robot changed its direction')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_title('Adjusting the trajectory difference.')
ax.yaxis.grid(True)


# Save the figure and show
plt.tight_layout()
# plt.savefig('bar_plot_with_error_bars.png')
plt.show()


group1 = np.array([14, 15, 15, 16, 13, 8, 14, 17, 16, 14, 19, 20, 21, 15, 15, 16, 16, 13, 14, 12])
group2 = np.array([15, 17, 14, 17, 14, 8, 12, 19, 19, 14, 17, 22, 24, 16, 13, 16, 13, 18, 15, 13])

statistic,p_value = st.ttest_ind(a=group1, b=group2, equal_var=True)
print(x)