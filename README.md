ghost-example
=============

Simple test for others to run to replicate possible 'bug' in GhostDriver


This test was created using OSX Lion but also occurs on Ubuntu 12.04

To get the test running you will need the following:

1. Python 2.7
2. PhantomJS
3. Selenium
4. Homebrew

Setup is simple (I would recomend using a virtualenv to keep things nice and tidy):

    pip install selenium
    brew install phantomjs

That should do it provided you have all the other stuff.  Now run the thest:

./tests/click_fail_test.py


