25. **Dict Comprehension**
```python
pairs = {(i, i * 2) for i in range(10)}
print(dict(sorted(pairs)))
```