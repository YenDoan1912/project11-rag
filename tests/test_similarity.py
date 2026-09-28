import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.models import Document  # noqa: E402
from src.repository._similarity import cosine_similarity, rank_by_similarity  # noqa: E402


def test_cosine_basic():
    assert cosine_similarity([1, 0], [1, 0]) == 1.0
    assert cosine_similarity([1, 0], [0, 1]) == 0.0


def test_cosine_edge_cases():
    # vector rong / khac chieu / vector 0 -> 0.0, khong duoc no ZeroDivisionError
    assert cosine_similarity([], [1, 2]) == 0.0
    assert cosine_similarity([1, 2, 3], [1, 2]) == 0.0
    assert cosine_similarity([0, 0], [1, 1]) == 0.0


def test_rank_orders_desc():
    docs = [
        Document("a", "", embedding=[1, 0, 0]),
        Document("b", "", embedding=[0, 1, 0]),
        Document("c", "", embedding=[0.9, 0.1, 0]),
    ]
    ranked = rank_by_similarity(docs, [1, 0, 0], top_k=2)
    assert [d.doc_id for d in ranked] == ["a", "c"]
