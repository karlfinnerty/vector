
from vector import Vector
from input_components import components
from math import sqrt


def main():

	x1, y1, z1 = components()
	x2, y2, z2 = components()
	u = Vector(x1, y1, z1)
	v = Vector(x2, y2, z2)

	print("multiplying u by 1/sqrt(6)")
	u = u.mult(1/sqrt(6))
	print("u: {}".format(u))
	print("v: {}".format(v))
	print("\n")

	print("u is a unit vector: {}".format(u.is_unit_vector()))
	print("u and v are orthogonal: {}".format(u.is_orthogonal(v)))
	print("u and v are orthonormal: {}".format(u.is_orthonormal(v)))

if __name__ == '__main__':
	main()
