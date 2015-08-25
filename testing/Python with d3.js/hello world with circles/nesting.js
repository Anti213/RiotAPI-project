d3.json("tweets.json",function(data) {
 var tweetData = data.tweets;
 var nestedTweets = d3.nest()
 .key(function(el) {return el.user})
 .entries(tweetData);
});