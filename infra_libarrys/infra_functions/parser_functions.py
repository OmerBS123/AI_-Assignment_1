from infra_libarrys.consts_and_enums.general_consts import GeneralPosConsts
from infra_libarrys.consts_and_enums.EdgeConsts import BlockedEdgeConsts, FragileEdgeConsts
from infra_libarrys.consts_and_enums.package_consts import PackageConsts
from infra_libarrys.consts_and_enums.agents_consts import AgentConsts
from infra_libarrys.infra_classes.Package import Package
from infra_libarrys.infra_classes.Agent.InterferingAgent import InterferingAgent
from infra_libarrys.infra_classes.Agent.HumanAgent import HumanAgent
from infra_libarrys.infra_classes.Agent.NormalAgent import NormalAgent
from infra_libarrys.consts_and_enums.parser_consts import ParserFlags
from infra_libarrys.infra_classes.Grid import Grid


def get_flow_args(parser_dict):
    grid = get_grid(parser_dict)
    agents_list = get_agents_list(parser_dict, grid)
    package_appear_dict, package_disappear_dict = get_package_dict(parser_dict)
    return grid, agents_list, package_appear_dict, package_disappear_dict


def get_package_dict(parser_dict):
    return {package.time_appearance: package for package in parser_dict[ParserFlags.P]}, {package.time_delivery + 1: package for package in parser_dict[ParserFlags.P]}


def get_agents_list(parser_dict, grid):
    agents_list = []
    for agent_flag, x, y in parser_dict[ParserFlags.AGENTS]:
        curr_node = grid.graph[x][y]
        if agent_flag == AgentConsts.NORMAL_AGENT_FLAG:
            agents_list.append(NormalAgent(curr_node, grid))
        elif agent_flag == AgentConsts.INTERFERING_AGENT_FLAG:
            agents_list.append(InterferingAgent(curr_node, grid))
        else:
            agents_list.append(HumanAgent(curr_node, grid))

    return agents_list


def get_grid(parser_dict):
    x = parser_dict[ParserFlags.X][0]
    y = parser_dict[ParserFlags.Y][0]
    blocked_edges = parser_dict[ParserFlags.B]
    fragile_edges = parser_dict[ParserFlags.F]
    gird = Grid(x, y, blocked_edges=blocked_edges, fragile_edges=fragile_edges)
    return gird


def parse_x_flag(line, parser_dict):
    splitted_line = line.split()
    parser_dict[ParserFlags.X].append(int(splitted_line[GeneralPosConsts.POS_FOR_X]))


def parse_y_flag(line, parser_dict):
    splitted_line = line.split()
    parser_dict[ParserFlags.Y].append(int(splitted_line[GeneralPosConsts.POS_FOR_Y]))


def parse_p_flag(line, parser_dict):
    splitted_line = line.split()
    args_package = (int(splitted_line[PackageConsts.POS_FOR_X]), int(splitted_line[PackageConsts.POS_FOR_Y]), int(splitted_line[PackageConsts.POS_DEST_X]), int(splitted_line[PackageConsts.POS_DEST_Y]),
                    int(splitted_line[PackageConsts.POS_APPEAR_TIME]), int(splitted_line[PackageConsts.POS_DELIVERY_TIME]))
    package = Package(*args_package)
    parser_dict[ParserFlags.P].append(package)


def parse_b_flag(line, parser_dict):
    splitted_line = line.split()
    from_pos = (int(splitted_line[BlockedEdgeConsts.POS_X_FROM]), int(splitted_line[BlockedEdgeConsts.POS_Y_FROM]))
    to_pos = (int(splitted_line[BlockedEdgeConsts.POS_X_TO]), int(splitted_line[BlockedEdgeConsts.POS_Y_TO]))
    parser_dict[ParserFlags.B].append((*from_pos, *to_pos))


def parse_f_flag(line, parser_dict):
    splitted_line = line.split()
    from_pos = (int(splitted_line[FragileEdgeConsts.POS_X_FROM]), int(splitted_line[FragileEdgeConsts.POS_Y_FROM]))
    to_pos = (int(splitted_line[FragileEdgeConsts.POS_X_TO]), int(splitted_line[FragileEdgeConsts.POS_Y_TO]))
    parser_dict[ParserFlags.F].append((*from_pos, *to_pos))


def parse_agent_flag(line, parser_dict):
    splitted_line = line.split()
    pos_x = int(splitted_line[AgentConsts.POS_X])
    pos_y = int(splitted_line[AgentConsts.POS_Y])
    agent_flag = splitted_line[AgentConsts.POS_FLAG]
    agent_tuple = (agent_flag, pos_x, pos_y)
    parser_dict[ParserFlags.AGENTS].append(agent_tuple)
