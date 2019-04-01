from faker.factory import Factory
import models

print("hi")

class UserFactory(Factory):

    class Meta:
        model = models.User
