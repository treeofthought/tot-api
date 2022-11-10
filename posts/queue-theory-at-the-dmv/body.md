I spent three and a half hours at the DMV the other day.

Cool story, Stuart. Tell it again.

If you insist!

After a series of unrelated but poor decisions, I found myself walking into an office of the DMV at 9:30 AM. This office bills itself as a "License Express." Since I needed a new license, and I wanted the experience to be express, I thought I was in the right place.

Step one was to get a picture taken and do some paperwork. This took about 5 minutes. Express indeed!

Step two was to wait for my number to be called so a kind and sympathetic DMV employee could help me sort out getting a new license.

Step one did not set my expectations for step two.

Tragedy struck in slow motion. Very slow motion. They gave me ticket R833. I looked up in time to see R781 be called. 48 numbers away? That didn’t seem right. There were codes other than "R" being called, and only about 50 people in the room. The numbers must not be sequential. This is the License Express! I was sure I’d be on my way in no time.

The next number was R782. Then R783. My hope turned to ash as I realized the License "Express" had betrayed me.

Due to one of those "unrelated but poor decisions," my phone had just 4% battery. I had to conserve this in case I needed to call home and tell my parents I loved them before dying of starvation at the DMV. Thus, I was unable to kill the time browsing reddit.

I set about distracting myself the only way I could think of–trying to guess when I would be able to leave.

At 10:06, I noted that R787 was called.

Cruelly, R788 came thirteen minutes later. I couldn’t know it at the time, but this would be the largest gap I observed all day. Fate was having fun with me.

One data point doesn’t make for a great model, but it does serve to illustrate the simplest way we can predict departure time: it took thirteen minutes to get from R787 to R788. At that point, I had 833 – 788 = 45 numbers to go. At thirteen minutes per number, that’s 13 x 45 = 585 minutes = 9 hours and 45 minutes. Meaning I’d be leaving the DMV and going my merry way at 8:07PM.

Fortunately for my sanity (and more importantly, my ongoing employment), the pace picked up. By keeping track of the average time between numbers being called, multiplying that by the amount of numbers I still had to sit through, and adding that to the time of the most-recent call, I got ever-refined estimates for my departure.

One way to visualize the situation is to look at how my predicted departure time evolved throughout my wait. I’ll also add a horizontal bar showing what wound up being my true departure time.

![Predicted departures over time]({IMG_ROOT}/letting-go-queue-theory-at-the-dmv/naive-predictions.png)

By 10:45 I was reasonably sure I’d be out of there around 1:15. At 11:45, Lady Luck decided to stop toying with me and my estimates marched steadily downward until they collided with reality, right at 12:21.

Spending most of the day being off by about an hour in my estimate isn’t great. Maybe we can improve the prediction.

The first step to improving a model is understanding why it behaves as it does. Towards this end, let’s visualize the raw data. What numbers were called when?

![When were which numbers called?]({IMG_ROOT}/letting-go-queue-theory-at-the-dmv/numbers-called.png)

This plot confirms that the rate picked up around 11:45. (Notice how the steps come quicker, making the right-most portion of the curve look more steep than the rest.)

The point of averaging all the wait times together is to keep getting a better guess for what the remaining wait time will be. Naively, we tend to think "more data is better." But if the true gap between numbers is changing, including the oldest data points in our average could be counterproductive. This suggests an adage that is as true in data science as it is in life: Sometimes, it’s best to let go of the past

To understand how wait time evolved throughout the day, let’s look at how much time past before each new number was called. I’ll also add two ways to estimate the "true" wait time to this plot.

1. Simply average every wait time so-far observed. Call this the "Naive Average"
2. Average only the eight most recent data points. More snobbily, we call this "a one-sided simple rolling average with window size eight"

![Estimates of wait time over time]({IMG_ROOT}/letting-go-queue-theory-at-the-dmv/prediction-comparison.png)

Some interesting observations from this plot!

1. Both estimators are exactly equal until the ninth datapoint. This is a nice sanity check
2. The estimators are in close agreement until 11:45. Basically, until 11:45, the true average wait time does seem to have been reasonably constant. Note that the rolling average is jumpier though.
3. At 11:45, the 8 datapoint rolling average adjusts to the acceleration almost immediately, whereas the naive average trends sluggishly downwards. Let’s see what impact this has on prediction quality:

![Prediction quality by predictor type]({IMG_ROOT}/letting-go-queue-theory-at-the-dmv/prediction-comparison-full.png)

Much better! The rolling average "forgets" about that first major outlier, and so starts out more optimistic than the naive estimator. Longer wait times pull it back to basically agree with the naive estimator, but it learns from the 11:45 acceleration, and so it hones in on the true departure about 40 minutes sooner than the naive estimator.

Of course, there’s nothing magical about choosing eight data points. The longer the lookback window, the less sensitive the estimate is to outliers, but the less quickly the metric adapts to true changes in the underlying wait time. Shorter lookback windows will adapt to changes very quickly, at the expense of overreacting to outliers.

Choosing this window is a simple example of what’s called "tuning" a model. To find the optimal window, we could try all possible windows, and pick the one that causes the model to become as accurate as possible as early as possible.

Shrewd readers might point out that would be cheating–using knowledge of the end to improve "predictions" of the end. (Specifically, this is a form of data leakage) One way I might have assessed these different options in real time is to set arbitrary breaks in the data, have each model predict those breaks, and whichever one did best, trust its prediction until the next breakpoint.

I didn’t take it this far, though, because my laptop was dying (unrelated, poor decision) and I really wanted to make sure I recorded all the data points. So I was reduced to closing my laptop, waiting for a number to be called, adding the new data, and rerunning the naive model to get the newest prediction.

I suppose I could try and finish the truly predictive version, but here’s another prediction for you: I ain’t gonna. The only way it would be useful would be if I’m at that same DMV office in the near future, and speaking of "letting go of the past," this was an experience I am keen to let go.
