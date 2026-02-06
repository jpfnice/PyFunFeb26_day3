data=[34,56,78,89,10,30]

index=input("Pleaser enter an int in the range [0,5]: ")
index=int(index) # may raise a ValueError
print("At position", index, "there is the element", data[index]) # may raise an IndexError 
    
print("The end")