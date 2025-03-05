import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO

class InventoryEnv(gym.Env):
    def __init__(self, demand, holding_cost=2, penalty_cost=10):
        super(InventoryEnv, self).__init__()
        self.max_stock = 500  # Maximum stock level
        self.stock = np.random.randint(20, 100)  # Initial stock (random between 20 and 100)
        self.demand = demand  # Average demand per day
        self.holding_cost = holding_cost  # Holding cost per unit
        self.penalty_cost = penalty_cost  # Penalty for stockout

        # Action space (Reorder Quantity)
        self.action_space = gym.spaces.Discrete(100)
        self.observation_space = gym.spaces.Box(low=0, high=self.max_stock, shape=(1,), dtype=np.int32)

    def step(self, action):
        """Simulate one step in the inventory environment."""
        order_qty = action  # Reorder quantity
        self.stock += order_qty  # Add the ordered quantity to stock

        # Simulate sales: Random sales based on demand (between demand - 5 and demand + 5)
        sales = min(self.stock, np.random.randint(self.demand - 5, self.demand + 5))
        self.stock -= sales  # Subtract sales from stock

        # Reward Calculation:
        # Holding penalty (stock left over) + Stockout penalty if stock is too low
        holding_penalty = self.stock * self.holding_cost
        stockout_penalty = self.penalty_cost if self.stock < 5 else 0
        reward = sales - (holding_penalty + stockout_penalty)  # Reward is sales minus penalties

        # Done flag is False (not a terminal state in this simple model)
        done = False

        # Return the new state (stock), reward, done flag, and additional info (empty in this case)
        return np.array([self.stock]), reward, done, {}

    def reset(self):
        """Reset the environment to an initial state."""
        self.stock = np.random.randint(20, 100)  # Reset stock to a random number between 20 and 100
        return np.array([self.stock])  # Return the initial stock as the starting state

if __name__ == "__main__":
    """Training the Reinforcement Learning model."""
    env = InventoryEnv(demand=50)  # Initialize the environment with average demand of 50 units
    model = PPO("MlpPolicy", env, verbose=1)  # Use PPO algorithm (Proximal Policy Optimization)
    model.learn(total_timesteps=10000)  # Train the model for 10,000 timesteps

    # Save the trained model
    model.save("../../models/inventory_rl_model.pkl")
    print("✅ Reinforcement Learning Model Trained and Saved!")
