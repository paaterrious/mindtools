from mindtools import retry


def test_retry_eventually_succeeds():
    state = {"calls": 0}

    @retry(attempts=3)
    def unstable():
        state["calls"] += 1
        if state["calls"] < 3:
            raise ValueError("temporary failure")
        return "success"

    assert unstable() == "success"
    assert state["calls"] == 3
