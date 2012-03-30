d8888b. db    db  .o88b.  .o88b.  .d88b.       d8888b. db      db    db .d8888. 
88  `8D `8b  d8' d8P  Y8 d8P  Y8 .8P  Y8.      88  `8D 88      88    88 88'  YP 
88oodD'  `8bd8'  8P      8P      88    88      88oodD' 88      88    88 `8bo.   
88~~~      88    8b      8b      88    88      88~~~   88      88    88   `Y8b. 
88         88    Y8b  d8 Y8b  d8 `8b  d8'      88      88booo. 88b  d88 db   8D 
88         YP     `Y88P'  `Y88P'  `Y88P'       88      Y88888P ~Y8888P' `8888Y' 

[Pycco Plus][pp] is a fork of Pycco, a Python port of Docco: the original
quick-and-dirty, hundred-line- long, literate-programming-style documentation
generator. This fork was created out a specific need to incorporate
non-standard [Pygments][pyg] lexers without forcing the user to install custom
versions of Pygments. Specifically, Pycco Plus was created for my
[dotfiles][df] project.

As of the end of March 2012, Pycco Plus requires the development branch of
[Pystache][pys] rather than 0.4.0 or 0.4.1. Unfortunately, this means you must
clone the repo and build it manually. Once 0.5.0 is released, the standard
installation through pip will be sufficient.

[pp]: http://www.github.com/joshdmiller/pycco-plus
[pyg]: http://www.pygments.org
[df]: http://dotfiles.joshdmiller.com
[pys]: https://github.com/defunkt/pystache

Others:

Pycco (on which this is based) - http://fitzgen.github.com/pycco/

CoffeeScript (Original) - http://jashkenas.github.com/docco/

Ruby - http://rtomayko.github.com/rocco/

Sh - http://rtomayko.github.com/shocco/
