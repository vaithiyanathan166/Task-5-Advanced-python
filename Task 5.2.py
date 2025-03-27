#write a python code using lambda function to check every element of a list is an integer or string?

data = [10, "hello", 25, "world", 42, "python", 99]

# Lambda function to check type
check_type = list(map(lambda x: "Integer" if isinstance(x, int) else "String", data))

# Printing the result
print(check_type)
