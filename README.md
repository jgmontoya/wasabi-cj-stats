# Wasabi CoinJoin Stats

* `explorer.py`: Handles the requests to get relevant transaction data
* `stats.py`: Compute the per-round statistics. Currently it computes: min, max, mean, median, stdev and mode (if mode is not well defined it is set to -1)
* `Analysis.ipynb`: Here we can see the aggregated stats over the multiple rounds and some plots.