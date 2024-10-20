from matplotlib import pyplot as plt
plt.ion()
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5976.6, 10289.7, 14958.3]
#create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color = "green", marker = 'o', linestyle = 'solid')
#Add a title
plt.title("Norminal gdp")
#add a label to the y-axis
plt.ylabel("Billion of $")
plt.show()

movies = ["Avengers", "Spider Man", "Iron Man", "Thor"]
num_oscars = [5, 1, 6, 13]
#plot bars with movies indexes and number of oscars achieved
plt.bar(range(len(movies)), num_oscars)
plt.title("My favorite movie")
plt.ylabel("# of academy awards")
plt.xticks(range(len(movies)), movies)
plt.show()

from collections import Counter
grades = [83, 90, 95, 0 , 71, 72, 68, 70, 89, 95, 50]
histogram = Counter(min(grade // 10*10, 90) for grade in grades)
plt.bar([x+5 for x in histogram.keys()], histogram.values(), 10, edgecolor = (0, 0, 0))
plt.axis([-5, 105, 0, 5]) #x axis from -5 to 105, y-axis from 0 to 5
plt.xticks([10*i for i in range(11)]) #x-axis label at 0, 10, ... 100
plt.xlabel("Decile")
plt.ylabel("number of student")
plt.title("Distribution of Exam 1 grades")
plt.show()


variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
#We can make multiple calls to plt.plot 
#to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label = 'variance') #green solid line
plt.plot(xs, bias_squared, 'r-.', label = 'bias^2') #red dashed line
plt.plot(xs, total_error, 'b:', label = 'total_error') #blue dotted line
plt.legend(loc = 9) # loc = 9 means top-center
plt.xlabel('model complexity')
plt.xticks([])
plt.title("The bias-variance trade-off")
plt.show()

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120,220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
plt.scatter(friends, minutes)
for friend, minute, label in zip(friends, minutes, labels):
    plt.annotate(label, xy = (friend, minute), xytext = (5, -5), textcoords= 'offset points')
plt.title("Daily minutes vs Number of friends")
plt.xlabel('# of friends')
plt.ylabel('Time spent')
plt.show()