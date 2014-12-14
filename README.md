Installation
============

 * Install [`pandoc`](http://johnmacfarlane.net/pandoc/) on your system
 * Make sure `python` is installed
 * Copy the `pandoc.conf` file to the `conf.available` folder of your `apache` server
 * Enable via `a2enconf pandoc.conf`  (if apache 2.2 just copy to `conf.d` instead)
 * Create a `/usr/share/apache-pandoc` folder
 * Copy the `pandoc.py` file to the `/usr/share/apache-pandoc` folder
 * Restart your `apache` server

Usage
=====

 * Copy this file to a folder accessible by `apache` (i.e. `/home/user/public_html`)
 * Access `http://localhost/~user/README.md` with a browser (you will see the `html` version of this file)
 * Access `http://localhost/~user/README.md?pdf` with a browser (you will see the `pdf` version of this file)
 * Access `http://localhost/~user/README.md?rtf` with a browser (you will see the `rtf` version of this file)
 * Access `http://localhost/~user/README.md?odt` with a browser (you will see the `odt` version of this file)
 * Access `http://localhost/~user/README.md?raw` with a browser (you will see the `raw` version of this file)
 
If you have permissions to use `mod_rewrite`, you can use this `.htaccess` file in your `/home/user/public_html` folder

~~~
RewriteEngine On
RewriteBase /~user/
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)\.(raw|pdf|odt|rtf|html)$ $1.md?$2 [NC]
RewriteRule ^(.*)\.md$ $1.markdown [NC]
~~~

 * Access `http://localhost/~user/README.html` with a browser (you will see the `html` version of this file)
 * Access `http://localhost/~user/README.pdf` with a browser (you will see the `pdf` version of this file)
 * Access `http://localhost/~user/README.rtf` with a browser (you will see the `rtf` version of this file)
 * Access `http://localhost/~user/README.odt` with a browser (you will see the `odt` version of this file)
 * Access `http://localhost/~user/README.raw` with a browser (you will see the `raw` version of this file)

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
