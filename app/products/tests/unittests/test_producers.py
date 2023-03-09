"""Tests for Producers"""

import pytest
from app.products.repositories import ProducerRepository
from app.tests import TestClass, TestingSessionLocal

# ----- copy:
# pytest app/products/tests/unittests/test_producers.py


class TestProducersRepository(TestClass):
    """Test Producers Repository"""

    def test_create_producer(self):
        """Create Producer"""

        with TestingSessionLocal() as db:
            producer_repository = ProducerRepository(db)
            producer = producer_repository.create("Producer", "Address", "Description")
            assert producer.name == "Producer"
            assert producer.address == "Address"
            assert producer.description == "Description"
