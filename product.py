product1_price=30
product2_price=50
product3_price=80
product1=int(input())
product2=int(input())
product3=int(input())
l=[product1,product2,product3]
for i in l:
    print(i)
if(product1<0 or product2<0 or product3<0):
    print("please enter a positive number")
else:
    print("The amount to pay is:")
    total=product1*product1_price+product2*product2_price+product3*product3_price
    x=open("pricedata.txt","a")
    print("price of allproducts:")#to show line in terminal as well
    print("price of all products",file=x)
    dict={product1:product1_price,product2:product2_price,product3:product3_price}
    for k,v in dict.items():
        print(k,v)
        print(k,v,file=x)
    print("total amount is:",total)
    print(total,file=x)
    