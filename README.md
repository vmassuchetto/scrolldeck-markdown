This is a very simple Python script to convert a [markdown][1] formatted file
file to a [scrolldeck.js][1] presentation. The usage is:

    ./compile.py file.md > file.html

Originally, the script deals with paragraphs as presentations, if you want to
modify this, then you need to edit the regular expressions in the `compile.py`
file.

The header, footer and CSS can me modified in the `parts` and `css` folder. The
`$.scrolldeck` jQuery call can be modified in the `parts/footer.html` file.

[1]: http://johnpolacek.github.com/scrolldeck.js/
[2]: http://daringfireball.net/projects/markdown/
