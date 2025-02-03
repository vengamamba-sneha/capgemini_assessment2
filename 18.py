from abc import ABC, abstractmethod
class ICalculator(ABC):
      @abstractmethod
      def add(self):
        pass
      @abstractmethod
      def subtract(self):
        pass
      @abstractmethod
      def multiply(self):
        pass
      @abstractmethod
      def divide(self):
        pass
class Calculator(ICalculator):
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Addition: {num1+num2}")
    def subtract(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Subtraction: {num1-num2}")
    def multiply(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Multiplication: {num1*num2}")
    def divide(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Division: {num1/num2}")

calc = Calculator()
calc.add(10, 20)
calc.subtract(50, 10)
calc.multiply(105, 46)
calc.divide(10, 2)
    
