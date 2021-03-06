# import random
import copy
import numpy as np
from Tictactoe_Env import tictactoe
from Agent import AIagent_RL, AIagent_Base
from Functions import encode, available_actions

learning_rate = 0.4
train_episode1 = 350
train_episode2 = 150
verify_episode = 100
total_episode = (train_episode1 + train_episode2) * 100000
epsilon = 0.08
# epsilon_list = [0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2]

env = tictactoe()
agent = AIagent_RL(restore=True)
agent_base = AIagent_Base()


def update(agent, state, next_state, learning_rate=0.4):
    state = encode(state)
    next_state = encode(next_state)
    agent.value[state] = agent.value[state] + learning_rate * (agent.value[next_state] - agent.value[state])


def train():
    win_rate_list = []
    win_rate_mean = []

    episode = 0
    while True:  # episode < total_episode:

        # epsilon = random.choice(epsilon_list)

        # training stage1 (self-training)
        for _ in range(train_episode1):
            episode += 1
            done = 0
            env.reset()
            state = copy.copy(env.state)

            while not done:
                turn = copy.copy(env.turn)
                action = agent.policy(state, turn, available_actions(state), epsilon=epsilon)
                next_state, done, winner = env.step(action)
                update(agent, state, next_state, learning_rate=learning_rate)
                state = copy.copy(next_state)

        # training stage2 (vs agent_base)
        for i in range(train_episode2):
            episode += 1
            done = 0
            env.reset()
            state = copy.copy(env.state)

            j = 0
            while not done:
                j += 1
                turn = copy.copy(env.turn)
                if (i + j) % 2 == 1:
                    action = agent.policy(state, turn, available_actions(state), epsilon=epsilon)
                else:
                    action = agent_base.policy(state, turn, available_actions(state))
                next_state, done, winner = env.step(action)
                if done:
                    update(agent, state, next_state, learning_rate=learning_rate)
                state = copy.copy(next_state)

        # verification stage
        win = lose = draw = 0
        for i in range(verify_episode):
            done = 0
            env.reset()
            state = copy.copy(env.state)

            j = 0
            while not done:
                j += 1
                turn = copy.copy(env.turn)
                if (i + j) % 2 == 1:
                    # epsilon 0
                    action = agent.policy(state, turn, available_actions(state), epsilon=0)
                else:
                    action = agent_base.policy(state, turn, available_actions(state))
                next_state, done, winner = env.step(action)
                state = copy.copy(next_state)

            if winner == 0:
                draw += 1
            elif (i + j) % 2 == 1:
                win += 1
            else:
                lose += 1
        win_rate = (win + draw) / verify_episode
        print("[Episode %d] Win : %d Draw : %d Lose : %d Win_rate: %.2f" % (episode, win, draw, lose, win_rate))
        agent.save()

        if win_rate > 0.97:
            break

        # print status (each train_episode * 100)
        win_rate_list.append(win_rate)
        if episode % ((train_episode1 + train_episode2) * 100) == 0:
            mean = np.mean(win_rate_list)
            win_rate_mean.append(np.round(mean, 2))
            win_rate_list.clear()
            print("[ ", end='')
            for x in win_rate_mean:
                print("%.2f" % x, end=' ')
            print("]")


if __name__ == "__main__":
    train()
