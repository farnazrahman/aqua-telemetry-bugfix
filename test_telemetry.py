from telemetry import depth_status

assert depth_status(None) == "NO DATA", f"Expected NO DATA, got {depth_status(None)}"
assert depth_status(1.9) == "LIVE", f"Expected LIVE, got {depth_status(1.9)}"
assert depth_status(2.0) == "STALE", f"Expected STALE, got {depth_status(2.0)}"
assert depth_status(3.0) == "STALE", f"Expected STALE, got {depth_status(3.0)}"

print("All depth_status checks passed!")
