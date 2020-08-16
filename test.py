# import requests

# response = requests.get("https://api.github.com/users/AndresJejen/events?page=1&per_page=2")

# print("Status code: ", response.status_code)
# print("Printing Entire Post Request")
# result = response.json()
# print(len(list(result)))
# print(result)
# print(type(result))

# def fun1(number, other):
#     def fun2(x, y):
#         return x +y
#     return fun2(number,other)

# print(fun1(9,4))


x = [(i, {"value": f"parte_{i}"}) for i in range(5)]

result = { value["value"]: key for key, value in x }

print(result)