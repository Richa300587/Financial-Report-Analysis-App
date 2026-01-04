from .base import RAGException


# =========================
# Ingestion & Chunking
# =========================

class IngestionError(RAGException):
    """
    Base class for ingestion-time failures.
    These indicate document quality or structural issues.
    """
    pass


class ChunkingError(IngestionError):
    """
    Raised when semantic chunking fails.
    """
    pass


class TableIntegrityError(ChunkingError):
    """
    Raised when a table violates semantic or structural rules.

    Examples:
    - table without semantic summary
    - table split across chunks
    - table starting a chunk without context
    """

    def __init__(self, message: str, **kwargs):
        super().__init__(
            message,
            stage="chunking",
            retryable=False,  # tables are deterministic, never retry
            **kwargs
        )


# =========================
# Embeddings
# =========================

class EmbeddingError(RAGException):
    """
    Raised when embedding generation fails
    (timeouts, rate limits, transient API issues).
    """

    def __init__(self, message: str, **kwargs):
        super().__init__(
            message,
            stage="embedding",
            retryable=True,   # embeddings are usually retryable
            **kwargs
        )


# =========================
# Retrieval
# =========================

class RetrievalError(RAGException):
    """
    Raised when document retrieval fails semantically
    or confidence is too low.
    """
    pass


# =========================
# LLM Calls
# =========================

class LLMCallError(RAGException):
    """
    Raised when an LLM call fails, times out,
    or returns an invalid response.
    """

    def __init__(self, message: str, **kwargs):
        super().__init__(
            message,
            stage="llm",
            retryable=True,   # LLM calls are typically retryable
            **kwargs
        )
