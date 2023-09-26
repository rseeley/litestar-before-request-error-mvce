"""Minimal Litestar application."""
from __future__ import annotations

from asyncio import sleep
from typing import Any, Dict

from litestar import Litestar, Request, get

__all__ = ("async_hello_world", "sync_hello_world")


@get("/async")
async def async_hello_world() -> Dict[str, Any]:  # noqa: UP006
    """Route Handler that outputs hello world."""
    await sleep(0.1)
    return {"hello": "world"}


@get("/sync", sync_to_thread=False)
def sync_hello_world() -> Dict[str, Any]:  # noqa: UP006
    """Route Handler that outputs hello world."""
    return {"hello": "world"}


def before_request_handler_works(request: Request) -> None:
    """Before Request Handler."""
    print("Before Request Handler")


def before_request_handler_doesnt_work(request: Request) -> Any:
    """Before Request Handler."""
    print("Before Request Handler")


app = Litestar(
    route_handlers=[sync_hello_world, async_hello_world],
    before_request=before_request_handler_doesnt_work,
)
