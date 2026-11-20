from app.models.customer import Customer
from app.models.address import Address
from decimal import Decimal

def test_create_customer_in_database(db_session):
    address = Address(
        company_name="ABC Transport",
        address_type="OFFICE",
        street="Lipowa",
        building_number="10",
        postal_code="20-001",
        city="Lublin",
        country="Poland",
        latitude=Decimal("51.246500"),
        longitude=Decimal("22.568400")
    )

    db_session.add(address)
    db_session.flush()

    assert address.id is not None

    customer = Customer(
        address_id=address.id,
        email="kontakt@abc-transport.pl",
        phone="500600700",
        contact_person="Jan Kowalski",
        tax_id="1234567890"
    )

    db_session.add(customer)
    db_session.flush()

    assert customer.id is not None
    assert customer.address_id == address.id