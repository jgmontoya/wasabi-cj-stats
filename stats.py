from explorer import Explorer
from statistics import mean, median, mode, pstdev, StatisticsError
import pickle
from tqdm import tqdm


def get_summary_stats(values):
    summary = {}
    summary['min'] = min(values)
    summary['max'] = max(values)
    summary['mean'] = round(mean(values))
    summary['median'] = round(median(values))
    summary['stdev'] = round(pstdev(values), 2)
    try:
        summary['mode'] = mode(values)
    except StatisticsError:  # There is not exactly one most common value
        summary['mode'] = -1
    return summary


if __name__ == '__main__':
    stats = []
    explorer = Explorer()

    with open('WasabiCoinJoins.txt', 'r') as f:
        txids = [line.strip() for line in f]

    for txid in tqdm(txids):
        input_values = explorer.amounts_from_txid(txid)
        stats.append(get_summary_stats(input_values))

    with open('wasabi_cj_stats.pkl', 'wb') as f:
        pickle.dump(stats, f)
