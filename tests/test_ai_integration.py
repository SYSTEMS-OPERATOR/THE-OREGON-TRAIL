import os
import pytest

@pytest.mark.skipif(os.environ.get("AI_INTEGRATION") != "true", reason="AI mode only")
def test_ai_mode_placeholder():
    assert True
