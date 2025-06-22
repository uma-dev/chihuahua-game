from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from gym_ext.env import ChihuahuaEnv


def train():
    env = ChihuahuaEnv()  # render_mode =
    check_env(env)
    model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="logs/ppo_tensorboard/")
    model.learn(total_timesteps=100_000)
    model.save("models/ppo_chihuahua")


def evaluate():
    env = ChihuahuaEnv(render_mode="human")
    model = PPO.load("models/ppo_chihuahua")
    obs, _ = env.reset()
    for _ in range(1000):
        action, _ = model.predict(obs)
        obs, _, done, _, _ = env.step(action)
        if done:
            obs, _ = env.reset()
