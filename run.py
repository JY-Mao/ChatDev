# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import argparse
import logging
import os
import sys

from camel.typing import ModelType

# 获取当前文件的路径
root = os.path.dirname(__file__)
# 将当前路径添加到sys.path中
sys.path.append(root)

from chatdev.chat_chain import ChatChain


# 定义函数get_config，用于获取ChatChain的配置文件
# 参数company：自定义的配置文件名
# 返回：三个配置文件的路径：config_path, config_phase_path, config_role_path
def get_config(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/

    Returns:
        path to three configuration jsons: [config_path, config_phase_path, config_role_path]
    """
    # 获取公司配置文件夹的路径
    config_dir = os.path.join(root, "CompanyConfig", company)
    # 获取默认配置文件夹的路径
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    # 配置文件列表
    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    # 配置文件路径列表
    config_paths = []

    # 遍历配置文件列表
    for config_file in config_files:
        # 获取公司配置文件路径
        company_config_path = os.path.join(config_dir, config_file)
        # 获取默认配置文件路径
        default_config_path = os.path.join(default_config_dir, config_file)

        # 如果公司配置文件存在，则将公司配置文件路径添加到配置文件路径列表
        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        # 否则，将默认配置文件路径添加到配置文件路径列表
        else:
            config_paths.append(default_config_path)

    # 返回配置文件路径列表
    return tuple(config_paths)


# 创建参数解析器，描述参数
parser = argparse.ArgumentParser(description='argparse')
# 添加参数，类型为字符串，默认值为Default，帮助信息为Name of config, which is used to load configuration under CompanyConfig/
parser.add_argument('--config', type=str, default="Default",
                    help="Name of config, which is used to load configuration under CompanyConfig/")
# 添加参数，类型为字符串，默认值为DefaultOrganization，帮助信息为Name of organization, your software will be generated in WareHouse/name_org_timestamp
parser.add_argument('--org', type=str, default="DefaultOrganization",
                    help="Name of organization, your software will be generated in WareHouse/name_org_timestamp")
# 添加参数，类型为字符串，默认值为Develop a basic Gomoku game.，帮助信息为Prompt of software
parser.add_argument('--task', type=str, default="Develop a basic Gomoku game.",
                    help="Prompt of software")
# 添加参数，类型为字符串，默认值为Gomoku，帮助信息为Name of software, your software will be generated in WareHouse/name_org_timestamp
parser.add_argument('--name', type=str, default="Gomoku",
                    help="Name of software, your software will be generated in WareHouse/name_org_timestamp")
# 添加参数，类型为字符串，默认值为GPT_3_5_TURBO，帮助信息为GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K'}，参数可选
parser.add_argument('--model', type=str, default="GPT_3_5_TURBO",
                    help="GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K'}")
# 解析参数
args = parser.parse_args()

# Start ChatDev
# 开始聊天链

# ----------------------------------------
#          Init ChatChain
# ----------------------------------------
# 获取配置文件路径，阶段文件路径，角色文件路径
config_path, config_phase_path, config_role_path = get_config(args.config)
# 获取模型类型
args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO, 'GPT_4': ModelType.GPT_4, 'GPT_4_32K': ModelType.GPT_4_32k}
# 初始化聊天链
chat_chain = ChatChain(config_path=config_path,
                       config_phase_path=config_phase_path,
                       config_role_path=config_role_path,
                       task_prompt=args.task,
                       project_name=args.name,
                       org_name=args.org,
                       model_type=args2type[args.model])

# ----------------------------------------
#          Init Log
# ----------------------------------------
# 设置日志文件路径，日志级别，格式，日期格式，编码
logging.basicConfig(filename=chat_chain.log_filepath, level=logging.INFO,
                    format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%Y-%d-%m %H:%M:%S', encoding="utf-8")

# ----------------------------------------
#          Pre Processing
# ----------------------------------------

# 预处理
chat_chain.pre_processing()

# ----------------------------------------
#          Personnel Recruitment
# ----------------------------------------

# 招募人才
chat_chain.make_recruitment()

# ----------------------------------------
#          Chat Chain
# ----------------------------------------

# 执行聊天链
chat_chain.execute_chain()

# ----------------------------------------
#          Post Processing
# ----------------------------------------

# 处理后处理
chat_chain.post_processing()
