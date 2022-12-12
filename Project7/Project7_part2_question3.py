# Plot the data as a line graph
plt.plot(times, u_values_old, "-", label="Old Utilization")
plt.plot(times, u_values_old, "--", label="New Utilization, k = 5")
# Add labels and title
plt.legend(loc="upper left")
plt.xlabel("Time (t)")
plt.ylabel("Utilization (p)")
plt.title("a) Utilization (p) over Time (t)")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(lam_values_old, lam_values_old, "-", label="Old Throughput")
plt.plot(lam_values_old, lam_values_new, "--", label="New Throughput, k = 5")
# Add labels and title
plt.legend(loc="upper left")
plt.xlabel("Time (t)")
plt.ylabel("Throughput (x)")
plt.title("b) Throughput (x) over Time (t)")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(times, mean_values, "-", label="Old mean number in system")
plt.plot(times, mean_values, "--", label="New mean number in system, k = 5")
# Add labels and title
plt.legend(loc="upper left")
plt.xlabel("Time (t)")
plt.ylabel("Mean number in system E[N]")
plt.title("c) Mean number in system E[N] over Time (t)")

# Show the plot
plt.show()

# Plot the data as a line graph
plt.plot(times, mean_times, "-", label="Old mean time in system")
plt.plot(times, new_mean_times, "--", label="New mean time in system, k = 5")
# Add labels and title
plt.legend(loc="upper left")
plt.xlabel("Time (t)")
plt.ylabel("Mean time in system E[T]")
plt.title("d) Mean time in system E[T] over Time (t)")

# Show the plot
plt.show()
