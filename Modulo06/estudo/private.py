class MyClass:
  
  # Método público
  def method_1(self) -> None:
    print("method_1")
    
  def registry(self) -> None:
    print("Start process...")
    self.__verify()
    self.__verify_registry()
    self.__insert_data()
  
  # Método privado
  def __method_2(self) -> None:
    print("method_2")
    
  def __verify(self) -> None:
    print("Verifying data...")
    
  def __verify_registry(self) -> None:
    print("Verifying registry...")
    
  def __insert_data(self) -> None:
    print("Inserting in database...")
    
    
obj = MyClass()
obj.method_1()
# obj.__method_2()
obj.registry()