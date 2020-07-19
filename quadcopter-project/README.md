# Deep RL Quadcopter Controller
## Project Summary

In this project, we designed an agent to fly a quadcopter, and then trained it using a Deep Q-reinforcement learning! The project replicates parts of the DeepMind paper: [Lillicrap, Timothy P., et al., 2015. Continuous Control with Deep Reinforcement Learning](https://arxiv.org/pdf/1509.02971.pdf). The project uses Actor-Critic method, Ornstein-Uhlenbeck Noise and Replay buffer.

## Project Overview

The Quadcopter or Quadrotor Helicopter is becoming an increasingly popular aircraft for both personal and professional use. Its maneuverability lends itself to many applications, from last-mile delivery to cinematography, from acrobatics to search-and-rescue.

Most quadcopters have 4 motors to provide thrust, although some other models with 6 or 8 motors are also sometimes referred to as quadcopters. Multiple points of thrust with the center of gravity in the middle improves stability and enables a variety of flying behaviors.

But it also comes at a price–the high complexity of controlling such an aircraft makes it almost impossible to manually control each individual motor's thrust. So, most commercial quadcopters try to simplify the flying controls by accepting a single thrust magnitude and yaw/pitch/roll controls, making it much more intuitive and fun.

The next step in this evolution is to enable quadcopters to autonomously achieve desired control behaviors such as takeoff and landing. You could design these controls with a classic approach (say, by implementing PID controllers). Or, you can use reinforcement learning to build agents that can learn these behaviors on their own. This is what we did in this project!

## Known Issues

- The quadcopter's flying behaviour is to some extent erratic. You are always welcome to contribute by forking this project and changing the reward function or the structure of Agent or Critic neural networks.


## Project Instructions

1. Clone the repository and navigate to the folder.

```
git clone https://github.com/lsirse/Data-Science-Portfolio.git
cd quadcopter-project
```

2. Create and activate a new environment.

```
conda create -n quadcop python=3.6 matplotlib numpy pandas
source activate quadcop
```

3. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `quadcop` environment. 
```
python -m ipykernel install --user --name quadcop --display-name "quadcop"
```

4. Open the notebook.
```
jupyter notebook Quadcopter_Project.ipynb
```

5. Before running code, change the kernel to match the `quadcop` environment by using the drop-down menu (**Kernel > Change kernel > quadcop**). Then, follow the instructions in the notebook.

6. You will likely need to install more pip packages in your machine.  Please curate the list of packages needed to run the project in the `requirements.txt` file in the repository.