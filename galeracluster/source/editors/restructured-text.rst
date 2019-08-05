.. meta::
   :title: Sphinx & Restructured Text
   :description: Instructions and examples on using Restructured Text mark-up.
   :language: en-US
   :keywords: sphinx, restructured text, restructuredtext
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <../documentation/index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`


.. cssclass:: kb-list
.. _`sphinx-restructured-text`:

=============================
Sphinx & reStructuredText
=============================

The Codership Library uses a Python documentation system called, Sphinx.  It converts reStructuredText files into HTML web pages, as well as other formats (e.g., PDF and EPub). As for reStructuredText, it's a lightweight mark-up language that can be processed by Sphinx, and is easily readable by people.

This page of the Library, in the Editors section provides some examples of how to use reStructuredText to format text and organize document pages in the Library.  This is not a comprehensive list of formatting codes available, but rather a list of what we use in the Library |---| and only those we thought to add to this page.


-------------------
Text Formatting
-------------------

How to format text on pages of the Library is easiest and primary use of any mark-up language. Below are examples of how to format text, how to italicize, bold-face, and other basic formatting.

.. csv-table:: Inline Formatting
   :class: doc-options
   :header: "format", "example", "results"

   "italics", "\*text\*, \`text\`", "*text*"
   "bold", "\*\*text\*\*", "**text**"
   "monospace font",	"\``text``", "``text``"



-------------------
Lists
-------------------

If you want to present a list of items, you can use bullets.  In HTML, these are \<li> tags for each list item, grouped withing a pair \<ul> tags for an unnumbered list.  To generate these in restructuredtext,  you need only preface a bullet item with a hyphen and a space like so:

.. code-block:: text

   - some text
   - more text
     + some sub-text
     + more sub-text
   - other text

The lines preceded by hyphens will produce bullets.  The items preceded by plus-signs will produce a sub-bullet list. Notice that there's nothing to enter for the \<ul> tags. Below is the HTML text the code above will produce:

.. code-block:: html

   <ul class="simple">
   <li>some text</li>
   <li>more text<ul>
   <li>some sub-text</li>
   <li>more sub-text</li>
   </ul>
   </li>
   <li>other text</li>
   </ul>


numbered bullets:	#. text

Adding class to <ul> tag

   .. code-block:: text

      .. rst-class:: video-stats

      - Speaker:  Sakari Keskitalo, Philip Stoev
      - Date:  February 22, 2017
      - Length of Video:  52 minutes




-------------------
Special Characters
-------------------

If you want to use an emdash, you would enter three hyphens enclosed in a pair of bars, with spaces on both sides (i.e., ``|---|`` ).   At the bottom of the document, place the following code:

.. code-block:: text

   .. |---|   unicode:: U+2014 .. EM DASH
      :trim:

To add a hard-return, an HTML break tag, you can use *br*, wrapped in a pair of bars (i.e., ``|br|``).  At the bottom of the document, you would enter the following code:

.. code-block:: text

   .. |br| raw:: html

      <br/>



-------------------
Links
-------------------

For better navigation and richer information, all of the pages in the Library have links to other pages or other web sites.  These are accomplished, of course, with links.  The table below shows how to create links using Restructured Text mark-up:

.. csv-table::
   :class: doc-options
   :widths: 25, 40, 35
   :header: "Type", "Example", "Result"

   "External", "\`Label \<\http\:\/\/domain.com\/>\`\_", "`Label <http://domain.com/>`_"
   "Internal", "\:doc\:\`Page \<./library/page>\`", ":doc:`Page <./index>`"



-------------------
New Pages
-------------------

When new pages are added to Library, they must be included in the table of contents (i.e., ``toctree``) of a pages |---| typically an index.rst file |---| so that it may be included in the PDF versions of the documentation.  Below is how you would include three pages under the one on which these formatting codes are entered:

.. code-block:: text

   .. toctree::
     :maxdepth: 2

      some-document
      another-document

These will link two documents to the one which contains this text.  It will also put links to them on the page, wherever this is entered. The link will include the heading from each page.  Notice that the document file name did not include the file extention (i.e., ``.rst``).


-------------------
Meta Tags
-------------------

Meta tags are used to provide extra information to web browsers and search engines.  For instance the \<title> tag in the heading of an HTML page provides the title that you will see at the top of the browser, perhaps in the tabs. The \<description> tag can be used by the search engine to display a descpription you'll see in the search results. The \<keywords> tag helps to improve the ranking in searches.

There are many meta tags that may be included in an HTML page. Below is how you would add them to a page formatted with Restructured Text:

.. code-block:: text

   .. meta::
      :title: Sphinx & Restructured Text
      :description: Instructions on using Restructured Text mark-up.
      :language: en-US
      :keywords: sphinx, restructured text, restructuredtext
      :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.

This block of code should be entered at the very top of the document.  Below is the results of the above; it's the tags that can be see when looking at the page source in the web browser.

.. code-block:: html

   <head>
   <meta content="Sphinx &amp; Restructured Text" name="title" />
   <meta content="Instructions on using Restructured Text mark-up." name="description" />
   <meta content="en-US" name="language" />
   <meta content="sphinx, restructured text, restructuredtext" name="keywords" />
   <meta content="Codership Oy, 2014 - 2019. All Rights Reserved." name="copyright" />
   ...
   </head>



-------------------
CSS Classes & IDs
-------------------

Adding a CSS class or a CSS identification to an HTML tag is tricky with restructuredtext.  One way is to use ``rst-class`` like so:

.. code-block:: css

   .. _`some-link-point`:
   .. rst-class:: my-class
   .. rubric:: Some Sub-Heading

      A paragraph with some sort text, talking about something or other.

Below are the results of the above formatting codes:

.. code-block:: html

   <p class="my-class rubric" id="something-unique">Some Sub-Heading</p>

   <p>A paragraph with some sort text, talking about something or other.</p>



.. cssclass:: tutorial-article



We use Cascading Style Sheets (CSS) to set the fonts, margins, and other such text and page formats. However, you may want to add style for just one page.  To do this, you can use the ``raw`` directive like so:


-------------------
Raw HTML
-------------------

Sometimes the easiest approach to achieving something in HTML is to add a raw HTML tag.  This will require you to define or declare it, usually near the top of the file, and then invoking it as needed. Here's how you would declare it:

.. code-block:: html

   .. role:: raw-html(raw)
      :format: html

Below is how you would then use it to put \<small\> tags around some text:

.. code-block:: html

   :raw-html:`<small>a minor point</small>`



abbreviations:	:abbr:`s.t. (Some Text)`



.. |---|   unicode:: U+2014 .. EM DASH
      :trim:
