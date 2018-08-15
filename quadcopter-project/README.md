# Deep RL Quadcopter Controller
## Project Overview
In this project, we designed an agent to fly a quadcopter, and then trained it using a Deep Q-reinforcement learning! The project replicates parts of the DeepMind paper: [Lillicrap, Timothy P., et al., 2015. Continuous Control with Deep Reinforcement Learning](https://arxiv.org/pdf/1509.02971.pdf). The project uses Actor-Critic method, Ornstein-Uhlenbeck Noise and Replay buffer.

## Known Issues

- <span style="color:red">The quadcopter's flying behaviour is still very erratic. You are always welcome to contribute by forking this project and changing the reward function or the structure of Agent or Critic neural networks. </span>


## Project Instructions

1. Download the files and navigate to the downloaded folder.

```
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