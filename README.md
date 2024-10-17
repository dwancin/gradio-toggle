# `gradio_toggle`
<div style="display: flex; gap: 7px;">
  <a href="https://pypi.org/project/gradio-toggle/" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/gradio-toggle"></a>
  <a href="https://huggingface.co/spaces/dwancin/gradio_toggle" target="_blank"><img alt="Demo" src="https://img.shields.io/badge/%F0%9F%A4%97%20Demo-%23097EFF?style=flat&logoColor=black"></a>
  <a href="https://github.com/dwancin/gradio-toggle" target="_blank"><img alt="Static Badge" src="https://img.shields.io/badge/Repository-white?logo=github&logoColor=black"></a>
</div>

A toggle component that represents a boolean value, allowing users to switch between True and False states. Can function both as an input, to capture user interaction, and as an output, to display a boolean state.

![screenshot](https://raw.githubusercontent.com/dwancin/gradio-toggle/main/assets/preview.gif)

## Installation

```bash
pip install gradio_toggle
```

## Usage

```python
import gradio as gr
from gradio_toggle import Toggle

def update(input):
    output = input
    return output

with gr.Blocks() as demo:
    title = gr.HTML("<h1><center>gradio-toggle demo</center></h1>")
    with gr.Row():
        with gr.Column():
            input = Toggle(
                label="Input",
                value=False,
                info="Input version of the component",
                interactive=True,
            )
        with gr.Column():
            output = Toggle(
                label="Output",
                value=False,
                color="green",
                interactive=False,
            )
        
    input.change(fn=update, inputs=input, outputs=output)
        
if __name__ == "__main__":
    demo.launch()
```

## `Toggle`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
bool | Callable
```

</td>
<td align="left"><code>False</code></td>
<td align="left">Initial state of the toggle. If callable, it sets the initial state dynamically when the app loads.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

str | None

</td>
<td align="left"><code>None</code></td>
<td align="left">Text label displayed adjacent to the toggle. If None and used within a `gr.Interface`, it defaults to the parameter name.</td>
</tr>

<tr>
<td align="left"><code>info</code></td>
<td align="left" style="width: 25%;">

str | None

</td>
<td align="left"><code>None</code></td>
<td align="left">Text displayed below the toggle for additional guidance or information.</td>
</tr>

<tr>
<td align="left"><code>color</code></td>
<td align="left" style="width: 25%;">

str | None

</td>
<td align="left"><code>None</code></td>
<td align="left">Optional color setting for the toggle, supporting CSS color values (e.g., names, hex codes).</td>
</tr>

<tr>
<td align="left"><code>radius</code></td>
<td align="left" style="width: 25%;">

Literal["sm", "lg"]

</td>
<td align="left"><code>"lg"</code></td>
<td align="left">Size of the border radius used for the toggle style.</td>
</tr>

<tr>
<td align="left"><code>transition</code></td>
<td align="left" style="width: 25%;">

float

</td>
<td align="left"><code>0.3</code></td>
<td align="left">Transition time (in seconds) between the on and off state.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

bool | None

</td>
<td align="left"><code>None</code></td>
<td align="left">If True, the label is displayed; otherwise, it is hidden.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

bool

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, the toggle is placed within a styled container for visual grouping and padding.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

int | None

</td>
<td align="left"><code>None</code></td>
<td align="left">Relative sizing of the toggle in comparison to adjacent components when displayed in a row or block.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

int

</td>
<td align="left"><code>160</code></td>
<td align="left">Minimum width in pixels that the toggle will occupy, ensuring it does not shrink below this size.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

bool | None

</td>
<td align="left"><code>None</code></td>
<td align="left">If True, the toggle can be interacted with; if False, it is disabled. Default behavior is auto-detected based on usage.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

bool

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, the toggle is not rendered visibly in the interface.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

str | None

</td>
<td align="left"><code>None</code></td>
<td align="left">Optional identifier for the HTML element; useful for CSS customizations.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

list[str] | str | None

</td>
<td align="left"><code>None</code></td>
<td align="left">Optional list of class names for the HTML element; useful for CSS customizations.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

float | None

</td>
<td align="left"><code>None</code></td>
<td align="left">If value is callable, specifies how frequently (in seconds) to refresh the value while the interface is open.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

bool

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, the component is not rendered immediately, useful for deferred rendering or conditional UI updates.</td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

int | str | None

</td>
<td align="left"><code>None</code></td>
<td align="left">If assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.</td>
</tr>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the toggle changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `input` | This listener is triggered when the user changes the value of the toggle. |
| `select` | Event listener for when the user selects or deselects the toggle. Uses event data gradio.SelectData to carry `value` referring to the label of the toggle, and `selected` to refer to state of the toggle. See EventData documentation on how to use this event data |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, the toggle state as a boolean value.
- **As input:** Should return, the toggle state to be returned.

 ```python
 def predict(
     value: bool | None
 ) -> bool | None:
     return value
 ```
 
