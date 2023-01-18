# AI-Principles---Pygame

Use of search algorithms in AI such as BFS, DFS, UCS and A\*

This project consists of a small game that is created using pygame. Spacecraft (Agent) of the game can be controlled by the player. Agent is able to find it's way to the goal using several search algorithms such as BFS, DFS, UCS & A*(A-star).

Each algorithm has it's own copy of the game which can be found by the file name.

The game can be started by running below files.

|            <br>**File name**       	|    <br>**Algorithm** 	|    <br>**Tree/Graph**	|
|:----------------------------------:	|---------------------	|----------------------	|
|    <br>aip_agent_astar_graph.py    	|    <br>A star       	|    <br>Graph         	|
|    <br>aip_agent_astar_tree.py     	|    <br>A star       	|    <br>Tree          	|
|    <br>aip_agent_bfs_graph.py      	|    <br>BFS          	|    <br>Graph         	|
|    <br>aip_agent_bfs_tree.py       	|    <br>BFS          	|    <br>Tree          	|
|    <br>aip_agent_dfs_graph.py      	|    <br>DFS          	|    <br>Graph         	|
|    <br>aip_agent_dfs_tree.py       	|    <br>DFS          	|    <br>Tree          	|
|    <br>aip_agent_ucs_graph.py      	|    <br>UCS          	|    <br>Graph         	|
|    <br>aip_agent_ucs_tree.py       	|    <br>UCS          	|    <br>Tree          	|


# Required

<br>pip install pygame

# Controls

<br>When game is not active:

<br>r - Start game (without auto pilot)
<br>a - Start game with auto pilot (Spacecraft starts to find the goal on its own)

<br>When game is active:

<br>r - Reset game
<br>a - Start auto pilot
<br>g - Show grid with path
<br>(arrows) - Control spacecraft manually
