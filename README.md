# Words that are hex colours

This project finds words that can be converted into valid hexadecimal colour codes. It started with a Dutch word list, but you can use any language you like.

▶ [View the demo](https://aidanwyber.github.io/Kleurwoorden/)

Based on [this Dutch word list](https://github.com/OpenTaal/opentaal-wordlist/blob/master/elements/wordlist-ascii.txt).

## How it works

The pipeline is pretty straightforward. The Python script reads through a word list and looks for words that are exactly six characters long. It then checks if those words contain only letters that either exist in hexadecimal notation or can be cleverly substituted with numbers that look similar.

The substitution rules are simple: the letter "o" becomes zero, "l" and "i" both become one, "z" becomes two, "s" becomes five, "t" becomes seven, and "g" becomes nine. So a word like "facade" already works perfectly as a hex colour since it only uses valid hex characters. But a word like "badass" gets transformed into "#BADA55" by replacing the "s" characters with fives.

Once the script finds all the valid words, it converts them into proper hex colour codes and saves everything to a JSON file. The web page then loads that JSON and displays each word as a coloured tile, showing you both the original word and its hex code.

## Adding your own word list

If you want to try this with words from another language or a different word source, it's easy to swap in your own list. Just replace the `wordlist-ascii-NL.txt` file with your own text file containing one word per line. The script expects lowercase words without any special characters or accents.

You'll also want to update line 3 in `find_colour_words.py` to match your new filename. Then just run the script with Python and it will generate a fresh `colour_words.json` file with whatever colour words it finds in your list. Open up `index.html` in a browser and you'll see your new colour words displayed as tiles.
