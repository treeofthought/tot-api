Upsets–when a worse-seeded team defeats a better one–are one of the most exciting features of the NCAA Division I basketball tournament. Since 1985, when the tournament went to a 64-team format, the four one-seeds have always played the four sixteen-seeds in the first round of each tournament. The sixteen-seeds have never won. (In contrast, fifteen-seeds have upset two-seeds eight times in 128 attempts.)

A friend of mine suggested I check if sixteen-seeds were making any progress. In other words, are the one-seed margins of victory shrinking? My usual response to hobby analytics suggestions is:
      
1. Say, "cool idea, thanks for thinking of me."
2. Start poking around for data
3. Give up

In this case, kaggle makes a bunch of helpful March Madness data available, robbing me of the the “data is hard to find” excuse. In fact, it was easy to repurpose their lovely data to this question.

All I had to do was subtract the number of points scored by the sixteen-seed from the number scored by the one-seed in all previous match-ups, and look for patterns in this metric over time. A good place to start with this sort of analysis is a scatterplot:

![The initial scatterplot](http://127.0.0.1:5000/static/march-math-madness/scatter.png)

I definitely don’t see a clear trend, but we’re only just getting started. Let’s add a LOESS smoother:

![The initial scatterplot with smooter](http://127.0.0.1:5000/static/march-math-madness/scatter-loess.png)

Looks like there is an upward trend through 1996, then victory margins are flat or shrinking ever since. It wasn’t quite clear before the smoother, but now I see the pattern. It looks like the closest sixteen-seeds ever came was the late 80’s, but since then they rarely come within 10 points. There also were more big blowouts in the late nineties and early aughts.

Given the strong evidence of an upward trend from ’85 to ’96, we can safely reject the assertion that these games are getting closer since the introduction of the 64 team format. Let’s misbehave slightly and focus on just 1997 and onward. (The cherrypicking could have been avoided. We have 4 datapoints per season, I could have randomly divided the data so we get 2 datapoints per season, use that set to look for a place to start the search for the downward trend, and then try to confirm the hypothesis with the remaining half of the data. The good news is WordPress doesn’t have a very strict peer-review.)

While I’m at it, I’m going to replace the LOESS smoother with a linear one, because it will make the size of any observed effect easier to quantify:

![The initial scatterplot with linear smoother](http://127.0.0.1:5000/static/march-math-madness/margin-regressed.png)

Well, look at that! A nice, negative slope.

Of course, a slightly tilted line will occur by random chance much more often than a perfectly flat line even when no real trend exists. My favorite way to measure the strength of a linear trend is the following procedure:

1. Compute the slope of the trend line (-0.48 in our case)
2. Randomly shuffle the order of the data
3. Re-compute the slope of the trend line
4. Repeat steps 2 and 3 10,000 or 100,000 times
5. See how extreme our “true” slope measurement is compared to all the random ones

The idea is that either this data is essentially flat over time, or else time affects the values we observe. If the dataset is essentially flat, then shuffling it randomly will produce slopes that are similar in magnitude to our observed slope. If the ordering had a strong effect on the slope we observed, then our observation will stand out.

This was the result:

![Histogram of slopes](http://127.0.0.1:5000/static/march-math-madness/permutation.png)

The fact that our observation is so far left, and so few of the permutation slopes are further left, is strong evidence that our observed slope value is not just random chance. I would therefore assert with some confidence that since 1997, sixteen-seeds are getting closer to beating one-seeds.

They still have a long way to go. Recently, they lose by about 22 points on average, and seem to be improving by about half a point per year. This means they should be consistently beating the one seeds by 2067.
