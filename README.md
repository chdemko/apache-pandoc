Installation
============

 * Install [`pandoc`](http://johnmacfarlane.net/pandoc/) on your system
 * Make sure `python` is installed
 * Copy the `pandoc.conf` file to the `conf.d` folder of your `apache` server
 * Create a `/usr/share/apache-pandoc` folder
 * Copy the `pandoc.py` file to the `/usr/share/apache-pandoc` folder
 * Restart your `apache` server

Usage
=====

 * Copy this file to a folder accessible by `apache` (i.e. `/home/user/public_html`)
 * Access `http://localhost/~user/README.md` with a browser (you will see the `html` version of this file)
 * Access `http://localhost/~user/README.md?pdf` with a browser (you will see the `pdf` version of this file)
 * Access `http://localhost/~user/README.md?odt` with a browser (you will see the `odt` version of this file)
 * Access `http://localhost/~user/README.md?raw` with a browser (you will see the `raw` version of this file)

Advanced usage
==============
Create a `/home/user/public_html/.pandoc.ini` file containing

    [Pandoc]
    toc=true

And access to `http://localhost/~user/README.md` with a browser (you will see the `html` version of this file with a table of contents). A lot of configuration options can be inserted in the `.pandoc.ini` files. See `pandoc.py` for more details.

License
=======
`apache-pandoc` is released under the [CeCILL-B license](http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html)
 
 
Authors
=======
 * Christophe Demko
