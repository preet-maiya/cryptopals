from collections import Counter


def get_counts(enc):
    blocks = [enc[i:i+32] for i in range(0, len(enc), 32)]
    return dict(Counter(blocks))

f = open('detect_aes_block', 'r')
blocks = f.read().split()
i=0
max_count = -1
block_no = 0
count_final = {}
for block in blocks:
    counts = get_counts(block)
    print(counts)
    for b, c in counts.items():
        if c>max_count:
            max_count = c
            block_no = i
            count_final = counts

    i+=1

print(block_no, max_count)
print(count_final)