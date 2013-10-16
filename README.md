#Newsblur starred stories to atom feed

Uses the Newsblur API to get starred stories and turn them into an atom feed.

##Usage

Create a file named `config.py` that has `username` and `password` as exports - these will be used to login to Newsblur.

Then run from a shell and direct the output to the feed file:

`get_feed.py > feed_file.xml`

## Acknowledgements

Uses code from:

 * Newsblur: https://github.com/samuelclay/NewsBlur/tree/master/api
 * Webhelpers: https://bitbucket.org/bbangert/webhelpers/src/59054a81edec/webhelpers?at=trunk
