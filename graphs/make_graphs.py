import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pylab


# Some help for coloring
slices = [1,2,3] * 4 + [20, 25, 30] * 2
cmap = plt.cm.prism
colors = cmap(np.linspace(0., 1., len(slices)))

# Overall Course Rating
x_list_overall = [9, 2]
label_list_overall = ["Excellent", "Very Good", "Good", "Fair", "Poor"]
plt.axis("equal")
plt.pie(
        x_list_overall,
        autopct="%1.1f%%",
        colors=colors
        )

plt.legend(label_list_overall, loc='center left', bbox_to_anchor=(0.9, 0.5))
plt.savefig("graphs/overall.png", bbox_inches='tight')
plt.close()
###########


# University Part
x_list_university = [3, 4, 2, 1]
label_list_university = ["Department of Economics", "Harris School of Public Policy", "Booth School of Business", "Other"]
plt.axis("equal")
plt.pie(
        x_list_university,
        autopct="%1.1f%%",
        colors=colors
        )
plt.legend(label_list_university, loc='center left', bbox_to_anchor=(0.9, 0.5))
plt.savefig("graphs/part_univ.png", bbox_inches='tight')
plt.close()
###########



# Usefulness
x_list_rating_overall = [1, 2, 7]
label_list_rating_overall = ["3", "4", "Very useful: 5"]
plt.axis("equal")
plt.pie(
        x_list_rating_overall,
        autopct="%1.1f%%",
        colors=colors
        )

plt.legend(label_list_rating_overall, loc='center left', bbox_to_anchor=(0.9, 0.5))
plt.savefig("graphs/useful.png", bbox_inches='tight')
plt.close()
###########

# Well organized?
x_list_organized = [9,1]
label_list_organized = ["Excellent", "Very Good", "Good", "Fair", "Poor"]
plt.axis("equal")
plt.pie(
        x_list_organized,
        autopct="%1.1f%%",
        colors=colors
        )

plt.legend(label_list_organized, loc='center left', bbox_to_anchor=(0.9, 0.5))
plt.savefig("graphs/organized.png", bbox_inches='tight')
plt.close()
###########

# Right Speed
x_list_speed = [8,2]
label_list_speed = ["Excellent", "Very Good", "Good", "Fair", "Poor"]
plt.axis("equal")
plt.pie(
        x_list_speed,
        autopct="%1.1f%%",
        colors=colors
        )

plt.legend(label_list_speed, loc='center left', bbox_to_anchor=(0.9, 0.5))
plt.savefig("graphs/speed.png", bbox_inches='tight')
plt.close()
###########

# clearly
x_list_clearly = [10]
label_list_clearly = ["Excellent", "Very Good", "Good", "Fair", "Poor"]
plt.axis("equal")
plt.pie(
        x_list_clearly,
        autopct="%1.1f%%",
        colors=colors
        )

plt.legend(label_list_clearly, loc='center left', bbox_to_anchor=(0.9, 0.5))
plt.savefig("graphs/clearly.png", bbox_inches='tight')
plt.close()
###########

# accessible
x_list_access = [9,1]
label_list_access = ["Excellent", "Very Good"]
plt.axis("equal")
plt.pie(
        x_list_access,
        autopct="%1.1f%%",
        colors=colors
        )

plt.legend(label_list_access, loc='center left', bbox_to_anchor=(0.9, 0.5))
plt.savefig("graphs/access.png", bbox_inches='tight')
plt.close()
###########