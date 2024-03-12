# ipymario

A simple [anywidget](http://github.com/manzt/anywidget), built from Mike
Bostock's [Mario chime
snippet](https://twitter.com/mbostock/status/1765222176641437859).

See [video tutorial](https://www.youtube.com/watch?v=oZhyilx3gqI).

## Installation

```sh
pip install ipymario
```

## Usage


`In[1]:`

```py
import ipymario

ipymario.Widget()
```

`Out[1]:`

![clicking a mario brick in a jupyter output](https://github.com/manzt/ipymario/assets/24403730/e8befac9-3ce5-4ffc-a9df-3b18479c809a)

## Development

Create a virtual environment and and install `ipymario` in *editable* mode with
the optional development dependencies:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

All is set to open `demo.ipynb` in JupyterLab, VS Code, or your favorite editor
to start developing. Any change made in the `js` folder will be directly
reflected in the notebook.
