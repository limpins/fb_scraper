import shelve
from fb_posts import scrapeFacebookPageFeedStatus2
from fb_posts_realtime import scrapeFacebookPageFeedStatus
from fb_comments_page import scrapeFacebookPageFeedComments
import time

#import fb_pages
# Function to scrape with.
# Call with group id and whether you want to scrape all the way back 0 or since last scrape 1.
# To do: allow passing of an array of groups, allow passing of a custom scrape date, add functions for scraping of pages
# To do create unit tests to make sure it runs.
def scrape_groups_pages(page_id, from_time, function_number, page_or_group, comments):
    funcs = [scrapeFacebookPageFeedStatus,scrapeFacebookPageFeedStatus2, scrapeFacebookPageFeedComments]
    scrape(page_id, from_time, funcs[function_number], page_or_group, comments)

# Get to time scrape from
def get_tstamp(page_id, tstamp ,path):
    if tstamp is 1:
        d = shelve.open(path)
        if page_id in d:
            time_opened = d[page_id]
            pageStamp = str(time_opened)
            print("Scraping since unix time " + pageStamp)
        else:
            print("key not found in dict proceeding with full scrape")
            pageStamp = -2180131200
    elif tstamp is 0:
        pageStamp = -2180131200
    else:
        pageStamp=tstamp
    return pageStamp

# Save the time the last time page was scraped
def save_shelve(page_id, path):
    timestamp = int(time.time())
    d = shelve.open(path)
    d[page_id] = timestamp
    d.close()
    return "shelve successfully saved at time"

#
def get_access(app_id, path):
    with open(path, 'r') as f:
        f.readline().strip("/n")
        second_line = f.readline()
    app_secret = second_line
    access_token = app_id + "|" + app_secret
    return access_token


def scrape(page_id,tstamp,scrape_func, page_or_group, comments):
    access_token = get_access("238791666290359",'app.txt')
    if comments:
        pageStamp = get_tstamp(page_id + "_comments", tstamp, "save_times")
        save_shelve(page_id + "_comments", 'save_times')
    else:
        pageStamp = get_tstamp(page_id, tstamp, "save_times")
        save_shelve(page_id,'save_times')
    scrape_func(page_id, access_token, pageStamp, page_or_group)




#if __name__ == '__main__':
    #group_id = "115285708497149"
    #scrape(group_id, 0,scrapeFacebookPageFeedStatus2)


