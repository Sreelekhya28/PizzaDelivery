def order():
  print("********WELCOME!*********")
  dic={1:'Small',2:'Medium',3:'Large'}
  dic1={'BBQ Chicken Pizza':250,'Cheese Pizza':200,'Veg Pizza':190}
  lis=[]
  lis1=[]
  lis2=[]
  bill=0
  n=int(input("Number of Pizzas you want to Order: "))
  print("\n")
  for i in range(n):
    print("Menu : ")
    print(dic1)
    print("\n")
    print("Order ",i+1," from list: ")
    try:
      y=input()
      if y not in dic1:
        raise Exception
    except:
      print("Error!...")
    lis1.append(dic1.get(y))
    lis2.append(y)
    print("Size of Pizza :")
    print(dic)
    print("\n")
    print("Size of Order ",i+1," from list :")
    try:
      x=int(input())
      if x>len(dic):
        raise Exception
      lis.append(dic.get(x))
    except:
      print("Error!...Doesn't Exist..")
    else:
      print("*********")
    finally:
      print("Order is : ",lis2)
      print("Cost is : ",lis1)
      print("Size is : ",lis)
      print("\n")
      print("----------------------------------------------------------------")
      print("\n")
  fo=open('pizza.txt','a')
  for(it,ele,le) in zip(lis2,lis,lis1):
    fo.write(str(it))
    fo.write(' - ')
    fo.write(str(ele))
    fo.write(' : ')
    fo.write(str(le))
    fo.write('\n')
    fo.write('~~~~~~~~~~~~')
    fo.write('\n')
  fo.close()
 # fo=open('pizza.txt','r')
 # print(fo.read())
  for b in lis1:
    bill=bill+b
  print("Bill is : ",bill)
  print("*************")
order()
print("Thank You!!")
