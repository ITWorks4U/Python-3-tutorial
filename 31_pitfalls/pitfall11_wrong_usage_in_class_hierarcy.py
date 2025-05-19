###
#	Don't mind of wrong object usage in class hierarcy.
###
class Base():
	a = 0
	b = 1
	
	#....
#end class

class Child1(Base):
	pass
	#....
#end class

class Child2(Base):
	pass
	#....
#end class

'''
	By instanciating the classes you want to, only
	the specific instance will be notify any change.
'''
b = Base()
c1 = Child1()
c2 = Child2()

b.a = 800

print(f'({b.a},{b.b})')
print(f'({c1.a},{c1.b})')
print(f'({c2.a},{c2.b})')


'''
	Since a and b are public by default it's not smart
	to modify the value on the direct way, because your
	child classes also notices that modification.
'''
Base.a = 500
print(f'{Base.a} => {Child1.a} => {Child2.a}')
