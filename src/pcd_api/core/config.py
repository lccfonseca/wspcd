

class Settings():
    sgbd: str = "mysql"
    connector: str = "mysqlconnector"
    db_host: str = "10.101.33.109"
    db_port: str = "3306"
    db_name: str = "pcd"
    db_user: str = "aluno"
    db_pass: str = "12345678"

    db_connection_string: str = f'{sgbd}+{connector}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

    project_name: str = "Uema.Devlab.Nau.Wspcd"

    api_v1_str: str = "/v1"