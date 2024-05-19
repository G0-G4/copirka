import re

def find_first_number_index(input_string):
    match = re.search(r'\d', input_string) 
    if match:
        return match.start() 
    else:
        return -1

old = set()
new = set() 
new_nv = dict()
old_nv = dict()
old_path = ''
new_path = ''

for lib in new:
    i = find_first_number_index(lib)
    new_nv[lib[:i]] = lib[i:]

for lib in old:
    i = find_first_number_index(lib)
    old_nv[lib[:i]] = lib[i:]

instructions = []
i = 0

for name in sorted((set(new_nv.keys()) | set(old_nv.keys()))):
    if name in new_nv and name in old_nv and new_nv[name] != old_nv[name]:
        instructions.append(f'обновить {name}{old_nv[name]} до {name}{new_nv[name]}')
        i += 1
        # print(f'обновить {name}{old_nv[name]} до {name}{new_nv[name]}')
        # print(f'rm {old_path}/{name}{old_nv[name]}')
        # print(f'cp {new_path}/{name}{new_nv[name]} {old_path}/')
    if name in new_nv and name not in old_nv:
        instructions.append(f'добавить {name}{new_nv[name]}')
        i += 1
        # print(f'добавить {name}{new_nv[name]}')
        # print(f'cp {new_path}/{name}{new_nv[name]} {old_path}/')
    if name in old_nv and name not in new_nv:
        instructions.append(f'удалить {name}{old_nv[name]}')
        # print(f'удалить {name}{old_nv[name]}')
        # print(f'rm {old_path}/{name}{old_nv[name]}')

print(*sorted(instructions), sep='\n')
print(i)
