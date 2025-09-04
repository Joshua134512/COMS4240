def println(string):
    print(str(string)+"\n")

#append
print("Append")
l = ["Apple", "Banana", "Orange"]
print(l)
l.append("Grape")
println(l)

#clear
print("Clear")
l.clear()
println(l)

#copy
print("Copy")
l2 = ["Watermelon"]
print(l2)
l1 = l2.copy()
println(l1)

#count
print("Count")
l = ["Watermelon", "Blueberry", "Watermelon"]
print(l)
println(l.count("Watermelon"))

#extend
print("Extend")
l2 = ["Banana", "Pear"]
print(l2)
l.extend(l2)
println(l)

#index
print("Index")
print(l)
println("Index of blueberry is: " + str(l.index("Blueberry")))

#insert
print("Insert")
l.insert(1, "Kiwi")
println(l)

#pop
print("Pop")
print(l)
print(l.pop(4))
println(l)

#remove
print("Remove")
l.remove("Watermelon")
println(l)

#reverse
print("Reverse")
l.reverse()
println(l)

#sort
print("Sort")
l.sort()
println(l)