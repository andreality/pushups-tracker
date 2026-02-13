from pixela.setup import create_user_account, create_graph
from config import config_dict


create_user_account(token=config_dict['pixela_token'],
                    user_name=config_dict['pixela_user_name'])

create_graph(graph_id=config_dict['pixela_graph_id'], graph_name=config_dict['pixela_graph_name'])

