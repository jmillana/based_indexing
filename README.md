# Ordinal Based Indexing
After the legend itself [TJ DeVries](https://github.com/tjdevries) ended with the 0 vs 1 based indexing war with the most elegant solution: [Solution 1.](https://twitter.com/teej_dv/status/1757852497928921290)

I'm glad to announce that the first ever implementation of Ordinal indexing is out!!!
The most **elegant** yet **blazingly** slow, list indexing system. **100%** not written in the infamous language of the **Crab**


# Best indexing ever
With based_indexing your lists access will move from a sad a boring `my_lame_list[131]` (acctually 132) to `my_amazing_list["one hundred and thirty-first"]`

## Usage Examples

### Your new favorite list
``` python
from based_indexing import list # Yes we are overwriting python's default and useless list

l = list(1, 2, 3)
print(list["first"])
print(list["middle"])
print(list["last"])

print(l["first":"last":"second")
```
```console
1
2
3
[1, 3]
```

What about 0/zeroth? 
Fear not, I've got you covered.
```python
from based_indexing import list

l = list(1, 2, 3)
print(list["zeroth"])
```
```console
ValueError: Zeroth 🖕!
```

### Range
Yes! not only the `list` has been re-implemented, also `range`!
``` python
from based_indexing import list # Aha, we don't like defaults

for i in range("fifth"):
  print(i)
print()
for i in range("two billion and first", "two billion and seventh", "third"):
    print(i)
```
```console
'first'
'second'
'third'
'fourth'
'fifth'

'two billion and first'
'two billion and fourth'
'two billion and seventh'

```
