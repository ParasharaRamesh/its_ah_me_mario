import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from nes_py.wrappers import JoypadSpace
import gym

from env import _register_all_coin_collector_envs


# from game.coincollector import _register_all_coin_collector_envs


def create_gym_env_from_level(world, stage, version, use_coin_collector_env):
    level_suffix = f"{world}-{stage}-v{version}"
    if not use_coin_collector_env:
        level = f"SuperMarioBros-{level_suffix}"
        env = gym_super_mario_bros.make(level)
    else:
        env_set = set(gym.envs.registration.registry.env_specs.copy().keys())
        level = f"CoinCollectorSuperMarioBrosEnv-{level_suffix}"
        if level not in env_set:
            # register all these custom environments for the first time
            _register_all_coin_collector_envs()

        assert level in set(gym.envs.registration.registry.env_specs.copy().keys()), f"Looks like {level} was not registered correctly!"
        env = gym.make(level)

    env = JoypadSpace(env, SIMPLE_MOVEMENT)
    return env

