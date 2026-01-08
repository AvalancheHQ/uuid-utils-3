"""Performance benchmarks for uuid-utils using pytest-codspeed."""

import uuid

import pytest
import uuid_utils

node = uuid.getnode()


@pytest.mark.benchmark
def test_uuid1_performance():
    """Benchmark UUID v1 generation performance."""
    for _ in range(10_000):
        uuid_utils.uuid1(node)


@pytest.mark.benchmark
def test_uuid3_performance():
    """Benchmark UUID v3 generation performance."""
    for _ in range(10_000):
        uuid_utils.uuid3(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid4_performance():
    """Benchmark UUID v4 generation performance."""
    for _ in range(10_000):
        uuid_utils.uuid4()


@pytest.mark.benchmark
def test_uuid5_performance():
    """Benchmark UUID v5 generation performance."""
    for _ in range(10_000):
        uuid_utils.uuid5(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid6_performance():
    """Benchmark UUID v6 generation performance."""
    for _ in range(10_000):
        uuid_utils.uuid6()


@pytest.mark.benchmark
def test_uuid7_performance():
    """Benchmark UUID v7 generation performance."""
    for _ in range(10_000):
        uuid_utils.uuid7()


@pytest.mark.benchmark
def test_uuid_from_hex_performance():
    """Benchmark UUID parsing from hex string."""
    for _ in range(10_000):
        uuid_utils.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_uuid_from_bytes_performance():
    """Benchmark UUID creation from bytes."""
    uuid_bytes = bytes.fromhex("a8098c1af86e11dabd1a00112444be1e")
    for _ in range(10_000):
        uuid_utils.UUID(bytes=uuid_bytes)


@pytest.mark.benchmark
def test_uuid_from_int_performance():
    """Benchmark UUID creation from integer."""
    uuid_int = 223357227817209978315032941467229913630
    for _ in range(10_000):
        uuid_utils.UUID(int=uuid_int)


@pytest.mark.benchmark
def test_uuid_from_fields_performance():
    """Benchmark UUID creation from fields."""
    for _ in range(10_000):
        uuid_utils.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))
