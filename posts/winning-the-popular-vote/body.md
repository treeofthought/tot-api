Twice in the last five elections, the winner of the electoral college—and therefore the presidency—did not collect the most popular votes.

As I write this, Clinton's popular vote lead has been tallied to about 2.6 Million. But this also means that only 48% of the votes went to Clinton. Granted, this is more than Trump's 46%, but it's not as if most of the voters picked Clinton. Even that wouldn't be unprecedented: the worst actual discrepancy in history came in 1824, when Andrew Jackson won 57% of the popular vote and still lost to John Quincy Adams (source).

This year's result has raised questions about the purpose and effectiveness of the electoral college, questions to which I don't have answers.

It does raise one question, however, that I may be qualified to answer. I started wondering: "What's the largest percentage of the popular vote a candidate could win and still go on to lose the presidency?"

Another way to think about this is "What situation maximizes a candidate's popular votes but gives them less than the 270 electoral votes necessary to win the presidency?"

Intuitively, we can see that popular votes are maximized if a candidate takes 100% of the popular votes in a state they win and as close as possible to 50% of the popular votes in a state they lose. With this in mind, we need only find the most populous group of states whose electoral college votes add up to 268 or less.

As is often the case, this obscure problem is actually a classic computer science problem in disguise. In this case, it is the knapsack problem. Pretend you have a knapsack which can only hold ten pounds. You have a pile of items of varying weights and values. What should you put in the pack to maximize the value you carry without going over the ten pound limit?

For our purposes, the "weight" of a state is its electoral votes, and the "value" is its popular votes. The limit of our knapsack is 268. The solution is fairly simple to code. I adapted mine from these lecture notes. Essentially, we build a matrix of the maximum possible values of progressively more of the objects for progressively bigger knapsacks. By keeping track of these solutions to subproblems, we are able to solve the big problem.

In picking the data to feed my code, I decided to use the number of actual votes cast–rather than the number of actual voters—to determine the popular votes available in each state. Assuming turnout rates don't vary too much from state-to-state, this shouldn't change the answer considerably.

Louisiana, Maryland, Massachusetts, Michigan, Minnesota, Missouri, New Jersey, North Carolina, Ohio, Oregon, Pennsylvania, Virginia, Washington, Wisconsin are the "optimal" subset of states. They had 77,936,283 popular votes cast and account for 268 electoral votes.

The remaining 31 states (counting D.C.) account for the winning 270 electoral votes and had 58,057,139 votes cast. 29,028,546 of these votes could be cast for our hypothetical loser without changing the outcome in the electoral college. If you are a voter in these states, congratulations! You are a member of the smallest group of people that could possibly select a president. Talk about power.

In total, this situation would be a popular vote disparity of 106,964,829 to 29,028,593. This means a candidate could have conceivably won 79% of the popular vote and still not become president!

Of course, the probability of this occurring is nearly zero (but it is possible!). It's more mathematical quirk than flaw in the U.S. constitution. And if we're talking about astronomically improbable outcomes that are still technically possible, I should mention it is possible to win 100% of the popular vote and lose the election thanks to faithless electors…but to discuss that would be to leave math and computer science and return to discussing the relevance of the electoral college.
