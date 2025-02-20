from collections.abc import Mapping, Sequence
from typing import Any

from django.http.request import HttpRequest
from django.template.exceptions import TemplateDoesNotExist as TemplateDoesNotExist  # noqa: F401
from django.utils.safestring import SafeString

from . import engines as engines  # noqa: F401
from .backends.base import _EngineTemplate

def get_template(template_name: str, using: str | None = ...) -> _EngineTemplate: ...
def select_template(template_name_list: Sequence[str] | str, using: str | None = ...) -> Any: ...
def render_to_string(
    template_name: Sequence[str] | str,
    context: dict[str, Any] | None = ...,
    request: HttpRequest | None = ...,
    using: str | None = ...,
) -> SafeString: ...
