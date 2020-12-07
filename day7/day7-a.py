bags = {}


def get_bag_definition(_line):
    components = _line.split(' contain ')
    return components[0].replace(' bags', '')


def get_contain_definition(_line):
    components = _line.split(' contain ')
    return components[1].replace(' bags', '').replace(' bag', '')


def get_gold_amount(_contain):
    num = _contain[0]
    rest = _contain[1:].strip().replace('.', '')

    if not num.isdigit():
        return 0

    if rest == 'shiny gold':
        return int(num)
    else:
        _bag = bags[rest]
        _contain_components = _bag.split(',')
        _gold_sum = 0
        for _contain_component in _contain_components:
            _gold_sum += int(num) * get_gold_amount(_contain_component.strip())
        return _gold_sum


with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    for line in lines:
        bag_definition = get_bag_definition(line)
        contain_definition = get_contain_definition(line)
        bags[bag_definition] = contain_definition

    count_gold = 0
    for bag, contain in bags.items():
        contain_components = contain.split(',')
        gold_sum = 0
        for contain_component in contain_components:
            gold_sum += get_gold_amount(contain_component.strip())
        if gold_sum > 0:
            count_gold += 1
    print(count_gold)
