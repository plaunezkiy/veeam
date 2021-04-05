import argparse
import hashlib
import os


algorithms = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
}


parser = argparse.ArgumentParser(description='Hash calculator/verifier')
parser.add_argument('file', type=str,
                    help='path to the file containing sums and filenames')
parser.add_argument('dir', type=str,
                    help='path to the directory containing files')
args = parser.parse_args()


try:
    with open(args.file, 'r') as sums_file:
        for line in sums_file:
            file_name, algorithm, hash_sum = line.strip().split()
            try:
                with open(os.path.join(args.dir, file_name), 'rb') as file:
                    status = 'FAIL'
                    calculated_hash = algorithms[algorithm](file.read())
                    if calculated_hash.hexdigest() == hash_sum:
                        status = 'OK'
                    print(f'{file_name} {status}')
            except FileNotFoundError:
                print(f'{file_name} NOT FOUND')
except FileNotFoundError:
    print(f'{args.file} NOT FOUND')
