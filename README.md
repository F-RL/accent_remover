# Remove Accents

Finding no online alternative, I devised this abomination.
It consists of one (1) function that takes any string and replaces characters with accents (like "é") with their unmodified version (in that case, "e").

Currently this works for latin script.

### Usage

```python
>>> from accent_remover import remove_accents
>>> s = "My name is André and my name breaks URLs"
>>> new_s = remove_accents(s)
>>> print(new_s)
"My name is Andre and my name breaks URLs"
```

Thank you for your attention.
