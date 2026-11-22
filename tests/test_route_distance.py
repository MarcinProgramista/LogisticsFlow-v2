from datetime import timedelta
from decimal import Decimal

import pytest
from sqlalchemy.exc import IntegrityError

from app.models.address import Address
from app.models.route_distance import RouteDistance

def test_create_route_distance(db_session):

    address_a = Address(
        company_name="ABC Transport",
        address_type="WAREHOUSE",
        street="Przemysłowa",
        building_number="10",
        postal_code="20-001",
        city="Lublin",
        country="Poland"
    )

    address_b = Address(
        company_name="XYZ Logistics",
        address_type="WAREHOUSE",
        street="Magazynowa",
        building_number="5",
        postal_code="22-400",
        city="Zamość",
        country="Poland"
    )

    db_session.add_all([address_a, address_b])
    db_session.flush()
    route_distance = RouteDistance(
        address_a_id=address_a.id,
        address_b_id=address_b.id,
        kms=Decimal("175.00"),
        duration_60=timedelta(hours=2, minutes=55),
        duration_80=timedelta(hours=2, minutes=11, seconds=15)
    )

    db_session.add(route_distance)
    db_session.flush()

    assert route_distance.id is not None
    assert route_distance.address_a_id == address_a.id
    assert route_distance.address_b_id == address_b.id
    assert route_distance.kms == Decimal("175.00")
    assert route_distance.duration_60 == timedelta(hours=2, minutes=55)
    assert route_distance.duration_80 == timedelta(hours=2, minutes=11, seconds=15)

def test_route_distance_must_be_unique(db_session):
    address_a = Address(
        company_name="ABC Transport",
        address_type="WAREHOUSE",
        street="Przemysłowa",
        building_number="10",
        postal_code="20-001",
        city="Lublin",
        country="Poland"
    )

    address_b = Address(
        company_name="XYZ Logistics",
        address_type="WAREHOUSE",
        street="Magazynowa",
        building_number="5",
        postal_code="22-400",
        city="Zamość",
        country="Poland"
    )
    db_session.add_all([address_a, address_b])
    db_session.flush()

    first_route = RouteDistance(
        address_a_id=address_a.id,
        address_b_id=address_b.id,
        kms=Decimal("175.00"),
        duration_60=timedelta(hours=2, minutes=55),
        duration_80=timedelta(hours=2, minutes=11, seconds=15)
    )

    db_session.add(first_route)
    db_session.flush()

    second_route = RouteDistance(
    address_a_id=address_a.id,
    address_b_id=address_b.id,
    kms=Decimal("180.00"),
    duration_60=timedelta(hours=3),
    duration_80=timedelta(hours=2, minutes=15)
)

    db_session.add(second_route)

    with pytest.raises(IntegrityError):
        db_session.flush()

def test_route_distance_addresses_must_be_different(db_session):
    address = Address(
        company_name="ABC Transport",
        address_type="WAREHOUSE",
        street="Przemysłowa",
        building_number="10",
        postal_code="20-001",
        city="Lublin",
        country="Poland"
    )

    db_session.add(address)
    db_session.flush()

    route_distance = RouteDistance(
        address_a_id=address.id,
        address_b_id=address.id,
        kms=Decimal("0.00"),
        duration_60=timedelta(0),
        duration_80=timedelta(0)
    )
    db_session.add(route_distance)

    with pytest.raises(IntegrityError):
        db_session.flush()
