# Design a program that determines the award a person competing in a triathlon will receive.
# Your program should read in the times (in minutes) for all three events of a triathlon, namely swimming, cycling, and running, and then calculate and display the total time taken to complete the triathlon.
swimming = int(input("Please enter your swimming time: "))
cycling = int(input("Please enter your cycling time: "))
running = int(input("Please enter your running time: "))
# The award a participant receives is based on the total time taken to complete the triathlon. 
totalTime = swimming + cycling + running
print("The total time for your Triathlon is {} minutes.".format(totalTime))
# The qualifying time for awards is 100 minutes.
# Display the award that the participant will receive based on the following criteria:
# Within the qualifying time. 0 - 100 minutes Provincial Colours
if totalTime <= 100:
    print("Congratulations! You have won Provincial Colours")
# Within 5 minutes of the qualifying time. 101 - 105 minutes Provincial Half Colours
elif totalTime <= 105:
    print("Congratulations! You have won Provincial Half Colours")
# Within 10 minutes of the qualifying time. 106 - 110 minutes Provincial Scroll
elif totalTime <= 110:
    print("Congratulations! You have won a Provincial Scroll")
# More than 10 minutes off from the qualifying time. 111+ minutes No award
else:
    print("Well done for finishing the Triathlon.  No Award is made for your finishing time")