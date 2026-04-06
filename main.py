import random as r 



def Random_rates(num_elm,num_set):
    time = num_elm 
   
    t_r = []
    x = 0 
    for x in range(num_set):
        r_r = [0]
        for i in range(time):
            x = (r_r[i-1]+r.uniform(-0.5,0.5))
        if x > 0:
            del r_r[0]
            r_r.append(x)
            t_r.append(r_r)
    
        
    return t_r

print(Random_rates(2,3))


        
            
