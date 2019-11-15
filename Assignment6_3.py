class Arithmatic:
	def __init__(self):
		self.Value1=0.0
		self.Value2=0.0
		self.Result=0.0	

	def Accept(self):
		Value1=float(input("Enter Value1 : "))
		Value2=float(input("Enter Value2 : "))
		self.Value1=Value1
		self.Value2=Value2

	def Addition(self):
		self.Result=self.Value1+self.Value2
		return self.Result

	def Substraction(self):
		self.Result=self.Value1-self.Value2
		return self.Result

	def Multiplication(self):
		self.Result=self.Value1*self.Value2
		return self.Result

	def Division(self):
		self.Result=self.Value1/self.Value2
		return self.Result

def main():
	obj1=Arithmatic()
	obj1.Accept()
	result=obj1.Addition()
	print("Addition is : ",result)
	result=obj1.Substraction()
	print("Substraction is : ",result)
	result=obj1.Multiplication()
	print("Multiplication is : ",result)
	result=obj1.Division()
	print("Division is : ",result)
	
	obj2=Arithmatic()
	obj2.Accept()
	result=obj2.Addition()
	print("Addition is : ",result)
	result=obj2.Substraction()
	print("Substraction is : ",result)
	result=obj2.Multiplication()
	print("Multiplication is : ",result)
	result=obj2.Division()
	print("Division is : ",result)	

if (__name__=="__main__"):
	main()