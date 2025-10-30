maintenance_cost = [15000,15500,16000,17000,17500,16500,18000,18500,19000,19500,20000,21000]

plt.scatter(maintenance_cost, accidents, color='red')
plt.title("Road Maintenance Cost vs Accidents")
plt.xlabel("Road Maintenance Cost (₹)")
plt.ylabel("Number of Accidents")
plt.show()
