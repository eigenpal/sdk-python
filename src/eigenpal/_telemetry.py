"""SDK telemetry headers attached to every outbound request.

The server reads these to track adoption — which language, which
version, which runtime are calling? Lets us answer "should we still
support Python 3.10?" or "is the 0.4 series still in use?" from log
aggregation alone, without having to ship a separate phone-home.

Header convention follows the Stainless / Anthropic SDK pattern:
    X-Eigenpal-Sdk          — language tag ("python")
    X-Eigenpal-Sdk-Version  — package version (rewritten at publish)
    X-Eigenpal-Sdk-Runtime  — "python-3.12.0" / "pypy-7.3.X"
    X-Eigenpal-Sdk-Os       — "darwin-arm64" / "linux-x86_64"

``User-Agent`` carries the same info in a single human-readable
string for log lines and proxies that don't surface custom headers.
"""

from __future__ import annotations

import platform
import sys

SDK_LANGUAGE = "python"
# Rewritten at publish time by scripts/render-sdk-versions.sh.
# Keep this string literal exactly stable — sed matches on it.
SDK_VERSION = "0.5.6"


def _detect_runtime() -> str:
    impl = platform.python_implementation().lower()  # "cpython", "pypy", ...
    name = "python" if impl == "cpython" else impl
    v = sys.version_info
    return f"{name}-{v.major}.{v.minor}.{v.micro}"


def _detect_os() -> str:
    system = platform.system().lower() or "unknown"
    machine = platform.machine().lower() or "unknown"
    return f"{system}-{machine}"


def build_telemetry_headers() -> dict[str, str]:
    runtime = _detect_runtime()
    os_name = _detect_os()
    return {
        "X-Eigenpal-Sdk": SDK_LANGUAGE,
        "X-Eigenpal-Sdk-Version": SDK_VERSION,
        "X-Eigenpal-Sdk-Runtime": runtime,
        "X-Eigenpal-Sdk-Os": os_name,
        "User-Agent": f"eigenpal-sdk-python/{SDK_VERSION} ({runtime}; {os_name})",
    }
