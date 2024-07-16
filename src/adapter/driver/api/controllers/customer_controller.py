from src.adapter.driver.api.schemas import CustomerCreationIn, CustomerOut
from src.core.application.use_cases import CreateCustomerUseCase, GetCustomerByCpfUseCase
from src.core.domain.entities.customer import Customer


class CustomerController:
    """This class manages customer-related actions using CustomerUseCase.

    The class acts as the intersection between the API and the business logic,
    handling HTTP requests related to customer data.

    Attributes:
        _customer_use_case (CustomerUseCase): An instance of the CustomerUseCase class for
        performing operations related to customers.
    """

    def __init__(
        self,
        create_customer_use_case: CreateCustomerUseCase,
        get_customer_by_cpf_use_case: GetCustomerByCpfUseCase,
    ) -> None:
        self._customer_use_case = create_customer_use_case
        self._get_customer_by_cpf_use_case = get_customer_by_cpf_use_case

    def create_customer(self, customer: CustomerCreationIn) -> CustomerOut:
        """Registers a new customer in the system from the provided customer data.

        Args:
            customer (CustomerCreationIn): The schema containing the necessary information to create
             a new customer.

        Returns:
            CustomerOut: The schema of the successfully registered customer.

        Raises:
            HTTPException: If there's any business rule violation defined in DomainError.
        """
        created_customer: Customer = self._customer_use_case.execute(customer.to_customer_data())
        return CustomerOut.from_entity(created_customer)

    def get_by_cpf(self, cpf: str) -> CustomerOut:
        """Retrieves a customer from the system using their CPF.

        Args:
            cpf (str): The customer's CPF to find the matching customer.

        Returns:
            CustomerOut: The schema of the customer found.

        Raises:
            HTTPException: If a customer with the provided CPF could not be found or there's any
            business rule violation defined in DomainError.
        """
        customer: Customer | None = self._get_customer_by_cpf_use_case.execute(cpf)
        return CustomerOut.from_entity(customer)


__all__ = ["CustomerController"]
