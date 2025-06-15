import sys
import types


def dummy_config():
    if "config" not in sys.modules:
        dummy_config = types.ModuleType("config")


        class _DummySettings:
            register_passphrase: str | None = "secret"


        dummy_config.settings = _DummySettings()
        sys.modules["config"] = dummy_config
