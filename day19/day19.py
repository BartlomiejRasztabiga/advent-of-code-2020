from collections import namedtuple

Rule = namedtuple("Rule", "val opts")
rule_text, messages = [x.splitlines() for x in open("input.txt").read().split("\n\n")]


def parse_rules(rule_text):
    rules = {}
    for line in rule_text:
        n, opts = line.split(": ")
        n = int(n)
        if '"' in opts:
            rules[n] = Rule(opts[1], None)
        else:
            rules[n] = Rule(None, [[int(r) for r in opt.split()] for opt in opts.split("|")])
    return rules


def test(message, rules, r):
    if rules[r].val:
        return {1, } if (message and message[0] == rules[r].val) else set()
    else:
        overall_matches = set()
        for opt in rules[r].opts:
            opt_match = {0, }
            for rule in opt:
                new_match = set()
                for n in opt_match:
                    new_match |= {n + m for m in test(message[n:], rules, rule)}
                opt_match = new_match
            overall_matches |= opt_match
        return overall_matches


rules = parse_rules(rule_text)
print("Part 1:", sum(len(m) in test(m, rules, 0) for m in messages))

rule_text += ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]

rules = parse_rules(rule_text)
print("Part 2:", sum(len(m) in test(m, rules, 0) for m in messages))
