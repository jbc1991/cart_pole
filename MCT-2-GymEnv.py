# Gotta import gym!
import gym

env = gym.make('CartPole-v0')

# Default observation variable
print("Initial Observation")
observation = env.reset()
print(observation)

print('\n')
for _ in range(1):


    # Random Action
    action = env.action_space.sample()

    # Get the 4 observation values 
    observation, reward, done, info = env.step(action)

    print("Performed One Random Action")
    print('\n')
    print('observation')
    print(observation)
    print('\n')

    print('reward')
    print(reward)
    print('\n')

    print('done')
    print(done)
    print('\n')

    print('info')
    print(info)
    print('\n')
