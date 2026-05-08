"""Official Python SDK for the Eigenpal API.

Example
-------

    from eigenpal import Eigenpal

    client = Eigenpal(api_key=os.environ["EIGENPAL_API_KEY"])

    # Async — enqueue and poll later.
    result = client.workflows.run("wf_abc", input={"contract": {"file_id": "f_x"}})

    # Sync — server holds the connection up to 60s.
    result = client.workflows.run(
        "wf_abc", input={...}, wait_for_completion=60,
    )

    # Client-side poll (up to 5min by default).
    result = client.executions.run_and_wait("wf_abc", input={...})
"""

from eigenpal.client import Eigenpal
from eigenpal.errors import (
    EigenpalAuthError,
    EigenpalError,
    EigenpalForbiddenError,
    EigenpalNotFoundError,
    EigenpalRateLimitError,
    EigenpalServerError,
    EigenpalTimeoutError,
    EigenpalValidationError,
)

__all__ = [
    "Eigenpal",
    "EigenpalError",
    "EigenpalAuthError",
    "EigenpalForbiddenError",
    "EigenpalNotFoundError",
    "EigenpalRateLimitError",
    "EigenpalServerError",
    "EigenpalTimeoutError",
    "EigenpalValidationError",
]
