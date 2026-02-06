"""
Given a file like the following:
    lausanne:6.3
    geneve:3.2
    nyon:4.3
    lausanne:7.3
    geneve:3.7
    nyon:2.3
    lausanne:5.3
    geneve:5.2
    nyon:2.3
    
makes use of it the create a dict like this one:
    
    {
     "lausanne":[6.3,7.3,5.3],
     "geneve":[3.2,3.7,5.2],
     "nyon":[4.3,2.3,2.3]
     }
    
then use the dict to find the average of the temperature associated with a 
given city name.
"""

