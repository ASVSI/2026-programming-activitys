# Backend
## install foundry
```shell
curl -L https://foundry.paradigm.xyz | bash
```
## To initialize an foundry application
```shell
forge init
```
## initialize an foundry project without git
```shell
forge init --no-git
```
## remove .git folder form the repo
```shell
rm -rf .git
```
## compile solidity smart contract
```shell
forge build
```
## Test the smart contract
```shell
forge test
```
## Get the total test coverage of the smart contract
```shell
forge coverage
```
## get all the functional gas report
```shell
forge snapshort
```
## Deploy smart contract to local anvil testnet
```shell
forge script script/Counter.s.sol 
```
## Deploy smart contract to other Networks
```shell
forge script script/Counter.s.sol 
```