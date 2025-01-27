

def towers_of_hanoi():
    initial_state = {'A': [3, 2, 1], 'B': [], 'C': []}

    current = []

    while (len(initial_state["A"]) and len(initial_state["B"])) == 0:

        if len(initial_state['C']) == 0:
            current = initial_state['A'][-1]
            initial_state['A'].remove(initial_state['A'][-1])
            initial_state['C'].append(current)
            current = []  # {'A': [3, 2], 'B': [], 'C': [1]}

        if len(initial_state['B']) == 0:
            current = initial_state['A'][-1]
            initial_state['A'].remove(initial_state['A'][-1])
            initial_state['B'].append(current)
            current = []  # {'A': [3], 'B': [2], 'C': [1]}

        if (len(initial_state['B']) == 1 and len(initial_state['C'])) == 1:
            current = initial_state['C'][-1]
            initial_state['C'].remove(initial_state['C'][-1])
            initial_state['B'].append(current)
            current = []  # {'A': [3], 'B': [2, 1], 'C': []}

        if len(initial_state['B']) == 2 and len(initial_state['C']) == 0:
            current = initial_state['A'][0]
            initial_state['A'].remove(initial_state['A'][0])
            initial_state['C'].append(current)
            current = []  # {'A': [], 'B': [2, 1], 'C': [3]}

        if len(initial_state['A']) == 0 and len(initial_state['B']) == 2:
            current = initial_state['B'][0]
            initial_state['B'].remove(initial_state['B'][0])
            initial_state['C'].append(current)
            current = []

        if len(initial_state['B']) == 1:
            current = initial_state['B'][0]
            initial_state['B'].remove(initial_state['B'][0])
            initial_state['C'].append(current)
            current = []  # {'A': [], 'B': [], 'C': [3, 2, 1]}
            break
    return initial_state


if __name__ == "__main__":
    print(towers_of_hanoi())
