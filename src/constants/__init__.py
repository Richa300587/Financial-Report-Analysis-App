import os
from datetime import date 

# =========================
# Chunking Constants
# =========================
TEXT_CHUNK_LIMIT = 800        # normal narrative text
TABLE_CHUNK_LIMIT = 1400     # relaxed limit when table exists
ABSOLUTE_MAX_LIMIT = 1600    # embedding model safety cap
TEXT_CHUNK_OVERLAP = 100          # tokens of overlap between chunks
TABLE_CHUNK_OVERLAP = 0

