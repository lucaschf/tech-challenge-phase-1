from factory import Faker
from faker import Faker as Fk

from .providers import CPFProvider

fk = Fk()

# Overwrite the factory.Faker's default _get_faker method.
# We do this so that when creating instances of the factory.Faker class, they will use our custom fk
# instance, which has been configured with the custom providers
Faker._get_faker = lambda *_: fk

# Add custom providers to the Faker instance
fk.add_provider(CPFProvider)
