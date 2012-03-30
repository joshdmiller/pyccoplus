from setuptools import setup, find_packages

setup(
        name = "Pycco Plus",
        version = "0.1.0",
        description = """A modified version of Pycco, the Python port of Docco: the original quick-and-dirty,
        hundred-line-long, literate-programming-style documentation generator.
        """,
        author = "Josh D Miller",
        author_email = "josh@joshdmiller.com.com",
        url = "http://www.github.com/joshdmiller/pycco-plus",
        packages = find_packages(),
        entry_points = {
            'console_scripts': [
                'pyccoplus = pyccoplus.main:main',
                ]
            },
        install_requires = ['markdown', 'pygments', 'pystache', 'smartypants'],
        extras_require = {'monitoring': 'watchdog'},
        )
