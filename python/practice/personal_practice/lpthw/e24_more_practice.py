# Learn Python the hard way
# Exercise 24: More Practice

print "LPTHW Practice"
print "E24: More Practice"
print "Done by Lucas Costa"
print "Date: 01/26/2016"
print "Message: just reviewed all my files"
print ""

print "let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'


poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

print "----------"
print poem
print "----------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
