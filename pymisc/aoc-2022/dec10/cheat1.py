import collections
import pprint

with open('crap.txt') as f:
    lines = f.read().split('\n')

monkeys = {
}

i_monkey = 0
cnt = collections.Counter()

mult = 1


for line in lines:
    if 'Monkey' in line:
        i_monkey = int(line.split()[1].strip(':'))
        monkeys[i_monkey] = [[], None, None, [None, None, None]]
    elif 'Starting items' in line:
        monkeys[i_monkey][0] = [int(x.strip(',')) for x in line.strip().split()[2:]]
    elif 'Test' in line:
        monkeys[i_monkey][3][0] = int(line.split()[-1])
        mult *= monkeys[i_monkey][3][0]
    elif 'If true:' in line:
        monkeys[i_monkey][3][1] = int(line.split()[-1])
    elif 'If false:' in line:
        monkeys[i_monkey][3][2] = int(line.split()[-1])
    elif 'Operation' in line:
        monkeys[i_monkey][1] = line.split('=')[1]
    elif line.strip():
        print(line)
        raise AssertionError()

N = 10000

print(mult)


for rnt in range(N):
    print(rnt)
    for i_monkey in range(len(monkeys)):
        monkey = monkeys[i_monkey]
        for item in monkey[0]:
            cnt[i_monkey] += 1
            expr = monkey[1]
            wl = eval(expr, {'old': item})
            wl %= mult
            if wl % monkey[3][0] == 0:
                who = monkey[3][1]
            else:
                who = monkey[3][2]
            # print(item, wl, 'to', who)
            monkeys[who][0].append(wl)
        del monkey[0][:]
    # for i_monkey in range(len(monkeys)):
    #     print(i_monkey, monkeys[i_monkey][0])

vals = sorted(cnt.values())

print(vals[-1] * vals[-2])
