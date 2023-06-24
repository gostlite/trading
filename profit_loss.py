# create a user and balance
import random
import matplotlib.pyplot as plt



def profit_loss():
    return(random.uniform(-2, 2))

# for i in range(11):


# # Number of traders and simulation duration
num_traders = 10
simulation_duration = 60  # minutes

# Initialize lists to store trader data
trader_data = [[] for _ in range(num_traders)]
print(trader_data)

# Simulate profit/loss for each trader over time
for minute in range(simulation_duration):
    for trader in range(num_traders):
        profit_loss = random.uniform(-5, 5)  # Simulating profit/loss between -5 and +5 dollars
        trader_data[trader].append(profit_loss)

print(trader_data)
# Plotting the trader data
plt.figure(figsize=(10, 6))
for trader in range(num_traders):
    plt.plot(range(simulation_duration), trader_data[trader], label=f"Trader {trader + 1}")
plt.xlabel("Time (minutes)")
plt.ylabel("Profit/Loss ($)")
plt.title("Trader Performance")
plt.legend()
plt.grid(True)
plt.show()
