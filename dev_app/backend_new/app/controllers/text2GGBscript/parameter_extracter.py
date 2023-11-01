# %%
from controllers.text2GGBscript.classes.Completion import Completion
from pprint import pprint

# %%
def rectangular(name):
    parameter_extracter = Completion(
        model="gpt-3.5-turbo",
        system_prompt=f"I enter a math problem statement in Japanese. Please, extract the parameters of rectangular {name}.",
        funct={
            # 関数名と全体の説明
            "name": "parameter_extract",
            "description": f"This process extracts the parameters of rectangular",
            # 関数の詳細(引数)
            "parameters": {
                "type": "object",
                "properties": {
                    # 第1引数
                    "side_name_width": {
                        "type": "string",
                        "pattern": "[A-Z]{2}",
                        "description": "sides name of width of rectangular such as AB",
                    },
                    # 第2引数
                    "length_width": {
                        "type": "number",
                        "description": "length of width of rectangular",
                    },
                    # 第3引数
                    "side_name_depth": {
                        "type": "string",
                        "pattern": "[A-Z]{2}",
                        "description": "sides name of depth of rectangular such as AD",
                    },
                    # 第4引数
                    "length_depth": {
                        "type": "number",
                        "description": "length of depth of rectangular",
                    },
                    # 第5引数
                    "side_name_height": {
                        "type": "string",
                        "pattern": "[A-Z]{2}",
                        "description": "sides name of height of rectangular such as AE",
                    },
                    # 第6引数
                    "length_height": {
                        "type": "number",
                        "description": "length of height of rectangular",
                    },
                },
                "required": ["side_name_width", "length_width", "side_name_depth", "length_depth", "side_name_height", "length_height"]
            }
        },
    )
    return parameter_extracter

# %%
def Cube(name):
    parameter_extracter = Completion(
        model="gpt-3.5-turbo",
        system_prompt=f"I enter a math problem statement in Japanese. Please, extract the parameters of Cube {name}.",
        funct={
            # 関数名と全体の説明
            "name": "parameter_extract",
            "description": f"This process extracts the parameters of Cube",
            # 関数の詳細(引数)
            "parameters": {
                "type": "object",
                "properties": {
                    # 第1引数
                    "side_length": {
                        "type": "number",
                        "description": "sides length of Cube",
                    },
                }
            }
        },
    )
    return parameter_extracter

# %%
def Segment(name):
    parameter_extracter = Completion(
        model="gpt-3.5-turbo",
        system_prompt=f"I enter a math problem statement in Japanese. Please, extract the parameters of Segment {name}.",
        funct={
            # 関数名と全体の説明
            "name": "parameter_extract",
            "description": f"This process extracts the parameters of Segment",
            # 関数の詳細(引数)
            "parameters": {
                "type": "object",
                "properties": {
                    # 第1引数
                    "point_1": {
                        "type": "string",
                        "description": "Point object name for the endpoints of the line segment such as \'A\'",
                    },
                    # 第2引数
                    "point_2": {
                        "type": "string",
                        "description": "Point object name for the endpoints of the line segment such as \'B\'",
                    },
                }
            }
        },
    )
    return parameter_extracter

# %%
def Intersect(name):
    parameter_extracter = Completion(
        model="gpt-3.5-turbo",
        system_prompt=f"I enter a math problem statement in Japanese. Please, extract the parameters of Intersect {name}.",
        funct={
            # 関数名と全体の説明
            "name": "parameter_extract",
            "description": f"This process extracts the parameters of Intersect",
            # 関数の詳細(引数)
            "parameters": {
                "type": "object",
                "properties": {
                    # 第1引数
                    "part_object_1": {
                        "type": "string",
                        "description": "Names of part objects that create intersections or planes, such as point \'A\', line \'AB\' or plane \'ABC\'",
                    },
                    # 第2引数
                    "part_object_2": {
                        "type": "string",
                        "description": "Names of part objects that create intersections or planes, such as point \'D\', line \'DE\' or plane \'DEF\'",
                    },
                }
            }
        },
    )
    return parameter_extracter

# %%
def Midpoint(name):
    parameter_extracter = Completion(
        model="gpt-3.5-turbo",
        system_prompt=f"I enter a math problem statement in Japanese. Please, extract the parameters of Midpoint {name}.",
        funct={
            # 関数名と全体の説明
            "name": "parameter_extract",
            "description": f"This process extracts the parameters of Midpoint",
            # 関数の詳細(引数)
            "parameters": {
                "type": "object",
                "properties": {
                    # 第1引数
                    "point_1": {
                        "type": "string",
                        "description": "Name of the endpoint object to create the midpoint, such as \'A\'",
                    },
                    # 第2引数
                    "point_2": {
                        "type": "string",
                        "description": "Name of the endpoint object to create the midpoint, such as \'B\'",
                    },
                }
            }
        },
    )
    return parameter_extracter

# %%
def PerpendicularLine(name):
    parameter_extracter = Completion(
        model="gpt-3.5-turbo",
        system_prompt=f"I enter a math problem statement in Japanese. Please, extract the parameters of Perpendicular Line {name}.",
        funct={
            # 関数名と全体の説明
            "name": "parameter_extract",
            "description": f"This process extracts the parameters of Perpendicular Line",
            # 関数の詳細(引数)
            "parameters": {
                "type": "object",
                "properties": {
                    # 第1引数
                    "point": {
                        "type": "string",
                        "description": "Name of the endpoint object to create the perpendicular line, such as \'A\'",
                    },
                    # 第2引数
                    "part_object": {
                        "type": "string",
                        "description": "Name of the part object to create the perpendicular line, such as point \'A\', line \'AB\' or plane \'ABC\'",
                    },
                }
            }
        },
    )
    return parameter_extracter

# %%
def tetrahedron(name):
    parameter_extracter = Completion(
        model="gpt-3.5-turbo",
        system_prompt=f"I enter a math problem statement in Japanese. Please, extract the parameters of tetrahedron {name}.",
        funct={
            # 関数名と全体の説明
            "name": "parameter_extract",
            "description": f"This process extracts the parameters of tetrahedron",
            # 関数の詳細(引数)
            "parameters": {
                "type": "object",
                "properties": {
                    # 第1引数
                    "side_name_and_length": {
                        "type": "array",
                        "description": "input name and length of all sides of tetrahedron as array",
                        "items": {
                            # リストの要素
                            "type": "object",
                            "properties": {
                                # dict[0]
                                "side_name": {
                                    "type": "string",
                                    "description": "name of side of tetrahedron such as \'AB\'"
                                },
                                # dict[1]
                                "side_length": {
                                    "type": "number",
                                    "description": "length of side of tetrahedron"
                                },
                            }
                        }
                    }
                }
            }
        },
    )
    return parameter_extracter

# %%
def main():
    print("TEST")
    parameter_extracter = rectangular("ABCD-EFGH")
    print(parameter_extracter.create("立体ABCD-EFGHは，AB=40cm，AD=30cm，AE=50cmの直方体である．", p_flg=True))
    return

if __name__ == '__main__':
    main()