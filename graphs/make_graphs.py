import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pylab


# Some help for coloring
slices = [1,2,3] * 4 + [20, 25, 30] * 2
cmap = plt.cm.prism
colors = cmap(np.linspace(0., 1., len(slices)))

# Course graphs
###############

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

fig.savefig("graphs/course/overall.png", bbox_inches='tight')
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
plt.savefig("graphs/course/part_univ.png", bbox_inches='tight')
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

fig.savefig("graphs/course/useful.png", bbox_inches='tight')
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

fig.savefig("graphs/course/organized.png", bbox_inches='tight')
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

fig.savefig("graphs/course/speed.png", bbox_inches='tight')
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

fig.savefig("graphs/course/clearly.png", bbox_inches='tight')
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

fig.savefig("graphs/course/access.png", bbox_inches='tight')
plt.close()
###################################




# Bootcamp graphs
#################


# 1)

# Bootcamp overall
values = np.array([4,6,0,0,0])
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

fig.savefig("graphs/bootcamp/overall.png", bbox_inches='tight')
plt.close()


# Which part of the university are you from?
x_list_university = [4, 4, 1]
label_list_university = ["Department of Economics", "Harris School of Public Policy", "Booth School of Business"]
plt.axis("equal")
plt.pie(
        x_list_university,
        autopct="%1.1f%%",
        colors=colors
        )
plt.legend(label_list_university, loc='center left', bbox_to_anchor=(0.9, 0.5))
plt.savefig("graphs/bootcamp/part_univ.png", bbox_inches='tight')
plt.close()


# How well did Philipp meet his goal ...

# to clearly explain the objectives
values = np.array([7,3,0,0,0])
labels = np.array(["Excellent", "Very Good", "Good", "Fair", "Poor"])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.axis("equal")
obj, text, bla = ax.pie(
        values,
        autopct="%1.1f%%",
        colors=colors
        )

for elem in bla[2:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/bootcamp/objectives.png", bbox_inches='tight')
plt.close()

# to be well organized
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

for elem in bla[1:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/bootcamp/organized.png", bbox_inches='tight')
plt.close()


# present at right speed
values = np.array([6,4,0,0,0])
labels = np.array(["Excellent", "Very Good", "Good", "Fair", "Poor"])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.axis("equal")
obj, text, bla = ax.pie(
        values,
        autopct="%1.1f%%",
        colors=colors
        )

for elem in bla[2:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/bootcamp/speed.png", bbox_inches='tight')
plt.close()


# present clearly and understandably
values = np.array([7,3,0,0,0])
labels = np.array(["Excellent", "Very Good", "Good", "Fair", "Poor"])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.axis("equal")
obj, text, bla = ax.pie(
        values,
        autopct="%1.1f%%",
        colors=colors
        )

for elem in bla[2:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/bootcamp/clearly.png", bbox_inches='tight')
plt.close()


# to be accessible
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

for elem in bla[1:]:
  elem.set_visible(False)

ax.legend(labels=labels, loc='center left', bbox_to_anchor=(0.9, 0.5))

fig.savefig("graphs/bootcamp/access.png", bbox_inches='tight')
plt.close()