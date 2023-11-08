import tomli
from dataclasses import dataclass
from typing import List

@dataclass
class Bike:
    start_stations: List[str]


class Workflow:
  _toml_source: str = './setting.toml'

  def __init__(self):
    self.reload()

  def reload(self):
      with open(self._toml_source, "rb") as f:
          self._options = tomli.load(f)
      return self

  @property
  def bikes(self):
      return Bike(**self._options["biketrips"])