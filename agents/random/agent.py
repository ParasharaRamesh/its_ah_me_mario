from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from tqdm import tqdm

from utils.manual import save_play


def random_agent(level, steps=500, record=False, buffer=[]):
    print("Starting random agent..")
    # create gym environment
    env = gym_super_mario_bros.make(level)
    env = JoypadSpace(env, SIMPLE_MOVEMENT)

    # play it
    done = True
    for _ in tqdm(range(steps)):
        if done:
            state = env.reset()
        action = env.action_space.sample()
        env_step = env.step(action)
        next_state, reward, done, info = env_step

        if record:
            buffer.append({
                "state": state,
                "action": action,
                "reward": reward,
                "done": done,
                "next_state": next_state,
                "info": info
            })

        state = next_state
        env.render()

    if record:
        # save it as a pickle file
        save_play(buffer, level, agent="random")

    env.close()
    print(f"Finished random agent..")


if __name__ == '__main__':
    #<world> is a number in {1, 2, 3, 4, 5, 6, 7, 8} indicating the world
    world = 1
    # <stage> is a number in {1, 2, 3, 4} indicating the stage within a world
    stage = 2

    # SuperMarioBros-<world>-<stage>-v<version>
    level = f"SuperMarioBros-{world}-{stage}-v2"

    # one attempt
    random_agent(level, steps=10000, record=False)
    #
    # # another attempt
    # random_agent(level, record=True)
