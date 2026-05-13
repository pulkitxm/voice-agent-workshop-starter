"""Verify your workshop setup before Thursday.

Pings every API listed in `.env` and prints a green check for each one that
works. If any check fails, fix it before the workshop — the message tells you
where to look.

Usage:
    python verify_setup.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def ok(msg: str) -> None:
    print(f"{GREEN}✓{RESET} {msg}")


def fail(msg: str) -> None:
    print(f"{RED}✗{RESET} {msg}")


def warn(msg: str) -> None:
    print(f"{YELLOW}!{RESET} {msg}")


_failures = 0


def _record_fail(msg: str) -> None:
    global _failures
    _failures += 1
    fail(msg)


# 1. Python version
def check_python() -> None:
    if sys.version_info >= (3, 10):
        ok(f"Python {sys.version_info.major}.{sys.version_info.minor}")
    else:
        _record_fail(
            f"Python {sys.version_info.major}.{sys.version_info.minor} < 3.10. "
            "Install Python 3.10+ via brew or https://python.org"
        )


# 2. Required env vars present
REQUIRED_VARS = {
    "LIVEKIT_URL": "LiveKit Cloud → Settings → Keys",
    "LIVEKIT_API_KEY": "LiveKit Cloud → Settings → Keys",
    "LIVEKIT_API_SECRET": "LiveKit Cloud → Settings → Keys",
    "GROQ_API_KEY": "https://console.groq.com",
    "SMALLEST_API_KEY": "https://console.smallest.ai/apikeys",
    "NOVEUM_API_KEY": "https://noveum.ai → Settings → API Keys",
}


_PLACEHOLDER_FRAGMENTS = ("your-project", "your_", "REPLACE", "xxx")


def _is_placeholder(value: str) -> bool:
    lowered = value.lower()
    return any(frag.lower() in lowered for frag in _PLACEHOLDER_FRAGMENTS)


def check_env_vars() -> None:
    for var, source in REQUIRED_VARS.items():
        value = (os.environ.get(var) or "").strip()
        if not value:
            _record_fail(f"{var} missing in .env — get it from {source}")
        elif _is_placeholder(value):
            _record_fail(f"{var} still has placeholder value — get a real one from {source}")
        else:
            ok(f"{var} present ({len(value)} chars)")


# 3. Live API checks
def check_groq() -> None:
    try:
        import requests
    except ImportError:
        warn("requests not installed; skipping live API checks")
        return
    key = (os.environ.get("GROQ_API_KEY") or "").strip()
    if not key:
        return
    try:
        r = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json={
                "model": "openai/gpt-oss-120b",
                "messages": [{"role": "user", "content": "say ok"}],
                "max_tokens": 5,
            },
            timeout=15,
        )
        if r.status_code == 200:
            ok("Groq API reachable + key valid")
        else:
            _record_fail(f"Groq returned HTTP {r.status_code}: {r.text[:120]}")
    except Exception as exc:
        _record_fail(f"Groq request failed: {exc}")


def check_smallestai() -> None:
    try:
        import requests
    except ImportError:
        return
    key = (
        os.environ.get("SMALLEST_API_KEY")
        or os.environ.get("SMALLEST_AI_API_KEY")
        or ""
    ).strip()
    if not key:
        return
    try:
        # Hit the voices list endpoint as a cheap auth probe.
        r = requests.get(
            "https://api.smallest.ai/waves/v1/lightning-v3.1/get_voices",
            headers={"Authorization": f"Bearer {key}"},
            timeout=15,
        )
        if r.status_code == 200:
            ok("Smallest.ai API reachable + key valid (STT + TTS)")
        elif r.status_code in (401, 403):
            _record_fail(
                "Smallest.ai API reachable but key rejected "
                f"(HTTP {r.status_code}). Re-copy from "
                "https://console.smallest.ai/apikeys."
            )
        else:
            _record_fail(f"Smallest.ai returned HTTP {r.status_code}: {r.text[:120]}")
    except Exception as exc:
        _record_fail(f"Smallest.ai request failed: {exc}")


def check_noveum() -> None:
    try:
        import requests
    except ImportError:
        return
    key = (os.environ.get("NOVEUM_API_KEY") or "").strip()
    if not key:
        return
    try:
        r = requests.get(
            "https://noveum.ai/api/v1/projects",
            headers={"Authorization": f"Bearer {key}"},
            timeout=15,
        )
        if r.status_code in (200, 401):
            # 401 means the endpoint reached us but key is wrong
            if r.status_code == 200:
                ok("Noveum API reachable + key valid")
            else:
                _record_fail(
                    "Noveum API reachable but key rejected (HTTP 401). "
                    "Re-copy from https://noveum.ai → Settings → API Keys."
                )
        else:
            _record_fail(f"Noveum returned HTTP {r.status_code}: {r.text[:120]}")
    except Exception as exc:
        _record_fail(f"Noveum request failed: {exc}")


def check_livekit_cli() -> None:
    import shutil

    if shutil.which("lk"):
        ok("LiveKit CLI (`lk`) found on PATH")
    else:
        warn(
            "LiveKit CLI not found. Optional but recommended: "
            "`brew install livekit-cli` (macOS) or see https://docs.livekit.io/realtime/cli/"
        )


def main() -> int:
    print("\n=== Voice Agent Workshop — Setup Verification ===\n")
    check_python()
    print()
    print("--- Environment variables ---")
    check_env_vars()
    print()
    print("--- Live API checks ---")
    check_groq()
    check_smallestai()
    check_noveum()
    print()
    print("--- Tooling ---")
    check_livekit_cli()
    print()

    if _failures == 0:
        print(f"{GREEN}🎉 All checks passed. You're ready for Thursday.{RESET}\n")
        return 0
    else:
        print(
            f"{RED}{_failures} check(s) failed.{RESET} "
            "Fix before Thursday or join Wednesday office hours.\n"
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
