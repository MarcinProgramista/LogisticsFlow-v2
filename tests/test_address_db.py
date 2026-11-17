from app.models.address import Address

def test_create_address_in_database(db_session):
    address = Address(
        company_name="ABC Transport",
        address_type="OFFICE",
        street="Lipowa",
        building_number="10",
        postal_code="20-001",
        city="Lublin",
        country="Poland"
    )

    db_session.add(address)
    db_session.flush()

    assert address.id is not None

    saved_address = db_session.query(Address).filter_by(id=address.id).first()

    assert saved_address is not None
    assert saved_address.city == "Lublin"
    assert saved_address.company_name == "ABC Transport"