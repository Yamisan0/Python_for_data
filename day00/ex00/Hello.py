ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here

#list
ft_list[1] = "World"

#tuples
y = list(ft_tuple)
y[1] = "France"
ft_tuple = tuple(y)

#set
ft_set.remove("tutu!")
ft_set.add("Paris")

#dictionary
ft_dict["Hello"] = "42Paris"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)