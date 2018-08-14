import numpy as np
from physics_sim import PhysicsSim

class Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_low = 0
        self.action_high = 900
        self.action_size = 4
        self.initial_distance = None
        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 
        if init_pose != None:
            self.initial_distance = np.sqrt((self.target_pos[0] - init_pose[0]) ** 2 + (self.target_pos[1] - init_pose[1]) ** 2 + (self.target_pos[2] - init_pose[2]) ** 2)

    def get_reward(self):
        """Uses current pose of sim to return reward."""
        if self.initial_distance != None:
            penalty = 0
            current_p = self.sim.pose
            target_p = self.target_pos[:3]

            a = (current_p[0] - target_p[0]) ** 2
            b = (current_p[1] - target_p[1]) ** 2
            c = (current_p[2] - target_p[2]) ** 2

            penalty += a
            penalty += b
            penalty += c

            #let's calculate the distance
            distance = np.sqrt(a+b+c)

            reward = ((self.initial_distance - distance) / self.initial_distance)
            if(reward < 0):
                reward = 0
            #continuous reward for just flying
            reward = 0.001
        else:
            reward = 1.-.3*(abs(self.sim.pose[:3] - self.target_pos)).sum()
        return reward

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state