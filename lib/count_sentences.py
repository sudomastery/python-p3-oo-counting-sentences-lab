#!/usr/bin/env python3

class MyString:
  def __init__(self, value: str = ""):
    # default to empty string
    self._value = ""
    # use setter to validate initial value
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")

  # sentence type checks
  def is_sentence(self) -> bool:
    return self.value.endswith(".")

  def is_question(self) -> bool:
    return self.value.endswith("?")

  def is_exclamation(self) -> bool:
    return self.value.endswith("!")

  def count_sentences(self) -> int:
    
    import re

    text = self.value.strip()
    if not text:
      return 0

    # Split on one-or-more of . ! ? and filter out empty/whitespace parts
    parts = re.split(r"[.!?]+", text)
    return sum(1 for p in parts if p.strip())
