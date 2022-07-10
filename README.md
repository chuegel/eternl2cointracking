# eternl2cointracking

`eternl2cointracking` converts a Eternl Wallet CSV file to a CoinTracking

## Requirements

* python 3.x
* pandas

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas.

```bash
pip install pandas
```

## Usage

```python
usage: eternl2cointracking.py [-h] -f FILENAME [-e EXCHANGE] [-g GROUP]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        specify the Eternl CSV file to import
  -e EXCHANGE, --exchange EXCHANGE
                        specify the exchange or wallet name
  -g GROUP, --group GROUP
                        specify the Trading-Group
```

Example:

```bash
python eternl2cointracking.py -f sample_eternl.csv -e "My ADA Wallet" -g Hodl
```

This generates a `new_sample_eternl.csv` file in the working directory.
Please see the [Known Issues](#Known-Issues)

## Mapping of Transaction Types

| Eternl Wallet                               | CoinTracking              |
|---------------------------------------------|:-------------------------:|
| reward [1]                                  | Stacking                  |
| reward - treasury [2]                       | Other Income              |
| Sent Funds                                  | Withdrawal                |
| Internal Transfer - Deposit [3]             | Other Fee                 |
| Internal Transfer [4]                       | Other Fee                 |
| Received Funds                              | Deposit                   |
| Internal Transfer - Deposit - Withdrawal [5]| Income (non taxable)      |

  [1] Staking rewards do not have any transaction type when exported via Eternl Wallet but are mentioned in the `Comment` column.  
      This information is used to update the transaction type to `Staking`  
  [2] Catalyst Voting rewards. Since this is a taxable event, the type is set to `Other Income`  
  [3] Registration deposit of your wallet to a staking pool  
  [4] Delegation fee to a staking pool, Catalyst Voting Registration fee etc.  
  [5] De-registration of your wallet from a staking pool. This amount is the deposit you made in [3] minus transaction fees. Not taxable event  

## Known Issues

The last row of the generated file is blank. This prevents a proper inmport into CoinTracking.
Please use an editor to delete it.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
