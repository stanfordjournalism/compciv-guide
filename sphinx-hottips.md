Linking to a relative spot: http://stackoverflow.com/questions/3630386/insert-relative-link-in-restructuredtext


Including a link from parent directory:

http://stackoverflow.com/questions/10199233/can-sphinx-link-to-documents-that-are-not-located-in-directories-below-the-root




http://www.sphinx-doc.org/en/1.5.1/markup/inline.html#role-kbd

:kbd:
Mark a sequence of keystrokes. What form the key sequence takes may depend on platform- or application-specific conventions. When there are no relevant conventions, the names of modifier keys should be spelled out, to improve accessibility for new users and non-native speakers. For example, an xemacs key sequence may be marked like :kbd:`C-x C-f`, but without reference to a specific application or platform, the same sequence should be marked as :kbd:`Control-x Control-f`.



http://www.sphinx-doc.org/en/1.5.1/rest.html#citations

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.



## Downloadable files

http://www.sphinx-doc.org/en/1.5.1/markup/inline.html#referencing-downloadable-files



----------


Force full make


      make html SPHINXOPTS='-E'
