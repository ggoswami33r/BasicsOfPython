from classes.Routers import MyRouter;
from classes.MyNewRouter import  MyNewRouter;





router1 = MyRouter("R1","2600","123456","Oxygen")


print(router1.routername)
print(router1.serialNo)
print(router1.ios)
print(router1.model)
print("First Prinring router with manuf date")
router1.print_router("20102018")#  its  not working need to check on urgent basis


router2 = MyRouter("R2","2700","456789","Kitkat")

print(router2.routername)
print(router2.serialNo)
print(router2.ios)
print(router2.model)


print(getattr(router1,"ios"))
setattr(router2,"ios","BlackBerry")
print(getattr(router2,"ios"))

router2.serialNo = 2800
print(getattr(router2,"serialNo"))

print(hasattr(router2,"ios"))
print(hasattr(router2,"routerManufCompany"))


#delattr((router2,"ios"))

print(hasattr(router2,"ios"))

print(isinstance(router2, MyRouter))
#print(isinstance(router3,MyRouter))

newRouter1 = MyNewRouter("NewRouterName","latest","12345","Oxyzen_latest","99999");
print("Print new Router..")
newRouter1.print_router("20242024");

print("Print my new router1")
newRouter1.print_new_router("123451234")

print("Checking if MyNewRouter is a subclass of MyRouter or not")

print(issubclass(MyNewRouter,MyRouter))