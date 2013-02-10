This is a very simple Python script to convert a [markdown][1] formatted file
file to a [scrolldeck.js][1] presentation. The usage is:

    ./compile.py file.md > file.html

Originally, the script deals with verbose presentations for academic purposes,
using one slide per parapgrah with citations at the bottom.

If you want to modify the default behavior, then you need to edit the regular
expressions in the `compile.py` file. The header, footer and CSS can me
modified in the `parts` and `css` folder. The `$.scrolldeck` jQuery call can be
modified in the `parts/footer.html` file.

The first slider with bigger and centered texts is located in the
`parts/header.html` file.

A sample presentation is something like:

    # Main Section

    ## Inner Section

    Some verbose citation or statemente here. `Optional author or reference
    here`

    Some other paragrah that will be converted in a slide.

    ## Another Inner Section and so on...

    This is the 6th slide. `I'm saying this`


[1]: http://johnpolacek.github.com/scrolldeck.js/
[2]: http://daringfireball.net/projects/markdown/
