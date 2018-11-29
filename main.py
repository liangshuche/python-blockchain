from argparse import ArgumentParser
from blockchain import Blockchain
from utils import DB

parser = ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

parser_addblock = subparsers.add_parser('addblock')
parser_addblock.add_argument('-transactions')

parser_printchain = subparsers.add_parser('printchain')

parser_printblock = subparsers.add_parser('printblock')
parser_printblock.add_argument('-height', type=int)

parser_resetdb = subparsers.add_parser('resetdb')

args = parser.parse_args()

bc = Blockchain()

if (args.command == 'addblock'):
    bc.add_block(args.transactions)
elif (args.command == 'printchain'):
    bc.print_chain()
elif (args.command == 'printblock'):
    bc.print_block(args.height)
elif (args.command == 'resetdb'):
    DB().reset()
else:
    parser.print_help()
