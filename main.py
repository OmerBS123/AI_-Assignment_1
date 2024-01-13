from infra_libarrys.infra_classes.SearchAlgorithem.Dijkstra import Dijkstra
from infra_libarrys.infra_functions.infra_functions import parse_args
from infra_libarrys.infra_functions.parser_functions import get_flow_args
from collections import defaultdict
from infra_libarrys.infra_classes.Flow import Flow


def main():
    config_path = "/Users/omerbensalmon/Desktop/BGU/Semester_5/inroduction_to_AI/Home_Assigments/Assigment_1/config.txt"
    parser_dict = defaultdict(list)
    parse_args(config_path, parser_dict)
    grid, agents_list, package_appear_dict, package_disappear_dict = get_flow_args(parser_dict)
    flow = Flow(grid, agents_list, package_appear_dict, package_disappear_dict)
    try:
        flow.run_flow()
    except Exception as e:
        print(f"Found exception while running flow, the exception:{e}")


if __name__ == "__main__":
    # main()
    #test for djkstra
    config_path = "/Users/omerbensalmon/Desktop/BGU/Semester_5/inroduction_to_AI/Home_Assigments/Assigment_1/config.txt"
    parser_dict = defaultdict(list)
    parse_args(config_path, parser_dict)
    grid, agents_list, package_appear_dict, package_disappear_dict = get_flow_args(parser_dict)
    for package in  package_appear_dict.values():
        package.add_self_to_env(grid)

    djkstra_algo = Dijkstra(grid.graph[0][0], grid)
    shortes_path = djkstra_algo.run_dijkstra()
    print("wait")
