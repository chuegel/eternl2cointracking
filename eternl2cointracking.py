import pandas as pd
import argparse
import hashlib


# Create the parser and add arguments
parser = argparse.ArgumentParser()

parser.add_argument('-f', '--filename', required=True, help="specify the Eternl CSV file to import")
parser.add_argument('-e', '--exchange', required=False, help="specify the exchange or wallet")
parser.add_argument('-g', '--group', required=False, help="specify the Trading-Group")

# Parse and print the results
args = parser.parse_args()

filename = (args.filename)
exchange = (args.exchange)
group = (args.group)

new_filename = 'new_' + filename

# DO NOT EDIT BELOW
################

# rename columns to match Cointracking names
col_names = ['Date',
             'Sell Amount',
             'Sell Currency',
             'Buy Amount',
             'Buy Currency',
             'Fee',
             'Fee Currency',
             'Label',
             'Comment',
             'Tx-ID',
             'Type']

df = pd.read_csv(filename, sep=',',names=col_names, skiprows=[0])

# add Exchange and Trade-Group column with args
df['Exchange'] = exchange 
df['Trade-Group'] = group

# re-arrange positions of columns
df = df[['Type','Buy Amount','Buy Currency','Sell Amount','Sell Currency','Fee','Fee Currency','Exchange','Trade-Group','Comment','Date','Tx-ID']]
#df = df[['Type','Buy Amount','Buy Currency','Sell Amount','Sell Currency','Fee','Fee Currency','Exchange','Trade-Group','Comment','Date']]

# set Type to "Staking" for staking rewards
stake = (df['Comment'].astype(str).str.contains('reward - epoch', na=False)) 
df.loc[stake, 'Type'] = 'Staking'

# Eternl wallet does not export staking rewards with a Tx-ID. 
# In order to detect duplicates when importing into CoinTracking, we must generate a TX-Id from the Comment column.

# Convert column to string
df['Buy Amount'] = df['Buy Amount'].astype(str)
# Apply hashing function to the column
hash =  df['Buy Amount'].apply(
    lambda x: 
        hashlib.sha256(x.encode()).hexdigest()
)

df.fillna({'Tx-ID':hash}, inplace=True)

# set Type to Other Income for Catalyst Voting rewards
catalyst = (df['Comment'].astype(str).str.contains('reward - treasury', na=False))
df.loc[catalyst, 'Type'] = 'Other Income'


# match Withdrawal types 
withdraw = (df['Type'].astype(str).str.contains('Sent Funds', na=False))  
df.loc[withdraw, 'Type'] = 'Withdrawal'

# match other fees 
other_fee = (df['Type'].astype(str).str.fullmatch('Internal Transfer - Deposit', na=False)) | (df['Type'].astype(str).str.fullmatch('Internal Transfer', na=False))
df.loc[other_fee, 'Type'] = 'Other Fee'

# match Deposit types 
received = (df['Type'].astype(str).str.contains('Received Funds', na=False)) 
df.loc[received, 'Type'] = 'Deposit'

# match staking de-registration deposit
deposit = (df['Type'].astype(str).str.fullmatch('Internal Transfer - Deposit - Withdrawal', na=False)) 
df.loc[deposit, 'Type'] = 'Income (non taxable)'

# print output and write new file
print(df) 
df.to_csv(new_filename, index=False, sep=',')

