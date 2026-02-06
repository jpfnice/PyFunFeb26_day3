"""
    "w", "a", "r" (default), "r+", "w+", "a+"
"""
# os os.path 
with open("data.out", "a") as myfile:
   print("another line", file=myfile)

    
print("The end")