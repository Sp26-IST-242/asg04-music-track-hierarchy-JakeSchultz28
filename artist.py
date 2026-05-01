"""
Represents a musical artist or podcast creator.

This is the simplest class in the hierarchy — no dependencies, no validation.
It introduces two core Python OOP conventions:
  1. The single leading-underscore (_name) signals a non-public attribute.
  2. @property exposes a clean public getter without allowing direct mutation.
"""

class Artist:
    
    # Constructor
    def __init__(self, name : str, genre : str):
        self._name = name
        self._genre = genre

    # Properties (getters)
    @property
    def name(self):
        # Returns name
        return self._name
    
    @property
    def genre(self):
        # Returns genre
        return self._genre
    
    def __str__(self):
        # Prints artist name and genre
        return f"{self._name}, {self._genre}"