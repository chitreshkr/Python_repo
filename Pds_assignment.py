for a in range(1,11):
    for b in range(1,11):
        my_dict={}
        key=1
        for x in range(1,101):
            init=x
            ls=[]
            count=0
            while x not in ls:
                ls+=[x]
                x=x//2 if x%2==0 else a*x+b
                count+=1
                if x in ls:
                    index=ls.index(x)
                    #print('a=',a, 'b=',b, 'x=',init)
                    #print('it converges', 'steps=',count)
                    #print(ls)
                    #print(index)
                    #print(list(ls[index:]))
                    pattern=list(ls[index:])
                    pattern.sort()
                    if pattern not in my_dict.values():
                        my_dict[key]=pattern
                        #print(my_dict)
                        key+=1
                        break
                if count==100:
                    #print('a=',a, 'b=',b, 'x=',init)
                    #print('does not converge')
                    break
        print('a=',a, ' b=',b, '  unique_holding_patterns=',len(my_dict))