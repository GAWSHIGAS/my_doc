fuel_price = [97,98,99,100,101,102,104,105,106,107,108,109]

plt.plot(fuel_price, vehicles, marker='o', linestyle='-', color='orange')
plt.title("Fuel Price vs Vehicle Traffic")
plt.xlabel("Fuel Price (₹/L)")
plt.ylabel("Vehicles Passed")
plt.show()
