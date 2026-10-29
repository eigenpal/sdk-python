"""Exercise every generated module on each supported test interpreter."""

import importlib
import pkgutil

import eigenpal._generated as generated


def test_all_generated_modules_import():
    # Catches generator upgrades introducing Python 3.11-only runtime imports.
    modules = list(pkgutil.walk_packages(generated.__path__, generated.__name__ + "."))
    assert modules
    for module in modules:
        importlib.import_module(module.name)


def test_public_run_error_preserves_business_code():
    from eigenpal import RunError

    payload = {
        "code": "workflow_rejected", "statusCode": 422,
        "message": "Wrong document", "step": "assert_contract", "retryable": False,
    }
    failure = RunError.from_dict(payload)
    assert failure.status_code == 422
    assert failure.to_dict() == payload
