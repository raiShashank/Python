class CartesianPoint:
	pass

cp1 = CartesianPoint()
cp2 = CartesianPoint()
cp1.x = 1.0
cp1.y = 2.0
cp2.x = 1.0
cp2.y = 2.0
cp2.z = 5.0

def samePoint(p1,p2):
	return (p1.x == p2.x) and (p1.y == p2.y)

def main():
	print samePoint(cp1,cp2)
	
if __name__ == '__main__':
	main()
