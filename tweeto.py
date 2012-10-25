import json
import oauth2 as oauth
import urllib
 
ckey='eSXhSq76HVGz0DYi7yxiXQ'
csecret='SMVxVN644DqUk7jT7mHs4ltSEw1XRTH02WBpCs2H3h0'
akey='871928226-eAGoKxJ2zXZ9LvP9hbQ51ejjJQhtko7BH2v7U3GM'
asecret='fZxZUh8RAZOmLK3s5IVciX6htj4m8e6T5CkgBY5JU'
 
def post_twitter(status):
    try:
        consumer = oauth.Consumer(key=ckey, secret=csecret)
        token = oauth.Token(key=akey, secret=asecret)
        client = oauth.Client(consumer, token)
        resp, content = client.request(
            'https://api.twitter.com/1.1/statuses/update.json',
            method='POST',
            body = urllib.urlencode({"status": status,
                                     "wrap_links": True}),
            #headers=http_headers,
            #force_auth_header=True
            )
    except oauth.Error as err:
        print("Twitter Error:"+err)
    return resp, content

def get_timeline(screen_name=None, user_id=None):
    # Get the proper user
    if screen_name and user_id:
        body = urllib.urlencode({'screen_name': screen_name,
                                 'user_id': user_id})
    elif screen_name:
        body = urllib.urlencode({'user_id': user_id})
    elif user_id:
        body = urllib.urlencode({'screen_name': screen_name})
    else:
        return

    try:
        consumer = oauth.Consumer(key=ckey, secret=csecret)
        token = oauth.Token(key=akey, secret=asecret)
        client = oauth.Client(consumer, token)
        resp, content = client.request(
            'https://api.twitter.com/1.1/statuses/user_timeline.json',
            method='GET',
            body=body,
            #headers=http_headers,
            #force_auth_header=True
            )
    except oauth.Error as err:
        print("Twitter Error:"+err)
    return resp, json.loads(content)


 
# response, content = post_twitter("@GV_party Olivet College Computer Science Lab")
# print response # {'status': '200', 'content-length': '2008', 'x-transaction': 'b249a671a17e133a', 'x-access-level': 'read-write-directmessages', 'expires': 'Tue, 31 Mar 1981 05:00:00 GMT', 'x-mid': 'eeb4e621e67b4c5d5282dbbc7a3d7ea9f6433520', 'x-transaction-mask': 'a6183ffa5f8ca943ff1b53b5644ef11420c80de6', 'server': 'tfe', 'last-modified': 'Tue, 23 Oct 2012 19:52:16 GMT', 'x-runtime': '0.14685', 'etag': '"3d30507fd7fb787b09807184ec572259"', 'pragma': 'no-cache', 'cache-control': 'no-cache, no-store, must-revalidate, pre-check=0, post-check=0', 'date': 'Tue, 23 Oct 2012 19:52:17 GMT', 'x-frame-options': 'SAMEORIGIN', 'content-type': 'application/json; charset=utf-8', '-content-encoding': 'gzip', 'vary': 'Accept-Encoding', 'set-cookie': 'k=10.36.54.105.1351021936863879; path=/; expires=Tue, 30-Oct-12 19:52:16 GMT; domain=.twitter.com, guest_id=v1%3A135102193689074450; domain=.twitter.com; path=/; expires=Fri, 24-Oct-2014 07:52:16 GMT, dnt=; domain=.twitter.com; path=/; expires=Thu, 01-Jan-1970 00:00:00 GMT, lang=en; path=/, lang=en; path=/, lang=en; path=/, twid=u%3D871928226%7CdYHbwQNx8Nvz%2BWqxlV5eJ7ycyf4%3D; domain=.twitter.com; path=/; secure, _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAPBLo86AToMY3NyZl9p%250AZCIlOTVjMDIzYTlhZmE5ZDk2YzFiZjI4NTlhZTcxOTY4ZTg6B2lkIiUxY2Ri%250ANDY0MGU2OGE2ZmM3OTBhOWFlZjRlMTY2ZjFmMw%253D%253D--e0c67632317a6f20b750a8b857b55f4e6d296c0e; domain=.twitter.com; path=/; HttpOnly'}
# print content # {"in_reply_to_user_id_str":"80118741","entities":{"urls":[],"hashtags":[],"user_mentions":[{"name":"Global Village Band","screen_name":"GV_party","id_str":"80118741","indices":[0,9],"id":80118741}]},"place":null,"retweeted":false,"contributors":null,"retweet_count":0,"geo":null,"in_reply_to_status_id":null,"truncated":false,"text":"@GV_party Olivet College Computer Science Lab","id_str":"260831024605446144","coordinates":null,"in_reply_to_screen_name":"GV_party","in_reply_to_user_id":80118741,"created_at":"Tue Oct 23 19:52:16 +0000 2012","favorited":false,"user":{"id":871928226,"follow_request_sent":false,"following":false,"screen_name":"occslab","url":null,"profile_use_background_image":true,"created_at":"Wed Oct 10 14:54:10 +0000 2012","profile_text_color":"333333","utc_offset":null,"statuses_count":1,"default_profile_image":true,"verified":false,"name":"Olivet CSLab","favourites_count":0,"profile_sidebar_border_color":"C0DEED","friends_count":1,"description":"Olivet College Computer Science Lab - Mott 112","profile_image_url":"http:\/\/a0.twimg.com\/sticky\/default_profile_images\/default_profile_1_normal.png","protected":false,"location":"","entities":{"description":{"urls":[]}},"profile_background_tile":false,"is_translator":false,"profile_sidebar_fill_color":"DDEEF6","followers_count":0,"contributors_enabled":false,"default_profile":true,"time_zone":null,"notifications":false,"lang":"en","id_str":"871928226","profile_background_color":"C0DEED","profile_background_image_url_https":"https:\/\/si0.twimg.com\/images\/themes\/theme1\/bg.png","geo_enabled":false,"profile_image_url_https":"https:\/\/si0.twimg.com\/sticky\/default_profile_images\/default_profile_1_normal.png","listed_count":0,"profile_background_image_url":"http:\/\/a0.twimg.com\/images\/themes\/theme1\/bg.png","profile_link_color":"0084B4"},"source":"\u003Ca href=\"http:\/\/cslab.cs.olivetcollege.edu\" rel=\"nofollow\"\u003ECSLab Tweet\u003C\/a\u003E","in_reply_to_status_id_str":null,"id":260831024605446144}

# response, content = get_timeline('@GV_party')
# print response
# content = json.loads(content)
# print len(content)
# print content[0]
# print content[0]
