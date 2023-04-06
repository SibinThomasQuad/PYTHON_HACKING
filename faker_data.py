from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Generate a fake name
name = fake.name()

# Generate a fake email
email = fake.email()

# Generate a fake password
password = fake.password()

phone = fake.phone_number()

# Print the registration data
print("Name:", name)
print("Email:", email)
print("Password:", password)
print("Phone:", phone)
