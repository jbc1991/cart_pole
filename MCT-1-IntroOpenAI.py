# Gotta import gym!
import gym

env = gym.make('CartPole-v0')

# Reset the environment to default beginning
env.reset()

# Using _ as temp placeholder variable
for _ in range(1000):
    # Render the env
    env.render()
    env.step(env.action_space.sample()) # take a random action
