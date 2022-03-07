def div(a,b):
    print(a/b)

def smart_div(func):  #decorator

   def inner(a,b):
     if a<b:
        a,b =b,a
        return func(a,b)  #changing functionality of function div

   return  inner
div = smart_div(div)
div(2,4)

