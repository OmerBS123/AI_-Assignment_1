import tkinter as tk

from Assigment_1.infra_libarrys.consts_and_enums.gui_consts import GuiSizeConsts, GuiColorConsts, GuiFontConsts


class GraphUI:
    def __init__(self, env, agents_list):
        self.env = env
        self.root = tk.Tk()
        self.root.title("Graph Simulation")

        self.canvas = tk.Canvas(self.root, width=GuiSizeConsts.DEFAULT_WIDTH, height=GuiSizeConsts.DEFAULT_HEIGHT, bg=GuiColorConsts.WHITE)
        self.canvas.pack()

        self.timer_label = tk.Label(self.root, text="Timer: 0")
        self.timer_label.pack(side=tk.TOP)

        self.message_entry = tk.Entry(self.root, width=GuiSizeConsts.MESSAGE_ENTRY_WIDTH)
        self.message_entry.pack(side=tk.BOTTOM)
        self.message_entry.insert(0, "Type your message here")

        self.message_button = tk.Button(self.root, text="Send Message", command=self.send_message)
        self.message_button.pack(side=tk.BOTTOM)

        self.offset_x = 0
        self.offset_y = 0

        self.agents_list = agents_list
        self.root.protocol("WM_DELETE_WINDOW", self.close_ui)
        self.flow = None
        self.should_close = False
        self.timer = 0

    def set_flow(self, flow):
        self.flow = flow

    def update_ui(self, timer_label):
        self.update_offsets()
        self.draw_graph()
        self.draw_agents()
        self.update_timer_label(timer_label=timer_label)
        self.root.update_idletasks()

    def update_offsets(self):
        self.root.update()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        self.offset_x = (canvas_width - self.env.width * GuiSizeConsts.SCALE_SIZE) // 2
        self.offset_y = (canvas_height - self.env.height * GuiSizeConsts.SCALE_SIZE) // 2

    def run_ui(self):
        self.root.after(0, self.update_ui_after)
        self.root.after(GuiSizeConsts.SECOND_IN_MILLI, self.check_close_flag)
        self.root.mainloop()

    def close_ui(self):
        self.flow.running = False
        self.should_close = True

    def draw_graph(self):
        self.canvas.delete("all")
        drawn_edges = set()
        for x in range(self.env.width + 1):
            for y in range(self.env.height + 1):
                node = self.env.graph[x][y]
                self.canvas.create_oval(x * GuiSizeConsts.SCALE_SIZE + self.offset_x, y * GuiSizeConsts.SCALE_SIZE + self.offset_y, x * GuiSizeConsts.SCALE_SIZE + GuiSizeConsts.OVAL_SIZE + self.offset_x,
                                        y * GuiSizeConsts.SCALE_SIZE + GuiSizeConsts.OVAL_SIZE + self.offset_y, fill=GuiColorConsts.BLUE)  # Node representation

                for edge in node.edges:
                    if edge in drawn_edges:
                        continue
                    drawn_edges.add(edge)
                    node1, node2 = edge.nodes
                    x1, y1 = node1.get_x_y_coordinate()
                    x2, y2 = node2.get_x_y_coordinate()
                    mid_x = (x1 + x2) * 0.5 * GuiSizeConsts.SCALE_SIZE + self.offset_x + GuiSizeConsts.LINE_SIZE
                    mid_y = (y1 + y2) * 0.5 * GuiSizeConsts.SCALE_SIZE + self.offset_y + GuiSizeConsts.LINE_SIZE
                    self.canvas.create_line(x1 * GuiSizeConsts.SCALE_SIZE + GuiSizeConsts.LINE_SIZE + self.offset_x, y1 * GuiSizeConsts.SCALE_SIZE + GuiSizeConsts.LINE_SIZE + self.offset_y,
                                            x2 * GuiSizeConsts.SCALE_SIZE + GuiSizeConsts.LINE_SIZE + self.offset_x, y2 * GuiSizeConsts.SCALE_SIZE + GuiSizeConsts.LINE_SIZE + self.offset_y, fill=GuiColorConsts.BLACK)
                    self.canvas.create_text(mid_x, mid_y, text=f"{edge.weight}", fill=GuiColorConsts.GREY, font=GuiFontConsts.EDGE_WEIGHT_FONT)

    def draw_agents(self):
        for curr_agent in self.agents_list:
            if curr_agent.curr_crossing_edge is None:
                x, y = curr_agent.curr_node.get_x_y_coordinate()
                self.canvas.create_text(x * GuiSizeConsts.SCALE_SIZE + 10 + self.offset_x, y * GuiSizeConsts.SCALE_SIZE - 5 + self.offset_y, text=curr_agent.tag, fill=curr_agent.agent_color, font=GuiFontConsts.EDGE_WEIGHT_FONT)  # Display agent's tag above it
            else:
                node1, node2 = curr_agent.curr_crossing_edge.nodes
                x1, y1 = node1.get_x_y_coordinate()
                x2, y2 = node2.get_x_y_coordinate()
                mid_x = (x1 + x2) * 0.5 * GuiSizeConsts.SCALE_SIZE + self.offset_x + GuiSizeConsts.LINE_SIZE
                mid_y = (y1 + y2) * 0.5 * GuiSizeConsts.SCALE_SIZE + self.offset_y + GuiSizeConsts.LINE_SIZE
                self.canvas.create_text(mid_x + GuiSizeConsts.AGENT_OFFSET_ON_EDGE, mid_y, text=curr_agent.tag, fill=curr_agent.agent_color, font=GuiFontConsts.EDGE_WEIGHT_FONT)
                # self.canvas.create_line(x1 * GuiConsts.SCALE_SIZE + 10 + self.offset_x, y1 * GuiConsts.SCALE_SIZE + 10 + self.offset_y,
                #                         x2 * GuiConsts.SCALE_SIZE + 10 + self.offset_x, y2 * GuiConsts.SCALE_SIZE + 10 + self.offset_y, fill=curr_agent.color)
                # # Adjust the coordinates based on the offset
                # self.canvas.create_text((x1 + x2) * 15 + 10 + self.offset_x, (y1 + y2) * 15 + 5 + self.offset_y, text=curr_agent.tag, fill=curr_agent.agent_color)

    def update_timer_label(self, timer_label):
        current_time = timer_label
        self.timer_label.config(text=f"Timer: {current_time}")

    def send_message(self):
        message = self.message_entry.get()
        # Handle the message (e.g., display it in the UI or send it to agents)
        print(f"Message: {message}")

    def check_close_flag(self):
        if self.should_close:
            self.root.destroy()
        else:
            self.root.after(GuiSizeConsts.SECOND_IN_MILLI, self.check_close_flag)

    def update_ui_after(self):
        self.update_ui(self.timer)
        self.root.after(GuiSizeConsts.SECOND_IN_MILLI // 4, self.update_ui_after)

    def update_timer(self, new_time):
        self.timer = new_time
