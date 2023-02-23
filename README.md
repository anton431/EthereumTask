# Backend service that performs operations with an NFT token


## Stack

>Language: __Python 3__<br>
Web framework: __Django & DRF__<br>
Database: __SQLite__<br>
Blockchain framework: __Web3.py__<br>
Blockchain: __Ethereum (TESTNET  Goerli)__<br>

Optional requirements:<br>
- Docker Desctop<br>
- Swagger

## API Views

><p>/tokens/create — this API creates a new unique token on the blockchain
>and writes the request parameters to the database;<br></p>
><p>/tokens/list — this API returns a list of all 
>objects of the Token model;<br></p>
><p>/tokens/total_supply — this API
>gives information about the current total number of tokens in the network.<br></p>

## Private information

>Private information is in the .env:<br>
>>API_Key — you infura provider key;<br>
PRIVATE_KEY — your metamask key;<br>
SECRET_KEY — django key;<br>
owner — contract address.<br>
