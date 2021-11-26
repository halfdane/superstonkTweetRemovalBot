# superstonkTweetRemovalBot

A bot that identifies its own posts and uses them to remove duplicate posts from other users.
For the time being, it will use the linked URL to find the duplicates.

Passing the parameter '-t' enables the test-mode which doesn't create a reddit post.


# Run

You have to export the following environment variables:

    export reddit_client_id="some-client-id"
    export reddit_client_secret="random gibberish"
    export reddit_username="half_dane"
    export reddit_password="very_secret"

    export target_subreddit="Superstonk or a test subreddit"

Afterwards execute

    make

This sets up the venv for python and downloads the necessary dependencies before running the bot in test-mode 

# Targets

    make fake_run   # execute the bot in test mode.
    make run        # execute the bot in normal mode. Please note that this will create a new comment with each execution
    make clean      # clean up compile results and the venv
