import sys, getopt, os
import logging

from reddit_front import RedditFront

def main(argv):
    test = False
    try:
        opts, args = getopt.getopt(argv, "t")
    except getopt.GetoptError:
        logging.error('main.py [-t testrun]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-t':
            test = True

    redditFront = RedditFront(test=test)
    redditFront.removeDuplicateTweets()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main(sys.argv[1:])
