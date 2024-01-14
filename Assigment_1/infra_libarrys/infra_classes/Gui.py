import tkinter as tk
import time

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
UPDATE_INTERVAL = 100  # milliseconds

class GraphUI:
    def __init__(self, env):
        self.env = env
        self.root = tk.Tk()
        self.root.title("Graph Simulation")

        self.canvas = tk.Canvas(self.root, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, bg="white")
        self.canvas.pack()

        self.timer_label = tk.Label(self.root, text="Timer: 0")
        self.timer_label.pack(side=tk.TOP)

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(side=tk.BOTTOM)
        self.message_entry.insert(0, "Type your message here")

        self.message_button = tk.Button(self.root, text="Send Message", command=self.send_message)
        self.message_button.pack(side=tk.BOTTOM)

        self.agents = {}  # Assuming agents are stored in a dictionary with agent_id as keys

        self.update_ui()
        self.root.mainloop()

    def update_ui(self):
        self.draw_graph()
        self.draw_agents()
        self.update_timer_label()
        self.root.after(UPDATE_INTERVAL, self.update_ui)

    def draw_graph(self):
        self.canvas.delete("all")
        for x in range(self.env.width + 1):
            for y in range(self.env.height + 1):
                node = self.env.graph[x][y]
                self.canvas.create_oval(x * 30, y * 30, x * 30 + 20, y * 30 + 20, fill="blue")  # Node representation

                for edge in node.edges:
                    x1, y1, x2, y2 = edge.nodes
                    self.canvas.create_line(x1 * 30 + 10, y1 * 30 + 10, x2 * 30 + 10, y2 * 30 + 10, fill="black")  # Edge representation

    def draw_agents(self):
        for agent_id, agent in self.agents.items():
            if agent.state == "on_node":
                x, y = agent.current_node.x, agent.current_node.y
                self.canvas.create_oval(x * 30 + 5, y * 30 + 5, x * 30 + 15, y * 30 + 15, fill="red")  # Agent on node
            elif agent.state == "on_edge":
                x1, y1, x2, y2 = agent.current_edge.nodes
                self.canvas.create_line(x1 * 30 + 10, y1 * 30 + 10, x2 * 30 + 10, y2 * 30 + 10, fill="red")  # Agent on edge

    def update_timer_label(self):
        current_time = int(time.time())
        self.timer_label.config(text=f"Timer: {current_time}")

    def send_message(self):
        message = self.message_entry.get()
        # Handle the message (e.g., display it in the UI or send it to agents)
        print(f"Message: {message}")


class Agent:
    def __init__(self, agent_id, initial_node):
        self.agent_id = agent_id
        self.current_node = initial_node
        self.current_edge = None
        self.state = "on_node"  # or "on_edge" depending on the initial state

if __name__ == "__main__":
    # Assume you have an initialized environment object 'env'
    graph_ui = GraphUI(env)
