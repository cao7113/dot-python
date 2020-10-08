## Python Modules

https://docs.python.org/3/tutorial/modules.html

```
# import all names, better just in scripts
from fibo import *
from fibo import fib, fib2

# mod alias
import fibo as fib

# import func with alias
from fibo import fib as fibonacci

# import after module changed
import importlib; importlib.reload(modulename)

# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings
import os; dir(os)
import builtins; dir(builtins)
```

## Search Paths

`PYTHONPATH`
