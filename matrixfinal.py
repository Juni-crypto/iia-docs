def submains(s,t,a,b,c): 
    for i in range(0,c+1,1):
        for j in range(1,c+1,1):
           # print("(",i,j,")")
            subvectors(i,j,a,b,c,s,t)
            #count=count+1

    for i in range(0,((c-1)+1),1):
        for j in range(c+1,(b+1),1):
           # print("(",i,j,")")
            subvectors(i,j,a,b,c,s,t)
            #count=count+1
        
    for i in range(1,c+1,1):
        for j in range((-c+1),(0+1),1):
           # print("(",i,j,")")
            subvectors(i,j,a,b,c,s,t)
            #count=count+1

    for i in range(1,c+1,1):
        for j in range((-b+1),(-c+1),1):
           # print("(",i,j,")")
            subvectors(i,j,a,b,c,s,t)
            #count=count+1
            
def matrixcheck(i,j,m,n,s,t):
    if((i==m)and(j==n)and(i==s)and(j==t)):
        print("2")
        print("(",s,",",t,")","(",i,",",j,",",m,",",n,")")
    elif(((i==s)and(j==t)and(i,j!=m,n))or((m==s)and(n==t)and(i,j!=m,n))):
        print("1")
        print("(",s,",",t,")","(",i,",",j,",",m,",",n,")")
    elif(((i+m)==s)and((j+n)==t)):
        print("-1")
        print("(",s,",",t,")","(",i,",",j,",",m,",",n,")")
    else:
        print("0")
        print("(",s,",",t,")","(",i,",",j,",",m,",",n,")")
def subvectors(i,j,a,b,c,s,t):
    m=a
    ra=b
    b=c
    count=0
    if((i>=0)and (i<=b) and (j>=1) and (j<=b)): 
        m=i
        for n in range(j,(ra-j+1),1):
            m1=m+i
            n1=n+j
            if((m1>=(-ra+1)) and (m1<=ra) and (n1>=(-ra+1)) and (n1<=ra)):
               #print("(",i,j,")","(",m,n,")")
               matrixcheck(i,j,m,n,s,t)
               #count=count+1
        t1=i+1
        t2=ra-i
        if(t1>t2):
            t2=t2-1
            t3=-1
        else:
            t2=t2+1
            t3=1
        for m in range(t1,t2,t3):
            for n in range((-ra+1),(ra-j+1)):
                m1=m+i
                n1=n+j
                if((m1>=(-ra+1)) and (m1<=ra) and (n1>=(-ra+1)) and (n1<=ra)):
                #    print("(",i,j,")","(",m,n,")")
                    matrixcheck(i,j,m,n,s,t)
                    #count=count+n1
    #print(count)
    #countb=0
    if((i>=0) and (i<=(b-1)) and (j>=(b+1)) and (j<=ra)):
        for m in range((i+1),(ra-i+1)):
            for n in range((-ra+1),(ra-j+1)):
                m1=m+i
                n1=n+j
                if((m1>=(-ra+1)) and (m1<=ra) and (n1>=(-ra+1)) and (n1<=ra)):
                 #   print("(",i,j,")","(",m,n,")")
                    matrixcheck(i,j,m,n,s,t)
        #            countb=countb+1
   # print(countb)
    #countc=0
    if((i>=1) and (i<=b) and (j>=(-b+1)) and (j<=0)):
        m=i
        for n in range((-ra+1-j),j+1):
            m1=m+i
            n1=n+j
            if((m1>=(-ra+1)) and (m1<=ra) and (n1>=(-ra+1)) and (n1<=ra)):
               # print("(",i,j,")","(",m,n,")")
                matrixcheck(i,j,m,n,s,t)
    #            countc=countc+1
        m=i
        for n in range(1,(ra+1)):
            m1=m+i
            n1=n+j
            if((m1>=(-ra+1)) and (m1<=ra) and (n1>=(-ra+1)) and (n1<=ra)):
                #print("(",i,j,")","(",m,n,")")
                matrixcheck(i,j,m,n,s,t)
     #           countc=countc+1
        t1=i+1
        t2=ra-i
        if(t1>t2):
            t2=t2-1
            t3=-1
        else: 
            t2=t2+1
            t3=1
        for m in range(t1,t2,t3):
            for n in range((-ra+1-j),(ra+1)):
                m1=m+i
                n1=n+j
                if((m1>=(-ra+1)) and (m1<=ra) and (n1>=(-ra+1)) and (n1<=ra)):
                 #   print("(",i,j,")","(",m,n,")")
                    matrixcheck(i,j,m,n,s,t)
      #              countc=countc+1
   # print(countc)
    #countd=0
    if((i>=1) and (i<=b) and (j>=(-ra+1)) and (j<=-b)):
        m=i
        for n in range(1,ra+1):
            m1=m+i
            n1=n+j
            if((m1>=(-ra+1)) and (m1<=ra) and (n1>=(-ra+1)) and (n1<=ra)):
              #  print("(",i,j,")","(",m,n,")")
                matrixcheck(i,j,m,n,s,t)
     #           countd=countd+1
        t1=i+1
        t2=ra-i
        if(t1>t2):
            t2=t2-1
            t3=-1
        else:
            t2=t2+1
            t3=1
        for m in range(t1,t2,t3):
            for n in range((-ra+1-j),(ra+1)):
                m1=m+i
                n1=n+j
                if((m1>=(-ra+1)) and (m1<=ra) and (n1>=(-ra+1)) and (n1<=ra)):
               #     print("(",i,j,")","(",m,n,")")
                    matrixcheck(i,j,m,n,s,t)
      #              countd=countd+1
   # print(countd)


a=int(input("enter 2n"))
print (a)
b=int(a/2)
c=int(b/2)
#count=0
for s in range(0,(b+1),1):
    if(s==0):
        for t in range(1,(b+1),1):
            print("---(",s,t,")---")
            submains(s,t,a,b,c)
    else:
        for t in range((-b+1),(b+1)):
            print("(",s,t,")")
            submains(s,t,a,b,c)
            
    
 #       count=count+1

#for s in range(0,((c-1)+1),1):
 #   for t in range(c+1,(b+1),1):
  #      print("(",s,t,")")
   #     submains(s,t)
  #      count=count+1
        
#for s in range(1,c+1,1):
 #   for t in range((-c+1),(0+1),1):
  #      print("(",s,t,")")
   #     submains(s,t)
   #     count=count+1

#for s in range(1,c+1,1):
 #   for t in range((-b+1),(-c+1),1):
  #      print("(",s,t,")")
   #     submains(s,t)
    #    count=count+1
        

        
