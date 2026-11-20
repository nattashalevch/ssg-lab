
import os
import subprocess
import hashlib
from datetime import datetime, timezone
from pathlib import Path

commit = os.getenv("GITHUB_SHA")

if not commit:
    commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True
    ).strip()

data_file = Path("data/measurements.csv")
data_hash = hashlib.sha256(data_file.read_bytes()).hexdigest()

content = f"""## Информация о сборке

- Git commit: `{commit[:12]}`
- Дата сборки: `{datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")}`
- Версия набора данных (SHA-256): `{data_hash[:12]}`
"""

Path("docs/build-info.md").write_text(content, encoding="utf-8")
print("Метка версии создана: docs/build-info.md")
