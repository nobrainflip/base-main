import random
import sys

import questionary
from loguru import logger
from questionary import Choice

from config import ACCOUNTS
from modules.nfts_2_me import mint_nft2me
from settings import RANDOM_WALLET, SLEEP_TO, SLEEP_FROM, QUANTITY_RUN_ACCOUNTS
from utils.helpers import get_run_accounts, update_run_accounts
from modules_settings import *


def get_module():
    result = questionary.select(
        "Select a method to get started",
        choices=[
            Choice("1) Make bridge to Base", bridge_base),
            Choice("2) Make bridge on Orbiter", bridge_orbiter),
            Choice("3) Mint free nft", mint_nft2me),
            Choice("4) Wrap ETH", wrap_eth),
            Choice("5) Unwrap ETH", unwrap_eth),
            Choice("6) Swap on Uniswap", swap_uniswap),
            Choice("7) Swap on Pancake", swap_pancake),
            Choice("8) Swap on WooFi", swap_woofi),
            Choice("9) Swap on BaseSwap", swap_baseswap),
            Choice("10) Swap on AlienSwap", swap_alienswap),
            Choice("11) Swap on Maverick", swap_maverick),
            Choice("12) Swap on Odos", swap_odos),
            Choice("13) Swap on 1inch", swap_inch),
            Choice("14) Swap on OpenOcean", swap_openocean),
            Choice("15) Swap on XYSwap", swap_xyswap),
            Choice("16) Bungee Refuel", bungee_refuel),
            Choice("17) Deposit Aave", deposit_aave),
            Choice("18) Withdraw Aave", withdraw_aave),
            Choice("19) Mint and Bridge Zerius NFT", mint_zerius),
            Choice("20) Send message L2Telegraph", send_message),
            Choice("21) Mint and bridge NFT L2Telegraph", bridge_nft),
            Choice("22) Create portfolio on Ray", create_portfolio),
            Choice("23) Create gnosis safe", create_safe),
            Choice("24) Swap tokens to ETH", swap_tokens),
            Choice("25) Use Multiswap", swap_multiswap),
            Choice("26) Use custom routes", custom_routes),
            Choice("27) Check transaction count", "tx_checker"),
            Choice("28) Exit", "exit"),
        ],
        qmark="⚙️",
        pointer="✅"
    ).ask()
    if result == "exit":
        sys.exit()
    return result


def get_wallets():
    wallets = [
        {
            "id": _id,
            "key": key,
        } for _id, key in enumerate(ACCOUNTS, start=1)
    ]

    return wallets


async def run_module(module, account_id, key, sleep_time, start_id):
    if start_id != 1:
        await asyncio.sleep(sleep_time)

    while True:
        run_accounts = get_run_accounts()

        if len(run_accounts["accounts"]) < QUANTITY_RUN_ACCOUNTS:
            update_run_accounts(account_id, "add")

            await module(account_id, key)

            update_run_accounts(account_id, "remove")

            break
        else:
            logger.info(f'Current run accounts: {len(run_accounts["accounts"])}')
            await asyncio.sleep(20)


async def main(module):
    wallets = get_wallets()

    tasks = []

    if RANDOM_WALLET:
        random.shuffle(wallets)

    sleep_time = random.randint(SLEEP_FROM, SLEEP_TO)

    for _, account in enumerate(wallets, start=1):
        tasks.append(asyncio.create_task(
            run_module(module, account["id"], account["key"], sleep_time, _)
        ))

        sleep_time += random.randint(SLEEP_FROM, SLEEP_TO)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    module = get_module()
    if module == "tx_checker":
        get_tx_count()
    else:
        asyncio.run(main(module))
