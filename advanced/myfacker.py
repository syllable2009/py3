from faker import Faker

faker = Faker('zh_CN')
print('name:', faker.name())
print('phone:', faker.phone_number())
print('address:', faker.address())
print('text:', faker.text())