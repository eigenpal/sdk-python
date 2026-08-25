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
from eigenpal._generated.models.api_error_envelope import ApiErrorEnvelope
from eigenpal._generated.models.create_automation_version_request_type_0 import (
    CreateAutomationVersionRequestType0,
)
from eigenpal._generated.models.create_automation_version_request_type_1 import (
    CreateAutomationVersionRequestType1,
)
from eigenpal._generated.models.restore_automation_version_request import (
    RestoreAutomationVersionRequest,
)

CreateAutomationVersionRequest = (
    CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1
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
    "ApiErrorEnvelope",
    "CreateAutomationVersionRequest",
    "CreateAutomationVersionRequestType0",
    "CreateAutomationVersionRequestType1",
    "RestoreAutomationVersionRequest",
]
