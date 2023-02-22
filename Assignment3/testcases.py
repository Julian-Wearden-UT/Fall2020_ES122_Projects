from Assignment3 import *


#Problem 1
print("Problem 1 Test Cases:")
#Test Case 1
try:
	if (sortedTheseNumbers(1,4,2,3,5) == [1,2,3,4,5]):
		print("Test Case 1: Passed")
	else:
		print("Test Case 1: Failed")
except:
	print("Test Case 1: Failed")

#Test Case 2
try:
	if (sortedTheseNumbers(1,4,-2.5,3,5) == [-2.5,1,3,4,5]):
		print("Test Case 2: Passed")
	else:
		print("Test Case 2: Failed")
except:
	print("Test Case 2: Failed")

#Test Case 3
try:
	if (sortedTheseNumbers(1,4,2,3,3,3,5, NoDuplicates = True) == [1,2,3,4,5]):
		print("Test Case 3: Passed")
	else:
		print("Test Case 3: Failed")
except:
	print("Test Case 3: Failed")

#Test Case 4
try:
	if (sortedTheseNumbers(1,4,2,3,5, Reverse = True) == [5,4,3,2,1]):
		print("Test Case 4: Passed")
	else:
		print("Test Case 4: Failed")
except:
	print("Test Case 4: Failed")

#Test Case 5
try:
	if (sortedTheseNumbers(1,1,-4,2,3,5, Reverse = True, SortbyAbsoluteValues = True, NoDuplicates = True) == [5,-4,3,2,1]):
		print("Test Case 5: Passed")
	else:
		print("Test Case 5: Failed")
except:
	print("Test Case 5: Failed")

#Test Case 6
try:
	if (sortedTheseNumbers(1,4,2,-3,3,5, SortbyAbsoluteValues = True) == [1,2,3,-3,4,5] or sortedTheseNumbers(1,4,2,-3,3,5, SortbyAbsoluteValues = True) == [1,2,-3,3,4,5]):
		print("Test Case 6: Passed")
	else:
		print("Test Case 6: Failed")
except:
	print("Test Case 6: Failed")

#Test Case 7
try:
	if (sortedTheseNumbers(1,4,2,-3,3,5,5, SortbyAbsoluteValues = True, NoDuplicates = True) == [1,2,3,-3,4,5] or sortedTheseNumbers(1,4,2,-3,3,5,5, SortbyAbsoluteValues = True, NoDuplicates = True) == [1,2,-3,3,4,5]):
		print("Test Case 7: Passed")
	else:
		print("Test Case 7: Failed")
except:
	print("Test Case 7: Failed")

print()


#Problem 2
print("Problem 2 Test Cases:")

#Test Case 1
try:
	p = Point(1,2,3)
	if (p.x == 1 and p.y == 2 and p.z == 3):
		print("Test Case 1: Passed")
	else:
		print("Test Case 1: Failed")
except:
	print("Test Case 1: Failed")

#Test Case 2
try:
	p = Point(1,2,3)
	if (str(p) == "(1, 2, 3)" or str(p) == "(1.0, 2.0, 3.0)"):
		print("Test Case 2: Passed")
	else:
		print("Test Case 2: Failed")
except:
	print("Test Case 2: Failed")

#Test Case 3
try:
	p = Point(1,2,3)
	PCD = PointCloudData([p])
	if (PCD.points == [p]):
		print("Test Case 3: Passed")
	else:
		print("Test Case 3: Failed")
except:
	print("Test Case 3: Failed")

#Test Case 4
try:
	p = Point(1,2,3)
	PCD = PointCloudData([p])
	p1 = Point(1,1,1)
	PCD.add(p1)
	if (PCD.points == [p, p1]):
		print("Test Case 4: Passed")
	else:
		print("Test Case 4: Failed")
except:
	print("Test Case 4: Failed")

#Test Case 5
try:
	p = Point(1,2,3)
	p1 = Point(1,1,1)
	PCD = PointCloudData([p, p1])
	PCD.remove(Point(1,1,1))
	if (PCD.points == [p]):
		print("Test Case 5: Passed")
	else:
		print("Test Case 5: Failed")
except:
	print("Test Case 5: Failed")

#Test Case 6
try:
	p = Point(1,2,3)
	p1 = Point(1,1,1)
	PCD = BoundingBox([p, p1])
	if (PCD.points == [p, p1]):
		print("Test Case 6: Passed")
	else:
		print("Test Case 6: Failed")
except:
	print("Test Case 6: Failed")

#Test Case 7
try:
	p = Point(1,2,3)
	p1 = Point(1,1,1)
	PCD = BoundingBox([p, p1])
	if (PCD.center == Point(1,1.5,2) and PCD.dimensions == [0,1,2]):
		print("Test Case 7: Passed")
	else:
		print("Test Case 7: Failed")
except:
	print("Test Case 7: Failed")

#Test Case 8
try:
	p = Point(1,2,3)
	p1 = Point(1,1,1)
	PCD = BoundingBox([p, p1])
	PCD.add(Point(3,3,3))
	PCD.updateBox(PCD.points)
	if (PCD.center == Point(2,2,2) and PCD.dimensions == [2,2,2]):
		print("Test Case 8: Passed")
	else:
		print("Test Case 8: Failed")
except:
	print("Test Case 8: Failed")

#Test Case 9
try:
	p = Point(3,3,3)
	p1 = Point(1,1,1)
	BB1 = BoundingBox([p, p1])
	BB2 = BoundingBox([Point(2,2,2), Point(4,4,4)])

	if (BB1.collisionCheck(BB2) and BB2.collisionCheck(BB1)):
		print("Test Case 9: Passed")
	else:
		print("Test Case 9: Failed")
except:
	print("Test Case 9: Failed")


#Test Case 10
try:
	p = Point(3,3,3)
	p1 = Point(1,1,1)
	BB1 = BoundingBox([p, p1])
	BB2 = BoundingBox([Point(5,5,5), Point(4,4,4)])

	if (BB1.collisionCheck(BB2) or BB2.collisionCheck(BB1)):
		print("Test Case 10: Failed")
	else:
		print("Test Case 10: Passed")
except:
	print("Test Case 10: Failed")

#Test Case 11
try:
	p = Point(3,3,3)
	p1 = Point(1,1,1)
	BB1 = BoundingBox([p, p1])
	BB2 = BoundingBox([Point(5,5,5), Point(4,4,4)])
	BB3 = BB1 + BB2

	if (BB3.center == Point(3,3,3) and BB3.dimensions == [4,4,4]):
		print("Test Case 11: Passed")
	else:
		print("Test Case 11: Failed")
except:
	print("Test Case 11: Failed")

#Test Case 12
try:
	p = Point(3,3,3)
	p1 = Point(1,1,1)
	BB1 = BoundingBox([p, p1])
	if (len(BB1) == 8):
		print("Test Case 12: Passed")
	else:
		print("Test Case 12: Failed")
except:
	print("Test Case 12: Failed")


print()
