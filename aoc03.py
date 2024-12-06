import re
#
# mul\((?<!\d)\d{1,3}(?!\d)\,(?<!\d)\d{1,3}(?!\d)\)
# mul\(\d{1,3}\,\d{1,3}\)

# part 1
def get_data():
    with open("aoc03-data.txt") as f:
        return f.read().splitlines()
    
def main():
    bigsum = 0

    data = get_data()

    for line in data:
        #print(line)
        match = re.findall("mul\(\d{1,3}\,\d{1,3}\)", line)
        clean = []
        for item in match:
            numbers = (re.findall("\d{1,3}", item))
            clean = list(map(int,numbers))
            #print(clean)
            bigsum = bigsum + (clean[0] * clean[1])
    print(bigsum)

if __name__ == "__main__":
    main()