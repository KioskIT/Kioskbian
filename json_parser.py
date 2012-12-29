import json
import sys


def main(argv):

	json_data = json.load(open('kiosk_parameters'));

	print(json_data[argv[0]])


main(sys.argv[1:])
