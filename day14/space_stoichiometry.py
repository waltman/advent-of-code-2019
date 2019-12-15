#!/usr/bin/env python3
from sys import argv
import pulp
from itertools import chain

def parse_line(line: str):
    input_string, output_string = line.split(" => ")

    def parse_pair(pair_string: str):
        quantity, name = pair_string.split()
        return name, int(quantity)

    outputs = parse_pair(output_string)
    inputs = tuple(map(parse_pair, input_string.split(", ")))
    return (outputs, inputs)


def parse_recipes(input_lines):
    recipes = {}

    for line in input_lines:
        outputs, inputs = parse_line(line)
        assert outputs[0] not in recipes
        recipes[outputs[0]] = (outputs[1], inputs)

    return recipes

filename = argv[1]
with open(filename) as f:
    input_lines = [line.strip() for line in f.readlines()]

recipes = {}
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        from_str, to_str = line.split(" => ")
        quant, name = to_str.split()
        inputs = from_str.split(", ")
        d = {}
        for i in inputs:
            q, n = i.split()
            d[n] = int(q)
        recipes[name] = (int(quant), d)

chemicals = {c: pulp.LpVariable(c, cat=pulp.LpInteger) for c in recipes}
chemicals["ORE"] = pulp.LpVariable("ORE", cat=pulp.LpInteger)
reactions = {c: pulp.LpVariable(f"reaction_{c}", cat=pulp.LpInteger) for c in recipes}
quantities_required = {c: [] for c in recipes}
quantities_required["ORE"] = []

constraints = []
for var in chain(chemicals.values(), reactions.values()):
    constraints.append(var >= 0)

for out_chemical, (quantity, inputs) in recipes.items():
    constraints.append(chemicals[out_chemical] == quantity * reactions[out_chemical])
    for chemical, quantity in inputs.items():
        quantities_required[chemical].append(reactions[out_chemical] * quantity)

for chemical, required in quantities_required.items():
    if not required:
        continue
    constraints.append(chemicals[chemical] >= pulp.lpSum(required))


# part 1
prob = pulp.LpProblem("day_14.1", pulp.LpMinimize)
for c in constraints:
    prob += c
prob += chemicals["ORE"]  # Minimize this
prob += chemicals["FUEL"] >= 1

prob.solve()
print(("Status:", pulp.LpStatus[prob.status]))
print('Part 1:', pulp.value(chemicals["ORE"]))

# part 2
prob = pulp.LpProblem("day_14.2", pulp.LpMaximize)
for c in constraints:
    prob += c
prob += chemicals["FUEL"]  # Maximize this
prob += chemicals["ORE"] == 1_000_000_000_000

prob.solve()
print(("Status:", pulp.LpStatus[prob.status]))
print('Part 2:', pulp.value(chemicals["FUEL"]))
