"""Official Python SDK for the EigenPal API.

Example
-------

    from eigenpal import EigenpalClient

    client = EigenpalClient(api_key=os.environ["EIGENPAL_API_KEY"])

    # Async — enqueue and poll later.
    result = client.run("workflows.extract-invoice", input={"contract": {"fileId": "f_x"}})

    # Sync — server holds the connection up to 60s.
    result = client.run(
        "workflows.extract-invoice", input={...}, wait_for_completion=60,
    )

    # Client-side poll (up to 5min by default).
    result = client.run_and_wait("workflows.extract-invoice", input={...})
"""

from eigenpal.client import EigenpalClient
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
    "EigenpalClient",
    "EigenpalError",
    "EigenpalAuthError",
    "EigenpalForbiddenError",
    "EigenpalNotFoundError",
    "EigenpalRateLimitError",
    "EigenpalServerError",
    "EigenpalTimeoutError",
    "EigenpalValidationError",
]
