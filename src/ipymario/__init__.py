import importlib.metadata
import pathlib

import anywidget
import traitlets
import numpy as np

try:
    __version__ = importlib.metadata.version("ipymario")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


colors = {
  'O': [0, 0, 0, 255],
  'X': [247, 82, 0, 255],
  ' ': [247, 186, 119, 255],
}

box = [
    ['O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['X', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O'],
    ['X', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', ' ', 'X', 'X', 'O', 'O', 'O', 'X', 'X', ' ', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', ' ', 'X', 'X', 'O', ' ', ' ', 'X', 'X', 'O', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', ' ', 'X', 'X', 'O', ' ', ' ', 'X', 'X', 'O', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', ' ', ' ', 'O', 'O', ' ', 'X', 'X', 'X', 'O', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'O', 'O', 'O', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'O', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'O', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['X', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', 'O', ' ', ' ', ' ', 'O', ' ', 'O'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
]

np_box = np.array([[colors[c] for c in row] for row in box], dtype=np.uint8)

class Widget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    _box = traitlets.Bytes(np_box.tobytes()).tag(sync=True)
    gain = traitlets.Float(0.1).tag(sync=True)
    duration = traitlets.Float(1.0).tag(sync=True)
    size = traitlets.Int(30).tag(sync=True)
    animate = traitlets.Bool(True).tag(sync=True)

    def click(self):
        self.send({ "type": "click" })
