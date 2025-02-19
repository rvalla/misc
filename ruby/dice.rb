# Let's write a first program in Ruby
puts "Testing ruby with a virtual dice"
dice = Random.rand(1..6)
puts "I got this number: "
puts dice
if dice > 4
  puts "You were lucky!"
else
  puts "It was not bad...!"
end
