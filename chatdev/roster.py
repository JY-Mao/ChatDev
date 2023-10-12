class Roster():
    def __init__(self) -> None:
        self.agents = list()

    def _recruit(self, agent_name: str):
        # 添加一个员工
        self.agents.append(agent_name)

    def _exist_employee(self, agent_name: str):
        # 获取所有员工的名字
        names = self.agents + [agent_name]
        # 将所有员工的名字转换为小写，并去除空格和下划线
        names = [name.lower().strip() for name in names]
        names = [name.replace(" ", "").replace("_", "") for name in names]
        # 获取最后一个员工的名字
        agent_name = names[-1]
        # 判断最后一个员工的名字是否在所有员工的名字中
        if agent_name in names[:-1]:
            return True
        return False

    def _print_employees(self):
        # 获取所有员工的名字
        names = self.agents
        # 将所有员工的名字转换为小写，并去除空格和下划线
        names = [name.lower().strip() for name in names]
        # 打印所有员工的名字
        print("Employees: {}".format(names))
