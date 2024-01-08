class MyRouter(object):
    "This is the class which describes about router definition"
    def __init__(self, routername, model, serialNo, ios):
        self.routername = routername;
        self.model = model
        self.serialNo = serialNo;
        self.ios = ios;
    def print_router( manuf_date, self):
        print("the router name is .. --> ", self.routername)
        print("The router model is .. -->", self.model)
        print("The serial no is .. -->", self.serialNo)
        print("The ios version is .. -->", self.ios)
        print("The model and date combined .. -->", self.model + self.manuf_date)