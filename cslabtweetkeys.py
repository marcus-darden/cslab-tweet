import json
import oauth2 as oauth
import urllib

ckey='eSXhSq76HVGz0DYi7yxiXQ'
csecret='SMVxVN644DqUk7jT7mHs4ltSEw1XRTH02WBpCs2H3h0'
akey='871928226-eAGoKxJ2zXZ9LvP9hbQ51ejjJQhtko7BH2v7U3GM'
asecret='fZxZUh8RAZOmLK3s5IVciX6htj4m8e6T5CkgBY5JU'

def get_client():
	try:
		consumer = oauth.Consumer(key=ckey, secret=csecret)
		token = oauth.Token(key=akey, secret=asecret)
		client = oauth.Client(consumer, token)
	except oauth.Error as err:
		print 'Something bad happened!'

	return client


def post_twitter(client, status):
	try:
		response, content = client.request(
			'https://api.twitter.com/1.1/statuses/update.json',
			method='POST',
			body=urllib.urlencode({'status': status,
								   'lat': 42.4414,
								   'long': 84.9242,
								   'display_coordinates': True}))
	except Error as e:
		print 'Something else bad happened.'

	return response, content

def get_timeline(client, screen_name=None, user_id=None):
    # Get the proper user
    if screen_name and user_id:
        body = urllib.urlencode({'screen_name': screen_name,
                                 'user_id': user_id})
    elif screen_name:
        body = urllib.urlencode({'user_id': user_id})
    elif user_id:
        body = urllib.urlencode({'screen_name': screen_name})

    try:
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


cslab = get_client()

r, c = post_twitter(cslab, 'FOR THE WIN!!! -From the Raspberry Pi')
#r, c = get_timeline(cslab, 'occslab')

print r
print c


"""
{"entities":{"urls":[],"hashtags":[
	{"text":"dontstop","indices":[38,47]}],
	"user_mentions":[{"name":"Global Village Band","screen_name":"GV_party","id_str":"80118741","indices":[22,31],"id":80118741}]}

{'status': '200', 'content-length': '1858',
 'x-transaction': 'ac9090bf3740a612',
 'x-access-level': 'read-write-directmessages',
 'expires': 'Tue, 31 Mar 1981 05:00:00 GMT',
 'x-mid': '45976aaaadfb523694d30aefb0ba3b9389624034',
 'x-transaction-mask': 'a6183ffa5f8ca943ff1b53b5644ef11420c80de6',
 'server': 'tfe', 'last-modified': 'Wed, 24 Oct 2012 15:35:55 GMT',
 'x-runtime': '0.12974', 'etag': '"5a0f0d32cde3db069347fb1016f7340b"',
 'pragma': 'no-cache', 'cache-control': 'no-cache, no-store, must-revalidate,pre-check=0, post-check=0',
 'date': 'Wed, 24 Oct 2012 15:35:55 GMT', 'x-frame-options': 'SAMEORIGIN', 'content-type': 'application/json; charset=utf-8',
 '-content-encoding': 'gzip', 'vary': 'Accept-Encoding', 'set-cookie': 'k=10.35.62.137.1351092955576074; path=/; expires=Wed, 31-Oct-12 15:35:55 GMT; domain=.twitter.com, guest_id=v1%3A135109295558028035; domain=.twitter.com; path=/; expires=Sat, 25-Oct-2014 03:35:55 GMT, dnt=; domain=.twitter.com; path=/; expires=Thu, 01-Jan-1970 00:00:00 GMT, lang=en; path=/, lang=en; path=/, lang=en; path=/, twid=u%3D871928226%7CdYHbwQNx8Nvz%2BWqxlV5eJ7ycyf4%3D; domain=.twitter.com; path=/; secure, _twitter_sess=BAh7CToPY3JlYXRlZF9hdGwrCMhpapM6AToMY3NyZl9pZCIlZWJjYjI2Yzli%250AZDU4NDBlNTVkZjdiZDE0NDMwYzZhYTciCmZsYXNoSUM6J0FjdGlvbkNvbnRy%250Ab2xsZXI6OkZsYXNoOjpGbGFzaEhhc2h7AAY6CkB1c2VkewA6B2lkIiU3MTlm%250AYzBkYTg5MzgyMWYzYjgxMzk1YjdlYWNjNTg4Yg%253D%253D--684dfbc1c46b6658d605ca78b484f38888fcb40e; domain=.twitter.com; path=/; HttpOnly'
}

{"entities":{"urls":[],"hashtags":[],"user_mentions":[]},
 "place":null,"retweeted":false,"contributors":null,
 "retweet_count":0,"geo":null,"in_reply_to_status_id":null,
 "truncated":false,"text":"Happy Wednesday!",
 "id_str":"261128898568396800","in_reply_to_status_id_str":null,
 "coordinates":null,"in_reply_to_screen_name":null,
 "in_reply_to_user_id":null,
 "created_at":"Wed Oct 24 15:35:55 +0000 2012",
 "favorited":false,"in_reply_to_user_id_str":null,

 "user": {"id":871928226,"follow_request_sent":false,
          "following":false,"screen_name":"occslab",
          "url":null,"profile_use_background_image":true,
          "created_at":"Wed Oct 10 14:54:10 +0000 2012",
          "profile_text_color":"333333","utc_offset":null,
          "statuses_count":2,"default_profile_image":true,
          "verified":false,"name":"Olivet CSLab",
          "profile_image_url_https":"https:\/\/si0.twimg.com\/sticky\/default_profile_images\/default_profile_1_normal.png",
          "favourites_count":0,"profile_sidebar_border_color":"C0DEED",
          "friends_count":1,"description":"Olivet College Computer Science Lab - Mott 112",
          "profile_image_url":"http:\/\/a0.twimg.com\/sticky\/default_profile_images\/default_profile_1_normal.png","protected":false,"location":"","entities":{"description":{"urls":[]}},"profile_background_tile":false,"profile_sidebar_fill_color":"DDEEF6","followers_count":0,"contributors_enabled":false,"default_profile":true,"time_zone":null,"notifications":false,"lang":"en","id_str":"871928226","profile_background_color":"C0DEED","profile_background_image_url_https":"https:\/\/si0.twimg.com\/images\/themes\/theme1\/bg.png","geo_enabled":false,"is_translator":false,"listed_count":0,"profile_background_image_url":"http:\/\/a0.twimg.com\/images\/themes\/theme1\/bg.png","profile_link_color":"0084B4"},"source":"\u003Ca href=\"http:\/\/cslab.cs.olivetcollege.edu\" rel=\"nofollow\"\u003ECSLab Tweet\u003C\/a\u003E","id":261128898568396800}
"""