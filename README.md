# Multiple-Choice-Randomizer-and-Tex-Generator
Given an input file, code randomizes the questions and associated options and prints multiple variations to a .tex file.

In order for the software to correctly produce a .tex file, a .txt file must be in a particular format.
See Format.txt for the formatting information and Example.txt for an example. Also provided are the .tex files when Example.txt is used as an input. A helpful answer sheet is also generated into a .txt.

mcRanTexGen.py depends only on built-in Python libraries. This was written in Python 2.7 so Python 3 users beware.
The .tex files use packages etoolbox and geometry as well as the exam class. These are readily available in most .tex distributions.

The program has a built in "cleaner" to help remove non-ascii characters or to replace common characters to be more .tex friendly. However please do not insert special characters with the intention to break the code ... you will.
