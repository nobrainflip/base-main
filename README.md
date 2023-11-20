<h1 align="center">Base Soft</h1>

---
<h2>How to run the Software</h2>


git clone https://github.com/nobrainflip/base-main

cd base

pip install -r requirements.txt

python main.py

---
<h2>Software Features</h2>

1. Deposit and withdraw ETH through the official bridge.

2. Bridge through Orbiter.

3. Wrap/unwrap ETH.

4. Swaps through Uniswap, PancakeSwap, Woofi, Baseswap, AlienSwap, Maverick, Odos, 1inch, Xy.Finance, OpenOcean (referral included for aggregators, 1% of the transaction amount goes to the developer, comes from the aggregator's contract, can be disabled in the config).

5. Bungee Refuel.

6. Aave (deposit/withdraw).

7. Mint free NFT on Mint.Fun (works with the "mint" contract function, other functions won't work, check Rabby or an explorer for details).

8. Mint + Bridge NFT through L2Telegraph (only in arb nova).

9. Send messages through L2Telegraph (only in arb nova).

10. Dump tokens to ETH.

11. Multi-swap capability - performs the specified number of exchanges on the specified DEXs.

12. Custom routes - actions that will be executed sequentially or in random order.

13. Transaction count checker.

---
<h2>Configuration</h2>

1. All main settings are done in the settings.py file, which contains information on what and where to edit.

2. In the accounts.txt file, specify your private keys.

3. In the rpc.json file located at data/rpc.json, you can change the RPC settings to your own.

Built by @czbag

Base 🫸🏻