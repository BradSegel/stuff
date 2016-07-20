	.data
firstMsg:		.asciiz	"\nEnter the first number: "
secondMsg:	.asciiz 	"\nEnter the second number: "
answerMsg:	.asciiz 	"\nThe greatest common divisor is:"
loopMsg:		.asciiz 	"\nThe algorithm looped "
loopEndMsg:	.asciiz	" times."

	.text
# initialize values we'll use for the algo
li	$t0, 0 # firstNum becomes high number
li	$t1, 0 # secondNum becomes low number
li	$t2, 0 # value holder
li	$t7, 0 # counter

# ask for first int
li	$v0, 4		
la	$a0, firstMsg
syscall

# read first input from user, pray that it's an int
li	$v0, 5
syscall
move $t0, $v0

# ask for second int
li	$v0, 4
la	$a0, secondMsg
syscall

# read second input from user, pray that it's an int
li	$v0, 5
syscall
move $t1, $v0

main:
# ensure t0 > t1
bgt	$t1, $t0, firstOrder

# incr our counter
add	$t7, $t7, 1
# Subtract the lesser from the larger
sub	$t2, $t0, $t1

# see to it that the 2 lowest terms involved with the 
# subtraction above are in t0, t1 and t0 > t1
bgt	$t1, $t0, reorder1
bgt	$t0, $t1, reorder0

beq	$t0, $t1, finish0 # when they are equal, both hold the GCD
beqz	$t1, finish0  	# when t1 equals 0, t0 holds the GCD   

# there's more to do, do it
j 		main

end:
# tell the user what's happened, then stop
li		$v0, 4
la		$a0, answerMsg
syscall

li		$v0, 1
move	$a0, $t2
syscall

li		$v0, 4
la		$a0, loopMsg
syscall

li		$v0, 1
move	$a0, $t7
syscall

li		$v0, 4
la		$a0, loopEndMsg
syscall

# end gracefully
li		$v0, 10
syscall

firstOrder:
# make sure t0 > t1 when we start
move	$t2, $t0
move	$t0, $t1
move	$t1, $t2
j		main

# t1 > t0
reorder1:
bgt		$t1, $t2, keep21
move	$t2, $t0
move	$t0, $t1
move	$t1, $t2
j		main  # t0 now holds the larger value

# t1 > t2  ( t1 > both)
keep21:
move	$t1, $t2 # set t1 = t2, lose value in t1
j		main  # by transitivity, t0 > t2

# t1 < t0
reorder0:
bgt		$t0, $t2, keep20
j		main  # t0 holds greater value

# t0 > t2 (t0 > both)
keep20:
move 	$t0, $t2 # set t0 = t2, lose value in t0
j		main

finish0:
move 	$t2, $t0
j		end

finish1:
move	$t2, $t1
j		end
