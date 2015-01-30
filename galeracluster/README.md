Documentation
=============

To compile the RST docs on Ubuntu one needs:

    $ sudo apt-get install python-sphinx texlive-latex-base texlive-latex-extra dvipng
    $ sudo pip install cloud-sptheme

(On other distributions it must be something similar.)

Then:

    $ make dirhtml
