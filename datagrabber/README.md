Figures out search urls for sites.

Uses pyppeteer to select the first input[type=text], types the canary "CANADIAN SLUT FUCKED HARD", then simulates a form submission by pressing enter.

produces a tabbed list file of sites and the query urls. The "CANADIAN SLUT FUCKED HARD" canary should provide info on both handling of spaces and capitals, aiding in developing a universal search api.

should be able to be used with the list in ../porntubehomepages like so:

`$ python grabdatas.py ../porntubehomepages/porntubesites.txt | tee porntubesearchqueries.txt`

expect lots of tracebacks on sites that are down. I don't care enough to filter them. ignore them, i did. it's fun.

Output of my run is in porntubesearchqueries.txt.


probably dupes in the list but that's later me's problem.
