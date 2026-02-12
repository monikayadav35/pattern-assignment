# *
# * *
# * * *
# * * * *
# * * * * *


n=4
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()      
#-------------------------------------------------------------------

# * * * * 
# * * * 
# * * 
# * 

n=4
for i in range(1,n+1):
    for j in range(n-i+1):
        print('*',end=' ')
    print()  
#-------------------------------------------------------------------

#       * 
#     * *
#   * * *
# * * * *

n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for j in range(i):
        print('*',end=' ')
    print()

#-------------------------------------------------------------------

# * * * * 
#   * * *
#     * *
#       *


n=4
for i in range(n+1):
    for j in range(n-n+i):
        print(" ",end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()

#=-------------------------------------------------------------------

# 1 
# 2 2
# 3 3 3
# 4 4 4 4

n=4
for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
    print()    

#-------------------------------------------------------------------

# 1 
# 2 3
# 4 5 6
# 7 8 9 10

n=4
tem=1
for i in range(1,n+1):
    for j in range(i):
        print(tem,end=' ')
        tem+=1
    print()    

#--------------------------------------------------------------------
# A 
# B B
# C C C
# D D D D

n=4
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+i-1),end=' ')
    print()    

#--------------------------------------------------------------------

# A 
# B C
# D E F
# G H I J

n=4
tem=0
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+tem),end=' ')
        tem+=1
    print()   

#--------------------------------------------------------------------

# - - - * 
# - - * *
# - * * *
# * * * *

n=4
for i in range(1,n+1):
    for j in range(i,n):
        print(' ',end=' ')  
    for num in range(1,i+1):
            print(i,end="  ")
    print()

#--------------------------------------------------------------------

#         *   
#       *   *
#     *   *   *
#   *   *   *   *
# *   *   *   *   *

n=5   
for i in range(1,n+1):
        
    for j in range(n,0,-1):
            
     if(j <= i):
                print("*",end="   ")
     else: 
         print(" ",end=" ")  
    print()

#--------------------------------------------------------------------

# *   *   *   *   *   
#   *   *   *   *
#     *   *   *
#       *   *
#         *

n=5   
for i in range(n,0,-1):
        
    for j in range(n,0,-1):
            
     if(j <= i):
                print("*",end="   ")
     else: 
         print(" ",end=" ")  
    print()

#--------------------------------------------------------------------

#                 1   
#               2   2
#             3   3   3
#           4   4   4   4
#         5   5   5   5   5
#       6   6   6   6   6   6
#     7   7   7   7   7   7   7
#   8   8   8   8   8   8   8   8
# 9   9   9   9   9   9   9   9   9


n=9   
for i in range(1,n+1):
        
    for j in range(n,0,-1):
            
     if(j <= i):
                print(i,end="   ")
     else: 
         print(" ",end=" ")  
    print()

#--------------------------------------------------------------------

#                 1   
#               1   2
#             1   2   3
#           1   2   3   4
#         1   2   3   4   5
#       1   2   3   4   5   6
#     1   2   3   4   5   6   7
#   1   2   3   4   5   6   7   8
# 1   2   3   4   5   6   7   8   9   


n=9
for i in range(1,n+1):
    tem=1
        
    for j in range(n,0,-1):
            
     if(j <= i):
                print(tem,end="   ")
                tem+=1
     else: 
         print(" ",end=" ")  
    print()

#--------------------------------------------------------------------

#         *   
#       *   *
#     *   *   *
#   *   *   *   *
# *   *   *   *   *

n=9   
for i in range(1,n+1):
        
    for j in range(n,0,-1):
            
     if(j <= i):
                print("*",end="   ")
     else: 
         print(" ",end=" ")  
    print()


#---------------------------------------------------------------------

# *   *   *   *   *   *   *   *   *   
#   *   *   *   *   *   *   *   *
#     *   *   *   *   *   *   *
#       *   *   *   *   *   *
#         *   *   *   *   *
#           *   *   *   *
#             *   *   *
#               *   *
#                 *

n=9   
for i in range(n,0,-1):
        
    for j in range(n,0,-1):
            
     if(j <= i):
                print("*",end="   ")
     else: 
         print(" ",end=" ")  
    print()

#--------------------------------------------------------------------
# 9   9   9   9   9   9   9   9   9   
#   8   8   8   8   8   8   8   8
#     7   7   7   7   7   7   7
#       6   6   6   6   6   6
#         5   5   5   5   5
#           4   4   4   4
#             3   3   3
#               2   2
#                 1

n=9   
for i in range(n,0,-1):
        
    for j in range(n,0,-1):
            
     if(j <= i):
                print(i,end="   ")
     else: 
         print(" ",end=" ")  
    print()

# --------------------------------------------------------------------
#                 1
#               1 2 1
#             1 2 3 2 1
#           1 2 3 4 3 2 1
#         1 2 3 4 5 4 3 2 1
#       1 2 3 4 5 6 5 4 3 2 1
#     1 2 3 4 5 6 7 6 5 4 3 2 1
#   1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

n=9   
for i in range(1,n+1):
    temp=1
    for j in range(n,0,-1):
            
     if(j <= i):
                print(temp,end=" ")
                temp+=1
     else: 
         print(" ",end=" ")  
    
    temp=i-1
    for j in range(2,n+1):
         
         if j<=i:
              print(temp,end=' ')
              temp-=1
         else:
              print(' ',end=" ")
    print()

#------------------------------------------------------------
#       1       
#     2 3 2     
#   3 4 5 4 3   
# 4 5 6 7 6 5 4

n=4
for i in range(1,n+1):
    tem=i
    for j in range(n,0,-1):
        if j<=i:
         print(tem,end=" ")
         tem+=1
        else:
         print(" ",end=" ")
    tem-=2
    for j in range(2,n+1):
      if j<=i:
         print(tem,end=" ")
         tem-=1
      else:
         print(" ",end=" ")
    print()          
#--------------------------------------------------------------------


n=4
for i in range(1,n+1):
    tem=i
    for j in range(n,0,-1):
        if j<=i:
         print(tem,end=" ")
         tem+=1
        else:
         print(" ",end=" ")
    print()