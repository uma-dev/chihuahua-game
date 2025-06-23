import os
from stable_baselines3 import PPO
from gym_ext.env import ChihuahuaEnv

MODEL_PATH = "models/ppo_chihuahua"
LOGS_PATH = "logs/ppo_tensorboard/"


def train(render_mode=None):
    env = ChihuahuaEnv(render_mode=render_mode)

    if os.path.exists(MODEL_PATH + ".zip"):
        print(f"Loading existing model from {MODEL_PATH}")
        model = PPO.load(MODEL_PATH, env=env)
        model.set_env(env)
    else:
        print(f"Training new model and saving to {MODEL_PATH}")
        model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=LOGS_PATH)

    model.learn(total_timesteps=100_000)
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


def evaluate():
    env = ChihuahuaEnv(render_mode="human")
    model = PPO.load(MODEL_PATH)
    obs, _ = env.reset()

    for _ in range(1000):
        action, _ = model.predict(obs)
        obs, _, done, _, _ = env.step(action)
        if done:
            print("Episode finished. Resetting env.")
            obs, _ = env.reset()
