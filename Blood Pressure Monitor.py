# Project to visualize blood pressure readings, and create an average for the readings.
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Title for chart
now = datetime.now()
time = now.strftime("%H:%M:%S")
date = now.strftime("%m/%d/%Y")
print(f"{date}, {time} \n Knowing your blood pressure is vital to maintain a healthy heart.\n Enter your last 15 blood pressure readings to create an average of your blood pressure.\n WARNNING: Even though this application is creating an average, you should always seek medical attention if your readings are too high or too low.")

# Empty list for the blood pressure readings.
systolic_rate = []
diastolic_rate = []
print(" \n Please enter your systolic rate.")

# While loop to create a list for systolic rate readings.
while len(systolic_rate) != 15:
    try:
        systolic_input = int(input(f"{len(systolic_rate) + 1}.) Systolic rate: "))
        if systolic_input >= 160:
            if systolic_input > 350:
                print(f"{systolic_input} is not a valid input, number is too high.")
            else:
                question = input(f"Is {systolic_input} correct? \n (Y/N) ")
                if question == "Y".lower() or question == "Yes".lower():
                    systolic_rate.append(systolic_input)
                elif question == "N".lower() or question == "No".lower():
                    print(f"Re-enter systolic rate")
                else:
                    print("Not a valid input.")
        elif systolic_input <= 90:
            if systolic_input < 40:
                print(f"{systolic_input} is not a valid input, number is too low.")
            else:
                question = input(f"Is {systolic_input} correct? \n (Y/N) ")
            if question == "Y".lower() or question == "Yes".lower():
                systolic_rate.append(systolic_input)
            elif question == "N".lower() or question == "No".lower():
                print(f"Re-enter systolic rate")
            else:
                print("Not a valid input.")
        else:
            systolic_rate.append(systolic_input)
    except ValueError:
        print("Not a valid entry.")

print("\n Awesome! \n Please enter your diastolic rate.")

# While loop to create a list for diastolic rate readings.
while len(diastolic_rate) != 15:
    try:
        diastolic_input = int(input(f"{len(diastolic_rate) + 1}.) Diastolic rate: "))
        if diastolic_input >= 90:
            if diastolic_input > 300:
                print(f"{diastolic_rate} is not a valid input, number is too high.")
            else:
                question = input(f"Is {diastolic_input} correct? \n (Y/N) ")
                if question == "Y".lower() or question == "Yes".lower():
                    diastolic_rate.append(diastolic_input)
                elif question == "N".lower() or question == "No".lower():
                    print(f"Re-enter diastolic rate")
                else:
                    print("Not a valid input.")
        elif diastolic_input <= 60:
            if diastolic_input < 30:
                print(f"{diastolic_input} is not a valid input, number is too low.")
            else:
                question = input(f"Is {diastolic_input} correct? \n (Y/N) ")
            if question == "Y".lower() or question == "Yes".lower():
                diastolic_rate.append(diastolic_input)
            elif question == "N".lower() or question == "No".lower():
                print(f"Re-enter diastolic rate")
            else:
                print("Not a valid input.")
        else:
            diastolic_rate.append(diastolic_input)
    except ValueError:
        print("Not a valid entry.")

# Using Numpy to create averages, minimum and maximum readings for the user to read.
systolic_average = np.average(systolic_rate)
diastolic_average = np.average(diastolic_rate)
systolic_max = np.amax(systolic_rate)
diastolic_max = np.amax(diastolic_rate)
systolic_min = np.amin(systolic_rate)
diastolic_min = np.amin(diastolic_rate)

# Average is then modified to create a statement for your blood pressure.
if systolic_average > 180 or diastolic_average > 110:
    print(f"Your blood pressure average is {round(systolic_average,2)}/{round(diastolic_average,2)} mmHg. Your average is classified as Hypertension Stage 3.")
elif systolic_average >= 160 or diastolic_average >= 100:
    print( f"Your blood pressure average is {round(systolic_average,2)}/{round(diastolic_average,2)} mmHg. Your average is classified as Hypertension Stage 2.")
elif systolic_average >= 140 or diastolic_average >= 90:
    print(f"Your blood pressure average is {round(systolic_average,2)}/{round(diastolic_average,2)} mmHg. Your average is classified as Hypertension Stage 1.")
elif systolic_average >= 130 or diastolic_average >= 85:
    print(f"Your blood pressure average is {round(systolic_average,2)}/{round(diastolic_average,2)} mmHg. Your average is classified as High Normal or Prehypertension.")
elif systolic_average >= 120 or diastolic_average >= 80:
    print(f"Your blood pressure average is {round(systolic_average,2)}/{round(diastolic_average,2)} mmHg. Your average is classified as Normal.")
elif systolic_average >= 105 or diastolic_average >= 60:
    print(f"Your blood pressure average is {round(systolic_average,2)}/{round(diastolic_average,2)} mmHg. Your average is classified as Ideal.")
else:
    print(f"Your blood pressure average is {round(systolic_average,2)}/{round(diastolic_average,2)} mmHg. Your average is classified as Hypotension.")

# Range of systolic and diastolic rates.
print(f"Your systolic range is {systolic_min}-{systolic_max}. Your diastolic range is {diastolic_min}-{diastolic_max}.")

# Variables for chart.
bp_reading = zip(systolic_rate, diastolic_rate)
x_axis = range(0, 15)
y_axis = list(bp_reading)
label_1 = "Systolic Rate"
label_2 ="Diastolic Rate"

# Using a scatter plot to chart inputs.
plt.style.use("seaborn")
plt.scatter(x_axis,[s for (s,d) in y_axis], c="darkcyan", marker="D", zorder=2)
plt.scatter(x_axis, [d for (s, d) in y_axis], c="navy", marker="D", zorder=2)
plt.legend([label_1, label_2], frameon=True, shadow=True)
plt.plot((x_axis, x_axis), ([s for (s,d) in y_axis],[d for (s, d) in y_axis]), c="black", linestyle="dotted", zorder=1)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], ["Reading 1", "Reading 2", "Reading 3", "Reading 4", "Reading 5", "Reading 6", "Reading 7", "Reading 8", "Reading 9", "Reading 10", "Reading 11", "Reading 12", "Reading 13", "Reading 14", "Reading 15"], rotation=30)
plt.ylim(30, 250)
plt.xlabel("User Entries")
plt.ylabel("Millimeters of Mercury (mmHg)")
plt.title(f"Blood Pressure Entries: {date}")
plt.tight_layout()
plt.show()