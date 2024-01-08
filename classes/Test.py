from classes.Routers import MyRouter;





router1 = MyRouter("R1","2600","123456","Oxygen")


print(router1.routername)
print(router1.serialNo)
print(router1.ios)
print(router1.model)
#router1.print_router("20102018")


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