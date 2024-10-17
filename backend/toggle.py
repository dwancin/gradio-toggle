# Toggle - A Gradio Custom Component
# Created by Daniel Ialcin Misser Westergaard
# https://huggingface.co/dwancin
# https://github.com/dwancin
# (c) 2024

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, Literal

from gradio_client.documentation import document

from gradio.components.base import Component, FormComponent
from gradio.events import Events

if TYPE_CHECKING:
    from gradio.components import Timer


class Toggle(FormComponent):
    """
    Creates a checkbox that can be set to `True` or `False`. Can be used as an input to pass a boolean value to a function or as an output
    to display a boolean value.

    Demos: sentence_builder, hello_world_3
    """

    EVENTS = [Events.change, Events.input, Events.select]

    def __init__(
        self,
        value: bool | Callable = False,
        *,
        label: str | None = None,
        info: str | None = None,
        color: str | Callable | None = None,
        radius: Literal["sm", "lg"] = "lg",
        transition: float = 0.3,
        every: Timer | float | None = None,
        inputs: Component | Sequence[Component] | set[Component] | None = None,
        show_label: bool | None = None,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        interactive: bool | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        key: int | str | None = None,
    ):
        """
        Parameters:
            value: 
                Initial state of the toggle. If callable, it sets the initial state dynamically when the app loads.
            label: 
                Text label displayed adjacent to the toggle. If None and used within a `gr.Interface`, it defaults to the parameter name.
            info: 
                Text displayed below the toggle for additional guidance or information.
            color: 
                Optional color setting for the toggle, supporting CSS color values (e.g., names, hex codes).
            radius:
                Size of the border radius used for the toggle style.
            transition:
                Transition time (in seconds) between on and off state.
            show_label: 
                If True, the label is displayed; otherwise, it is hidden.
            interactive: 
                If True, the toggle can be interacted with; if False, it is disabled. Default behavior is auto-detected based on usage.
            visible: 
                If False, the toggle is not rendered visibly in the interface.
            container: 
                If True, the toggle is placed within a styled container for visual grouping and padding.
            scale: 
                Relative sizing of the toggle in comparison to adjacent components when displayed in a row or block.
            min_width: 
                Minimum width in pixels that the toggle will occupy, ensuring it does not shrink below this size.
            elem_id: 
                Optional identifier for the HTML element; useful for CSS customizations.
            elem_classes: 
                Optional list of class names for the HTML element; useful for CSS customizations.
            every: 
                If value is callable, specifies how frequently (in seconds) to refresh the value while the interface is open.
            render: 
                If False, the component is not rendered immediately, useful for deferred rendering or conditional UI updates.
            key: 
                If assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.
        """
        super().__init__(
            label=label,
            info=info,
            every=every,
            inputs=inputs,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            key=key,
            value=value
        )
        self.color = color
        self.radius = radius
        self.transition = transition

    def api_info(self) -> dict[str, Any]:
        return {"type": "boolean"}

    def example_payload(self) -> bool:
        return True

    def example_value(self) -> bool:
        return True

    def preprocess(self, payload: bool | None) -> bool | None:
        """
        Parameters:
            payload: The received toggle state from the user.
        Returns:
            The toggle state as a boolean value.
        """
        return payload

    def postprocess(self, value: bool | None) -> bool | None:
        """
        Parameters:
            value: The toggle state to be returned.
        Returns:
            The state as a boolean, ensuring type consistency.
        """
        return bool(value)
