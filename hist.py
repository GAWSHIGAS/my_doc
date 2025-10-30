accidents = [45,42,50,48,52,55,60,58,62,65,63,68]

plt.hist(accidents, bins=5, color='lightgreen', edgecolor='black')
plt.title("Distribution of Monthly Accidents")
plt.xlabel("Number of Accidents")
plt.ylabel("Frequency")
plt.show()
