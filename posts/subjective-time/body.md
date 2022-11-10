It's alarming how each new year seems to go faster than the year before.

It makes a certain grim sense. Each year you live, you have that much of a longer memory with which to compare the next year you'll live. The day you're living now is–proportionally speaking–a smaller chunk of your life than was every day you've lived before. None of your tomorrows will ever seem to last as long as yesterday.

While talking about this with my friend Tommy, we realized this might mean we have less time left than we think. If you live to 80 years, the obvious halfway point of your life is 40 years. But time for a 40 year old seems to go much faster than it does for a 10 year old. This means those second 40 years seem to go by much faster, so 40 must be after the midway point.

Is it possible to pin down the "true" halfway point?

One way to model this situation is the harmonic series. Let your first year count as one subjective year. The second year would be half your life experience, so it would seem to take half as long as the first subjective year. After your third year, you have the three to compare it to, so that year accounts of one third of your life experience, and so on. After n years then, you've subjectively lived:

![Harmonic series model of subjective time]({IMG_ROOT}/subjective-time/harmonic-series.png)

There's a few flaws with this model.  For one thing, there's nothing special about the year boundary.  This is happening on the scale of days, or seconds.  We could adjust the formula accordingly by taking smaller and smaller slices.  Push this idea, and we'll accidentally invent differential calculus.

To model it continuously then, a simple differential equation:

![Simple differential equation for subjective time]({IMG_ROOT}/subjective-time/diff-eq.png)

What this formula says is "the subjective length of each new instant is diluted proportional to the amount of time you've been alive up to that instant"

I'll relegate the solution to an appendix.  This way readers who just want to read about the horrors of getting older can do so without reliving the horrors of Calc I.

One calculus-free observation is that this model "blows up" at T=0. The instant we are born, we have nothing to compare our experience to–that first instant would seem to take forever.

A sanity check saves us–memory doesn't quite work that way.  I have fuzzy flashes of being two years old, but I can't trace the line of my life with much certainty until the age of five.  So let's say we start to experience time at T=5 years.

This also means that we can no longer use "years" as a specific measure during this conversation.  If you agree that time seems to speed up as we get older, then  "20 years" apparently has different meaning if I'm talking about ages 5-25 versus 25-45. Let's talk in ratios of intervals instead, since that will capture the idea we're after; not all stretches of time are equal.

Armed with this formula, we can start making quantifying statements about the slippage of time.

* Four years of college goes by 25% faster than high school</li>
* The four years after college goes by 50% faster than high school
* Assuming you live to be 80, you've lived half your subjective life by age 20!

At the time of writing I'm 26.63 years old.  If I'm lucky enough to see 80, then I've already lived 60% of my subjective life. OOF.

This also sheds some light on why parents are saying their children "grow up so fast.""  In the time I grew from 5 to 18, my parents grew from about 35 to 53. According to my formula, they experienced this stretch of time three times faster than I did!

Here's a visualization that shows how much of your life you've lived at each age, measured both by this subjective proportional formula, and also the objective way of current age / max age.

![Conversion between obejctive and subjective time curve]({IMG_ROOT}/subjective-time/line-chart.png)

There's a pleasing symmetry to the quartiles.  Ages 5-10 seem to take a 25% of you life, ages 10-20 the next 25%, 20-40 the third 25%, and 40-80 the final portion.

The last forty years of your life will blink by as quickly as it took you to turn 10.  This is a little bit hard to stomach, but I think I'm better off for knowing it. Time is precious! Let's make the most of it.

## Calculus Appendix

Recall the differential equation

![The differential equation from before]({IMG_ROOT}/subjective-time/diff-eq.png)

We can integrate with separation of variables to get

![Differential solved via separation of variables]({IMG_ROOT}/subjective-time/antiderivative.png)

Logarithms do strange things to units, so we need a dimensionless quantity inside our logarithm.

If you buy my "time starts at T=5 years" argument, our formula is

![Specific solution given my boundary condition]({IMG_ROOT}/subjective-time/definite-integral.png)

Logarithm rules let us rewrite this as

![An algebraic re-expression of the above image]({IMG_ROOT}/subjective-time/solution.png)

Since T has units "years" and 5 has units "years," we are taking the logarithm of a dimensionless quantity, and we are saved.  A consequence is that the value we get for "S" has no interpretation by itself, but we can interpret ratios involving it.

It's easy now to reconstruct the calculations I did to make the points in the article.

Length of childhood is ln(18/5) = 1.281.  To find the age after 18 where we've lived the same amount of time, we seek x such that

![Solution constraint to childhood equation]({IMG_ROOT}/subjective-time/childhood-equation.png)

Pleasingly, we just need the logarithm arguments to be equal, and so the solution is quite simply

![Solution constraint to childhood equation]({IMG_ROOT}/subjective-time/childhood-solution.png)

To find the halfway point of subjective life, we need to solve the equation

![Halfway equation]({IMG_ROOT}/subjective-time/halfway-equation.png)

Which works out to x = 20 years.

