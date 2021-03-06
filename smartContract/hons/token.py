"""
Basic settings for an NEP5 Token and crowdsale
"""

from boa.interop.Neo.Storage import *

TOKEN_NAME = 'Hasty Ogre Name Service Token'

TOKEN_SYMBOL = 'HONS'

TOKEN_DECIMALS = 8

# This is the script hash of the address for the owner of the token
# This can be found in ``neo-python`` with the walet open, use ``wallet`` command
TOKEN_OWNER = b'h\xf3\x90\xdev0\xad\x98\x86 \xa1=\xd9p\xf6n\xdfiH\x98'

TOKEN_CIRC_KEY = b'in_circulation'

TOKEN_TOTAL_SUPPLY = 100_000_000 * 100_000_000  # 100m total supply * 10^8 ( decimals)

TOKEN_INITIAL_AMOUNT = 3_000_000 * 100_000_000  # 3m to owners * 10^8

# for now assume 1 dollar per token, and one neo = 40 dollars * 10^8
TOKENS_PER_NEO = 400 * 100_000_000

# for now assume 1 dollar per token, and one gas = 20 dollars * 10^8
TOKENS_PER_GAS = 200 * 100_000_000

# maximum amount you can mint in the limited round ( 500 neo/person * 40 Tokens/NEO * 10^8 )
MAX_EXCHANGE_LIMITED_ROUND = 500 * 40 * 100_000_000

# when to start the crowdsale
BLOCK_SALE_START = 10

# when to end the initial limited round
LIMITED_ROUND_END = 999_999_999_999

KYC_KEY = b'kyc_ok'

LIMITED_ROUND_KEY = b'r1'


def crowdsale_available_amount(ctx):
    """

    :return: int The amount of tokens left for sale in the crowdsale
    """

    in_circ = Get(ctx, TOKEN_CIRC_KEY)

    available = TOKEN_TOTAL_SUPPLY - in_circ

    return available


def add_to_circulation(ctx, amount):
    """
    Adds an amount of token to circlulation

    :param amount: int the amount to add to circulation
    """

    current_supply = Get(ctx, TOKEN_CIRC_KEY)

    current_supply += amount
    Put(ctx, TOKEN_CIRC_KEY, current_supply)
    return True


def get_circulation(ctx):
    """
    Get the total amount of tokens in circulation

    :return:
        int: Total amount in circulation
    """
    return Get(ctx, TOKEN_CIRC_KEY)
