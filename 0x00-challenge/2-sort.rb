# Skip non-integer arguments and convert integer arguments to integers
result = ARGV.select { |arg| arg =~ /^-?[0-9]+$/ }.map(&:to_i)

# Sort the integer arguments in ascending order
result.sort!

# Print the sorted integers to the standard output stream
puts result
