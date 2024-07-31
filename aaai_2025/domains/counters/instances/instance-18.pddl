;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_40_1)
	(:domain fn-counters)
	(:objects
		c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12 c13 c14 c15 c16 c17 c18 c19 c20 c21 c22 c23 c24 c25 c26 c27 c28 c29 c30 c31 c32 c33 c34 c35 c36 c37 c38 c39 - counter
	)

	(:init
		(= (max_int) 80)
		(= (value c0) 24)
		(= (value c1) 32)
		(= (value c2) 17)
		(= (value c3) 3)
		(= (value c4) 13)
		(= (value c5) 51)
		(= (value c6) 52)
		(= (value c7) 75)
		(= (value c8) 69)
		(= (value c9) 58)
		(= (value c10) 47)
		(= (value c11) 23)
		(= (value c12) 78)
		(= (value c13) 31)
		(= (value c14) 3)
		(= (value c15) 42)
		(= (value c16) 39)
		(= (value c17) 74)
		(= (value c18) 39)
		(= (value c19) 54)
		(= (value c20) 50)
		(= (value c21) 79)
		(= (value c22) 50)
		(= (value c23) 62)
		(= (value c24) 16)
		(= (value c25) 67)
		(= (value c26) 16)
		(= (value c27) 9)
		(= (value c28) 25)
		(= (value c29) 71)
		(= (value c30) 49)
		(= (value c31) 76)
		(= (value c32) 28)
		(= (value c33) 55)
		(= (value c34) 74)
		(= (value c35) 76)
		(= (value c36) 13)
		(= (value c37) 77)
		(= (value c38) 52)
		(= (value c39) 22)
		(= (total_cost) 0)
	)

	(:goal
		(and
			(<= (+ (value c0) 1) (value c1))
			(<= (+ (value c1) 1) (value c2))
			(<= (+ (value c2) 1) (value c3))
			(<= (+ (value c3) 1) (value c4))
			(<= (+ (value c4) 1) (value c5))
			(<= (+ (value c5) 1) (value c6))
			(<= (+ (value c6) 1) (value c7))
			(<= (+ (value c7) 1) (value c8))
			(<= (+ (value c8) 1) (value c9))
			(<= (+ (value c9) 1) (value c10))
			(<= (+ (value c10) 1) (value c11))
			(<= (+ (value c11) 1) (value c12))
			(<= (+ (value c12) 1) (value c13))
			(<= (+ (value c13) 1) (value c14))
			(<= (+ (value c14) 1) (value c15))
			(<= (+ (value c15) 1) (value c16))
			(<= (+ (value c16) 1) (value c17))
			(<= (+ (value c17) 1) (value c18))
			(<= (+ (value c18) 1) (value c19))
			(<= (+ (value c19) 1) (value c20))
			(<= (+ (value c20) 1) (value c21))
			(<= (+ (value c21) 1) (value c22))
			(<= (+ (value c22) 1) (value c23))
			(<= (+ (value c23) 1) (value c24))
			(<= (+ (value c24) 1) (value c25))
			(<= (+ (value c25) 1) (value c26))
			(<= (+ (value c26) 1) (value c27))
			(<= (+ (value c27) 1) (value c28))
			(<= (+ (value c28) 1) (value c29))
			(<= (+ (value c29) 1) (value c30))
			(<= (+ (value c30) 1) (value c31))
			(<= (+ (value c31) 1) (value c32))
			(<= (+ (value c32) 1) (value c33))
			(<= (+ (value c33) 1) (value c34))
			(<= (+ (value c34) 1) (value c35))
			(<= (+ (value c35) 1) (value c36))
			(<= (+ (value c36) 1) (value c37))
			(<= (+ (value c37) 1) (value c38))
			(<= (+ (value c38) 1) (value c39))
		)
	)

	(:metric minimize
		(total_cost)
	)

)