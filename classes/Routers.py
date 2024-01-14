class MyRouter(object):
    "This is the class which describes about router definition"
    def __init__(self, routerName, model, serialNo, ios):
        self.routername = routerName;
        self.model = model;
        self.serialNo = serialNo;
        self.ios = ios;

    def print_router(self,manuf_date):
        print
        self.manuf_date = manuf_date;
        print("the router name is .. --> ", self.routername)
        print("The router model is .. -->", self.model)
        print("The serial no is .. -->", self.serialNo)
        print("The ios version is .. -->", self.ios)
        print("The manufacturing date is ..-->" + self.manuf_date)