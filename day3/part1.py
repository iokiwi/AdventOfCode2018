import re
from collections import defaultdict


def read_input():
    i = input()
    values = []
    while(i):
        try: 
            values.append(i)
            i = input()
        except EOFError:
            return values


class Claim(object):
    pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    def __init__(self, row):
        m = self.pattern.match(row)
        if not m:
            raise "Syntax error" + row
        self.id, self.x, self.y, self.width, self.height = map(int, m.groups())

    def __str__(self):
        s = "Claim(id: {}, x: {}, y: {}, width: {}, height: {})"
        return s.format(self.id, self.x, self.y, self.width, self.height)

    def __repr__(self):
        return str(self)


def count_overlapping_claim_area(claim_map):
    return len([x for x in claim_map.values() if len(x) > 1])


def map_claims(claim_list):
    claim_map = defaultdict(list)
    for claim in claim_list:
        for x in range(claim.x, claim.x + claim.width):
            for y in range(claim.y, claim.y + claim.height):
                claim_map[(x, y)].append(claim.id)
    return claim_map


def main(): 
    values = read_input()
    claim_list = [Claim(s) for s in values]
    claim_map = map_claims(claim_list)
    print(count_overlapping_claim_area(claim_map))

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()