capacity = 4 
processList = [ 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2] 
                  
s = []  
pageFaults = 0
  
for i in processList: 
    if i not in s: 
        if(len(s) == capacity): 
            s.remove(s[0]) 
            s.append(i) 
  
        else: 
            s.append(i) 
  
        pageFaults +=1
    else: 
        s.remove(i) 
        s.append(i) 
    print(s)
      
print("{}".format(pageFaults)) 
