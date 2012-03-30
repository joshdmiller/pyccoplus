```
 .oPYo.                              .oPYo. 8               
 8    8                              8    8 8               
o8YooP' o    o .oPYo. .oPYo. .oPYo. o8YooP' 8 o    o .oPYo. 
 8      8    8 8    ' 8    ' 8    8  8      8 8    8 Yb..   
 8      8    8 8    . 8    . 8    8  8      8 8    8   'Yb. 
 8      `YooP8 `YooP' `YooP' `YooP'  8      8 `YooP' `YooP' 
:..::::::....8 :.....::.....::.....::..:::::..:.....::.....:
::::::::::ooP'.:::::::::::::::::::::::::::::::::::::::::::::
::::::::::...:::::::::::::::::::::::::::::::::::::::::::::::
```

[Pycco Plus][pp] is a fork of [Pycco][pycco], a Python port of Docco: the original
quick-and-dirty, hundred-line- long, literate-programming-style documentation
generator. This fork was created out a specific need to incorporate
non-standard [Pygments][pyg] lexers without forcing the user to install custom
versions of Pygments. Specifically, Pycco Plus was created for my
[dotfiles][df] project.

As of the end of March 2012, Pycco Plus requires the development branch of
[Pystache][pys] rather than 0.4.0 or 0.4.1. Unfortunately, this means you must
clone the repo and build it manually. Once 0.5.0 is released, the standard
installation through pip will be sufficient.

[pp]: http://www.github.com/joshdmiller/pyccoplus
[pyg]: http://www.pygments.org
[df]: http://dotfiles.joshdmiller.com
[pys]: https://github.com/defunkt/pystache
[pycco]: http://www.github.com/fitzgen/pycco

Others:

Pycco (on which this is based) - http://fitzgen.github.com/pycco/

CoffeeScript (Original) - http://jashkenas.github.com/docco/

Ruby - http://rtomayko.github.com/rocco/

Sh - http://rtomayko.github.com/shocco/
