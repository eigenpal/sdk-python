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
from eigenpal._generated.models.create_email_server_request_type_0 import (
    CreateEmailServerRequestType0,
)
from eigenpal._generated.models.create_email_server_request_type_1 import (
    CreateEmailServerRequestType1,
)
from eigenpal._generated.models.delete_email_server_response import (
    DeleteEmailServerResponse,
)
from eigenpal._generated.models.list_email_servers_response import (
    ListEmailServersResponse,
)
from eigenpal._generated.models.public_resend_email_server import PublicResendEmailServer
from eigenpal._generated.models.public_smtp_email_server import PublicSmtpEmailServer
from eigenpal._generated.models.restore_automation_version_request import (
    RestoreAutomationVersionRequest,
)
from eigenpal._generated.models.test_email_server_request import TestEmailServerRequest
from eigenpal._generated.models.test_email_server_response_type_0 import (
    TestEmailServerResponseType0,
)
from eigenpal._generated.models.test_email_server_response_type_1 import (
    TestEmailServerResponseType1,
)
from eigenpal._generated.models.update_email_server_request_type_0 import (
    UpdateEmailServerRequestType0,
)
from eigenpal._generated.models.update_email_server_request_type_1 import (
    UpdateEmailServerRequestType1,
)
from eigenpal._generated.models.update_email_server_request_type_2 import (
    UpdateEmailServerRequestType2,
)

CreateAutomationVersionRequest = (
    CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1
)
CreateEmailServerRequest = CreateEmailServerRequestType0 | CreateEmailServerRequestType1
EmailServer = PublicResendEmailServer | PublicSmtpEmailServer
TestEmailServerResponse = TestEmailServerResponseType0 | TestEmailServerResponseType1
UpdateEmailServerRequest = (
    UpdateEmailServerRequestType0
    | UpdateEmailServerRequestType1
    | UpdateEmailServerRequestType2
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
    "CreateEmailServerRequest",
    "CreateEmailServerRequestType0",
    "CreateEmailServerRequestType1",
    "DeleteEmailServerResponse",
    "EmailServer",
    "ListEmailServersResponse",
    "PublicResendEmailServer",
    "PublicSmtpEmailServer",
    "RestoreAutomationVersionRequest",
    "TestEmailServerRequest",
    "TestEmailServerResponse",
    "TestEmailServerResponseType0",
    "TestEmailServerResponseType1",
    "UpdateEmailServerRequest",
    "UpdateEmailServerRequestType0",
    "UpdateEmailServerRequestType1",
    "UpdateEmailServerRequestType2",
]
