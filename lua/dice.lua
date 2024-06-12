-- Let's write a first program in Lua
function dice()
    return math.random(1,6)
    end

print("Tell me a number of dice. I will throw them!")
n = io.read("*number")
for i = 1,n-1,1
    do
        print(dice())
    end
print("That's all!")
