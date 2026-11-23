from app.models.company import Company

import pytest
from sqlalchemy.exc import IntegrityError


def test_create_company_in_database(db_session):    

    company = Company(
        name="ABC Transport",
    )

    db_session.add(company)
    db_session.flush()

    assert company.id is not None

def test_create_company_without_name(db_session):
    company = Company()
    db_session.add(company)
    with pytest.raises(IntegrityError):
        db_session.flush()
    