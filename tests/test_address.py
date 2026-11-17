from app.models.address import Address


def test_create_address():
    address = Address(
        company_name="ABC Transport",
        address_type="OFFICE",
        street="Lipowa",
        building_number="10",
        postal_code="20-001",
        city="Lublin",
        country="Poland"
    )

    assert address.company_name == "ABC Transport"
    assert address.address_type == "OFFICE"
    assert address.city == "Lublin"

def test_address_optional_fields():
    address = Address(
        company_name="ABC Transport",
        address_type="WAREHOUSE",
        street="Przemysłowa",
        building_number="5",
        postal_code="22-400",
        city="Zamość",
        country="Poland"
    )

    assert address.apartment_number is None
    assert address.notes is None
