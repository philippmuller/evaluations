import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pylab


# Some help for coloring
slices = [1,2,3] * 4 + [20, 25, 30] * 2
cmap = plt.cm.prism
colors = cmap(np.linspace(0., 1., len(slices)))

# Overall Course Rating
values = np.array([9, 2, 0, 0, 0])
labels = np.array(["Excellent", "Very Good", "Good", "Fair", "Poor"])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.axis("equal")
obj, text, bla = ax.pie(
        values,
        autopct="%1.1f%%",
        colors=colors
        )

# remove the zero elements from visible plot
for elem in bla[2:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/overall.png", bbox_inches='tight')
plt.close()
###########


# University Part
# !!!!!!!!!!!!!!!!!!!!!!!!Check ordering
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
values = np.array([0, 0, 1, 2, 7])
labels = np.array(["Not useful at all: 1", "2", "3", "4", "Very useful: 5"])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.axis("equal")
obj, text, bla = ax.pie(
        values,
        autopct="%1.1f%%",
        colors=colors
        )

# remove the zero elements from visible plot
for elem in bla[:2]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/useful.png", bbox_inches='tight')
plt.close()
###########

# Well organized?
values = np.array([9, 1, 0, 0, 0])
labels = np.array(["Excellent", "Very Good", "Good", "Fair", "Poor"])
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.axis("equal")
obj, text, bla = ax.pie(
        values,
        autopct="%1.1f%%",
        colors=colors
        )

# remove the zero elements from visible plot
for elem in bla[2:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/organized.png", bbox_inches='tight')
plt.close()
###########

# Right Speed
values = np.array([8,2,0,0,0])
labels = np.array(["Excellent", "Very Good", "Good", "Fair", "Poor"])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.axis("equal")
obj, text, bla = ax.pie(
        values,
        autopct="%1.1f%%",
        colors=colors
        )

# remove the zero elements from visible plot
for elem in bla[2:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/speed.png", bbox_inches='tight')
plt.close()
###########

# clearly
values = np.array([10,0,0,0,0])
labels = np.array(["Excellent", "Very Good", "Good", "Fair", "Poor"])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.axis("equal")
obj, text, bla = ax.pie(
        values,
        autopct="%1.1f%%",
        colors=colors
        )

# remove the zero elements from visible plot
for elem in bla[1:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/clearly.png", bbox_inches='tight')
plt.close()
###########



# accessible
values = np.array([9,1,0,0,0])
labels = np.array(["Excellent", "Very Good", "Good", "Fair", "Poor"])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.axis("equal")
obj, text, bla = ax.pie(
        values,
        autopct="%1.1f%%",
        colors=colors
        )

# remove the zero elements from visible plot
for elem in bla[2:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/access.png", bbox_inches='tight')
plt.close()
###########