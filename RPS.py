import random
import numpy as np

MARKOV_CHAIN_LENGTH = 5

counter_moves = ['P', 'R', 'S']
move_index_map = {'R': 0, 'S': 1, 'P': 2}

def get_next_move_prediction(transition_tally, recent_plays):
    if len(recent_plays) != MARKOV_CHAIN_LENGTH - 1:
        raise ValueError("recent_plays must have a length equal to MARKOV_CHAIN_LENGTH - 1")

    current_tally = transition_tally
    for play in recent_plays:
        current_tally = current_tally[play]

    return max(range(len(current_tally)), key=current_tally.__getitem__)

def increment_transition_tally(transition_tally, recent_plays):
    if len(recent_plays) != MARKOV_CHAIN_LENGTH:
        raise ValueError("recent_plays must have a length equal to MARKOV_CHAIN_LENGTH")

    current_tally = transition_tally
    for play in recent_plays[:-1]:
        current_tally = current_tally[play]

    current_tally[recent_plays[-1]] += 1

# My solution
def player(
        prev_play,
        opponent_history=[],
        transition_tally=[]):

    if (len(opponent_history) >= 1000 or len(transition_tally) == 0):
        # Between players, reset the history and tally so future games aren't impacted by previous player's history
        opponent_history.clear()
        transition_tally.clear()
        transition_tally += np.zeros([3] * MARKOV_CHAIN_LENGTH).tolist()

    if prev_play:
        opponent_history.append(move_index_map[prev_play])

    if (len(opponent_history) < MARKOV_CHAIN_LENGTH) or not prev_play:
        return 'P'

    recent_plays = opponent_history[-MARKOV_CHAIN_LENGTH:]

    increment_transition_tally(transition_tally, recent_plays)
    prediction = get_next_move_prediction(transition_tally, recent_plays[1:])

    return counter_moves[prediction]