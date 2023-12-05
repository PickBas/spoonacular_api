import json
import time

import utility


def recipy_search_demo():
    """
    Demo for the RecipiesSearch class.
    Writes the response to recipy_search_output.json file.
    """
    rs = utility.RecipiesSearch()
    response = rs.exec_query("pasta")
    pretty_response = json.dumps(response.json(), indent=4)
    with open('recipy_search_output.json', 'w') as f:
        f.write(pretty_response)


def recipy_info_demo():
    """
    Demo for the RecipiesInfo class.
    Write the output to recipy_info_output.json file.
    """
    rs = utility.RecipiesInfo()
    response = rs.exec_query("654959")
    pretty_response = json.dumps(response.json(), indent=4)
    with open('recipy_info_output.json', 'w') as f:
        f.write(pretty_response)


def main():
    recipy_search_demo()
    time.sleep(2)
    recipy_info_demo()


if __name__ == '__main__':
    main()
