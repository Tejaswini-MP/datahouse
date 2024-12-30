import pricefinder 
a = input('please enter the locality')
print('locality is :'+ a)
length = input('Enter the length')
print('Length is :'+ length)
breadth = input('Enter the breadth')
print('Length is :'+ breadth)
typeofhouse = input('enter only built or non-built')
print('type of house :'+typeofhouse)
price=pricefinder.prices()
print(price)

