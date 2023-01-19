AI-Principles---Pygame

Use of search algorithms in AI such as BFS, DFS, UCS and A\*

This project consists of a small game that is created using pygame. Spacecraft (Agent) of the game can be controlled by the player. Agent is able to find it's way to the goal using several search algorithms such as BFS, DFS, UCS & A\*(A-star).

Each algorithm has it's own copy of the game which can be found by the file name.

The game can be started by running below files.

|        File name         | Algorithm | Tree/Graph |
| :----------------------: | --------- | ---------- |
| aip_agent_astar_graph.py | A star    | Graph      |
| aip_agent_astar_tree.py  | A star    | Tree       |
|  aip_agent_bfs_graph.py  | BFS       | Graph      |
|  aip_agent_bfs_tree.py   | BFS       | Tree       |
|  aip_agent_dfs_graph.py  | DFS       | Graph      |
|  aip_agent_dfs_tree.py   | DFS       | Tree       |
|  aip_agent_ucs_graph.py  | UCS       | Graph      |
|  aip_agent_ucs_tree.py   | UCS       | Tree       |

- Rest of the files are supporiting files which cannot start the game.

Required

pip install pygame

Controls

When game is not active:

r - Start game (without auto pilot)
a - Start game with auto pilot (Spacecraft starts to find the goal on its own)

When game is active:

r - Reset game
a - Start auto pilot
g - Show grid with path
(arrows) - Control spacecraft manually
