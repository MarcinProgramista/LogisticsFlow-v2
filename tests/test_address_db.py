from app.models.address import Address
from decimal import Decimal

def test_create_address_in_database(db_session):
    address = Address(
        company_name="ABC Transport",
        address_type="OFFICE",
        street="Lipowa",
        building_number="10",
        postal_code="20-001",
        city="Lublin",
        country="Poland",
        latitude=Decimal("50.061400"),
        longitude=Decimal("22.004700")
    )

    db_session.add(address)
    db_session.flush()

    assert address.id is not None

    saved_address = db_session.query(Address).filter_by(id=address.id).first()

    assert saved_address is not None
    assert saved_address.city == "Lublin"
    assert saved_address.company_name == "ABC Transport"
    assert saved_address.latitude == Decimal("50.061400")
    assert saved_address.longitude == Decimal("22.004700")
