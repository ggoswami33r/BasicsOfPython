from classes.Routers import MyRouter;
class MyNewRouter(MyRouter):
    def __init__(self, routerName, model, serialNo, ios, portsNo):
        #super().__init__(routerName, model, serialNo, ios)
        MyRouter.__init__(self,routerName, model, serialNo, ios);
        self.portsNo = portsNo;

    def print_new_router(self,string):
        print(string + self.model)