import os

name = "Rahul"
print(name)

new_name = name.lower().strip()
print(new_name)

environment = "productionn    "
environment = environment.lower().strip()

if environment=="production":
    print("ProductionConfig")
elif environment=="development":
    print("DevelopmentConfig")
else:
    raise ValueError("Invalid environment value")
