import utility


def main():
    rs = utility.RecipiesInfo()
    response = rs.exec_query("654959")
    print(response.json())


if __name__ == '__main__':
    main()
