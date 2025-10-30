import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
vehicles = [42000,46000,48000,52000,55000,50000,57000,59000,58000,61000,63000,65000]

plt.bar(months, vehicles, color='skyblue')
plt.title("Monthly Vehicle Traffic Comparison")
plt.xlabel("Months")
plt.ylabel("Vehicles Passed")
plt.show()
