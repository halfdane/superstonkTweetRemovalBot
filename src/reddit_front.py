import praw
import os
import logging

class RedditFront:
    LOG = logging.getLogger(__name__)

    def __init__(self, test=False):
        user_agent = "desktop:com.halfdane.superstonk_tweet_removal_bot:v0.0.1 (by u/half_dane)"
        self.LOG.debug("Logging in..")
        self.username=os.environ["reddit_username"]

        self.reddit = praw.Reddit(username=self.username,
                        password=os.environ["reddit_password"],
                        client_id=os.environ["reddit_client_id"],
                        client_secret=os.environ["reddit_client_secret"],
                        user_agent=user_agent)
        self.LOG.info(f"Logged in as {self.reddit.user.me()}")

        self.reddit.validate_on_submit = True
        self.subreddit = self.reddit.subreddit(os.environ["target_subreddit"])
        self.LOG.info(f'working in {self.subreddit.display_name}')

        for removal_reason in self.subreddit.mod.removal_reasons:
            if ("Mass Shared Content" in removal_reason.title):
                self.removal_reason = removal_reason

        if (not hasattr(self, 'removal_reason')):
            raise Exception("Couldn't find a fitting removal reason! Aborting now.")
        self.LOG.info(f"Using the removal reason [{self.removal_reason.title}] for removals")

        self.allowed_to_tweet=os.environ["allowed_to_tweet_username"]

        self.test = test

    def removeDuplicateTweets(self):
        for legit_post in self.subreddit.search(f"author:{self.allowed_to_tweet} title:\"New Tweet from\"", sort='new'):
            logging.info(f"Checking for duplicates of {legit_post.url}")
            for post in self.subreddit.search(f"url:{legit_post.url} -author:{self.allowed_to_tweet}", sort='new'):
                logging.info(f"Found duplicate: {post.permalink}")
                if not self.test:
                    logging.info(f"Found duplicate, removing it.")
                    post.mod.remove(mod_note="Automatically removed by superstonk_tweet_removal_bot", reason_id=self.removal_reason.id)
                else:
                    logging.info(f"This is a test, not actually doing anything")



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    reddit_front = RedditFront(test=True)
    reddit_front.removeDuplicatePosts()
