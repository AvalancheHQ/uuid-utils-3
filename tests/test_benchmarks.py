"""CodSpeed benchmarks for uuid_utils performance testing."""
import uuid

import pytest

import uuid_utils


@pytest.mark.benchmark
def test_uuid1_benchmark():
    """Benchmark UUID v1 generation."""
    node = uuid.getnode()
    for _ in range(10_000):
        uuid_utils.uuid1(node)


@pytest.mark.benchmark
def test_uuid3_benchmark():
    """Benchmark UUID v3 generation."""
    for _ in range(10_000):
        uuid_utils.uuid3(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid4_benchmark():
    """Benchmark UUID v4 generation."""
    for _ in range(10_000):
        uuid_utils.uuid4()


@pytest.mark.benchmark
def test_uuid5_benchmark():
    """Benchmark UUID v5 generation."""
    for _ in range(10_000):
        uuid_utils.uuid5(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid6_benchmark():
    """Benchmark UUID v6 generation."""
    for _ in range(10_000):
        uuid_utils.uuid6()


@pytest.mark.benchmark
def test_uuid7_benchmark():
    """Benchmark UUID v7 generation."""
    for _ in range(10_000):
        uuid_utils.uuid7()


@pytest.mark.benchmark
def test_uuid_from_hex_benchmark():
    """Benchmark UUID creation from hex string."""
    for _ in range(10_000):
        uuid_utils.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_uuid_from_int_benchmark():
    """Benchmark UUID creation from integer."""
    for _ in range(10_000):
        uuid_utils.UUID(int=223596183840713629990004217746136222238)


@pytest.mark.benchmark
def test_uuid_from_fields_benchmark():
    """Benchmark UUID creation from fields."""
    for _ in range(10_000):
        uuid_utils.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))
