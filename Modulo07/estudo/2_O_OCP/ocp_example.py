# SOLID - Open/Closed Principle (OCP)

class Programmer:
    def make(self) -> None:
        print("Programmer creating code")


class Seller:
    def make(self) -> None:
        print("Seller selling the product")


class HumanResources:
    def make(self) -> None:
        print("Human Resources hiring new devs")


class Company:
    def do_work(self, worker: any) -> None:
        # if worker == 1:
        #     print("Programmer creating code")
        # elif worker == 2:
        #     print("Seller selling the product")
        # elif worker == 3:
        #     print("Human Resources hiring new devs")
        # elif worker == 4:
        #     print("Frontend raising bugs for production")
        # else:
        #     print("Error, no Worker!")
        worker.make()


programmer = Programmer()
seller = Seller()
human_resources = HumanResources()
company = Company()

company.do_work(programmer)
company.do_work(seller)
company.do_work(human_resources)
