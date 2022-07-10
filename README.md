# eternl2cointracking

`eternl2cointracking` converts a Eternl Wallet csv file to the csv header format used by CoinTracking:

```bash
"Type", "Buy Amount", "Buy Currency", "Sell Amount", "Sell Currency", "Fee", "Fee Currency", "Exchange", "Trade-Group", "Comment", "Date"
```

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

```bash
                    Type  Buy Amount Buy Currency  Sell Amount Sell Currency  ...       Exchange Trade-Group                                       Comment                 Date                                              Tx-ID
0                Deposit   49.400000          ADA          NaN           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-02-09 09:28:53  ec103814b9ccb1e305ce20d6a25e681d3735d2301d5bb6...
1              Other Fee         NaN          ADA        2.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-02-09 09:38:46  a079d8358d3ac98d677f6cecd8cb2b408764eb48db7bdb...
2                Deposit  124.400000          ADA          NaN           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-02-13 08:05:14  f814c0c628e33c61136313108310de24854b5ca092e1be...
3              Other Fee         NaN          ADA        0.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-05-27 20:22:51  1faddee7abf6464ca9af8cd34315c15ab78b8e221d279a...
4              Other Fee         NaN          ADA        0.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-06-04 22:22:59  deeb2a18d0f080de19f75a3eb5e2d60b9d563411d0f717...
5             Withdrawal         NaN          ADA        1.314           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-06-05 06:37:45  99772ea457b2e73c156f30f655f0df9709e94282afd844...
6              Other Fee         NaN          ADA        0.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-07-09 06:58:31  252c4e6d7fac658030b7d50b17e78eca442e7a6327f7cd...
7              Other Fee         NaN          ADA        0.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-09-01 17:41:27  46b6004456774e8a9e507744751b57812223298a3336ae...
8                Deposit    1.281480          ADA          NaN           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-09-12 08:40:54  e9fa9496237fc419e5882ea77302b7cb8f659c78426425...
9                Deposit    1.144443          ADA          NaN           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-09-12 08:41:26  e434f19c80adc3a1fb88417b3c5cac93c099297be60c85...
10             Other Fee         NaN          ADA        0.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2021-11-28 11:48:29  3f8fef1f6904ed356b02f30d2a345c91242dc56bf10d93...
11             Other Fee         NaN          ADA        0.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2022-01-22 09:44:57  8f08a193962dcceb82f0e03035ea703480ed43f460b513...
12               Deposit   21.222222          ADA          NaN           ADA  ...  My ADA Wallet        Hodl                                           NaN  2022-01-25 08:44:13  b1d55664fdc47b5275bc092972156dca436b80bb0aab04...
13             Other Fee         NaN          ADA        0.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2022-02-09 20:57:10  9c0135a6c1819e5eacb53313e6ddc596a9a5f5ea9201e8...
14             Other Fee         NaN          ADA        0.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2022-02-14 23:12:43  91c0410db1cbcd5d8e601da08122cdcb0e7b1180f388f0...
15            Withdrawal         NaN          ADA        3.000           ADA  ...  My ADA Wallet        Hodl                                           NaN  2022-03-02 07:00:02  d59d5a2b9fc1a9366529fe8fc23b923b0352b376179908...
16               Deposit    1.244798          ADA          NaN           ADA  ...  My ADA Wallet        Hodl                                           NaN  2022-03-02 07:03:50  597a6a1dbf242bab42536b4e39b573add74ad00a3b217f...
17  Income (non taxable)    2.000000          ADA          NaN           ADA  ...  My ADA Wallet        Hodl                                           NaN  2022-06-14 22:04:55  49d79c33ec7dbc0a37de70f8602f2f363a9e7972008416...
18               Staking    1.622219          ADA          NaN           ADA  ...  My ADA Wallet        Hodl  reward - epoch: earned: 248 - spendable: 250  2021-02-24 22:44:52                                                NaN
19               Staking    3.045237          ADA          NaN           ADA  ...  My ADA Wallet        Hodl  reward - epoch: earned: 249 - spendable: 251  2021-03-01 22:44:52                                                NaN
20               Staking    2.217209          ADA          NaN           ADA  ...  My ADA Wallet        Hodl  reward - epoch: earned: 250 - spendable: 252  2021-03-06 22:44:52                                                NaN
21          Other Income    0.229180          ADA          NaN           ADA  ...  My ADA Wallet        Hodl             reward - treasury: spendable: 279  2021-07-19 23:44:52                                                NaN
```

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
