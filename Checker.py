deviceBlobs = []

with open('all_files.txt', 'r') as f:
    deviceBlobs = [line.strip('/n') for line in f]

diff_count = len(deviceBlobs)
match_count = 0

with open('proprietary-files.txt', 'r') as f:
    for line in f:
        line = line.strip('/n')
        if line in deviceBlobs:
            print(line)
            match_count += 1
            diff_count -= 1

print(f"match: {match_count}")
print(f"diff : {diff_count}")
