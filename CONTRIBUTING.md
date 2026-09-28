# Quy tắc đẩy code (đọc trước khi commit)

File này để cả nhóm làm việc trên cùng repo mà không dẫm chân nhau. Ai cũng đọc 1 lần.

## 1. Nhánh

- `main`: luôn phải chạy được (test xanh). Không push thẳng vào `main`.
- Mỗi người làm trên nhánh riêng theo mẫu: `<vai>/<việc>`
  - ví dụ: `p3/hybrid-retrieval`, `p5/eval-metrics`, `p1/qdrant-repo`
- Xong việc → mở Pull Request vào `main`, để P1 review rồi merge.

## 2. Commit

- Commit nhỏ, thường xuyên. Một commit = một thay đổi có nghĩa, đừng dồn 1 cục to.
- Message theo kiểu Conventional Commits (tiếng Việt cũng được):
  ```
  <type>: <mô tả ngắn>

  <giải thích thêm nếu cần>
  ```
- `type` hay dùng: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`.
- Ví dụ:
  - `feat: them hybrid retriever (BM25 + vector)`
  - `test: bo sung test cho repository factory`
  - `fix: sua loi doc config khi thieu key`

> Lưu ý: KHÔNG để công cụ AI làm committer/author. Author luôn là thành viên thật của nhóm.
> Giảng viên sẽ xem lịch sử commit để biết ai làm gì, nên commit đúng tên mình.

## 3. Trước khi push

Chạy đủ 3 bước, đỏ chỗ nào sửa chỗ đó rồi mới push:

```bash
make format   # ruff format
make lint     # ruff check
make test     # pytest
```

Hoặc chạy tay:

```bash
ruff format . && ruff check . && python -m pytest -q
```

## 4. Ranh giới module (ai đụng file nào)

| Vai | File được sửa | Không đụng |
|-----|---------------|------------|
| P1 | `src/repository/`, `src/config.py`, `src/models.py`, CI, docs kiến trúc | logic ML của người khác |
| P2 | `data/`, script ingest | interface trong `repository/` |
| P3 | `src/embedding.py`, `src/retriever.py` | `detector.py` |
| P4 | `src/llm_client.py`, `src/detector.py` | `retriever.py` |
| P5 | `src/evaluation.py`, `notebooks/` | các module lõi |

Interface (các class trừu tượng) do P1 chốt. Nếu cần đổi interface → báo P1, đừng tự sửa
vì sẽ vỡ code người khác.

## 5. Review PR

- PR nên nhỏ (< ~300 dòng), dễ đọc.
- Mô tả PR ghi rõ: làm gì, test ra sao, còn thiếu gì.
- P1 (hoặc người được chỉ định) đọc + chạy test local rồi mới merge.

## 6. Không commit rác

Không đẩy lên repo: `__pycache__/`, `.venv/`, dữ liệu nặng, file model tải về,
`data/kb/` (index sinh ra). Đã có trong `.gitignore`.
