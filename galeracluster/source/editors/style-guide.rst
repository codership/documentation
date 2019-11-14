.. meta::
   :title: Codership Editors' Page
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`
      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`
   - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`
   

.. cssclass:: library-index
.. _`style-guide`:

=============================
The Codership Style Guide
=============================

This style guide is a little haphazard at the moment. Rather than dedicate a significant amount of time to it, since our priority is improving, updating, and expanding the content of the Library, we add to this style guide when a style policy occurs to us during the course of our work.  After we have accumulated several style policies, we'll better organize this page. For now, there is no ordering to them.


.. _`style-numbers-symbols`:
.. rst-class:: section-heading
.. rubric:: Numbers & Symbols

Ampersands shouldn't be used in sentences, unless they are part of an organization's name (e.g., *Dolce & Gabbana*). They may be used in section and page titles (e.g., the title above this paragraph).

Arabic numbers shouldn't be used in sentences, unless they are meant to provide the value of something: *Set the wsrep_slave_threads variable to a value of at least 3.*

Here is an example of a sentence that would not be good form based on the above style policies and a couple of others here:

*The main 2 DBs used are MySQL & MariaDB... but not XtraDB!! ;)*


.. _`style-case`:
.. rst-class:: section-heading
.. rubric:: Case

Page heading and section headings should use title case.  That is to say, the initial letter of each word should be capitalized, unless it's a small word (e.g., an article or a preposition).  Here's an example: *An Administrator's Guide to Galera Cluster*.

Don't ever use all capitals for emphasis a point. Here's an example, which is unacceptable:  *When a cluster goes down, DON'T start the first node to leave the node first!!!*  This gives the reader a sense that you think they're so incompetent that they can't read the word *don't* as a negative unless you capitalize it. It's also the equivalent of yelling or speaking in a condescending way.  If you want to emphasize a point so it won't be missed, elaborate instead.


.. _`style-punctuation`:
.. rst-class:: section-heading
.. rubric:: Punctuation

Exclamation points should almost never be used anyway. The documentation is meant to be serious and therefore, not exciting. Related to this, sentences of exclamation should also be avoided:  *That's it! You're done.*  Not only is that unnecessary, it can be irritating the reader wasn't successful while following along.

The exception to not using exclamation points and exclamative sentences is tutorial articles and videos. In those forms, there is a more personal voice used to make the learner feel comfortable, as well as to communicate our pride in our products or work.

Ellipses never used in sentences. They may be used, though, to substitute code that has been omitted from an example. Punctuation used to form an emotional icon should never be used.

In compliance with the Modern Language Association, If a sentence ends with quoted text, the period should go outside of the quote marks |---| unless the entire sentence was a quote.  Here's an example of when the period belongs on the outside the quotes:

*Galera Cluster is said to provide "virtual syncronous replication".*


.. _`style-abbreviations-acronyms`:
.. rst-class:: section-heading
.. rubric:: Abbreviations & Acronyms

If an abbreviation or an acronym is so familiar (e.g., DBA) that it is used more often than written in full, it may be used. However, assume the reader is unfamiliar with the abbreviation and provide the full text within parentheses (Database Administrators) the first time the abbrieviation is used in a document. For abbreviations that are not so common, write the full version with the abbrieviation in parentheses the first time used in a document, and then use only the abbreviation thereafter:  *A new node will be synchronized using the State Snapshot Transfer (SST) method.*


.. _`style-regional-usage`:
.. rst-class:: section-heading
.. rubric:: Regional Usage

Since the U.S. is the dominant country in the software industry, we tend toward American word usage, spelling, and other such choices.  For instance, we would use the word *elevator* instead of *lift*, and spell *organization* with a *z* and not an *s* (i.e., not *organisation*).  However, since Codership is based in Finland and it's an internation organization, we write dates with the day first, followed by the month and year.  So we'll write the first of June as *1 June 2019*, not *June 1, 2019*.

Try very much to avoid dates with slashes (e.g. *6/1/2019*) since which is the month can be confusing to readers. This exception is if the date is the result of a function (e.g., CURDATE() in MySQL). Then you would then write it as the function returns it (e.g., *2019-08-03*).


.. _`style-phrases-expressions`:
.. rst-class:: section-heading
.. rubric:: Unnecessary Phrases & Expressions

Don't use opening or transitional phrases.  For example, don't start a sentence with the phrase, *In the event that*, when you can write simply, *If*.  Don't write rhetorical, unnecessary sentences or phrases.  Here are some examples of the opening phrases:  *Having said that...* isn't necessary since the reader knows what you just said or wrote;  *It goes with out saying...* is pointless since what follows is what doesn't need to be said;  *Not to mention...* is irritating if you're about to mention it |---| instead, delete the whole sentence; don't mention it.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
