import copy
import threading

from infra_libarrys.infra_classes.Agent.AstarAgent import AstarAgent
from infra_libarrys.infra_functions.infra_functions import parse_args
from infra_libarrys.infra_functions.parser_functions import get_flow_args
from infra_libarrys.infra_classes.Flow import Flow
from infra_libarrys.infra_classes.Gui import GraphUI


def main():
    config_path = "/Users/omerbensalmon/Desktop/BGU/Semester_5/inroduction_to_AI/Home_Assigments/Assigment_1/support_files/config.txt"
    parser_dict = parse_args(config_path)
    env, agents_list = get_flow_args(parser_dict)

    env.update_packages_state_if_needed(0)
    copy_of_env = copy.copy(env)

    astar_agent = AstarAgent(env=env, curr_node=env.graph[0][0])

    gui = GraphUI(env, agents_list)
    flow = Flow(env, agents_list, package_appear_dict, package_disappear_dict, gui_handler=gui)
    gui.set_flow(flow)
    flow_thread = threading.Thread(target=flow.run_flow)
    flow_thread.start()
    gui.run_ui()


if __name__ == "__main__":
    main()
