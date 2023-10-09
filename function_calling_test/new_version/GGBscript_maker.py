# %%
from __future__ import annotations
from sympy import symbols, Eq, solve, sqrt
from pprint import pprint

# %%
def rectangular(part_object: dict[str,str,dict]):
    object_name = part_object["object_name"]
    parameters = part_object["parameters"]

    segments = {
        "width": parameters["side_name_width"],
        "depth": parameters["side_name_depth"],
        "height": parameters["side_name_height"]
    }
    
    # segmentは辺の名前2文字 AB など
    for side, segment in segments.items():
        if segment[1] == object_name[1]:
            width = parameters[f"length_{side}"]
        elif segment[1] == object_name[3]:
            depth = parameters[f"length_{side}"]
        elif segment[1] == object_name[5]:
            height = parameters[f"length_{side}"]
        else:
            ValueError("長方形の辺の名前が合いません．エラー処理を作ってください．")

    ggbscript = f"{object_name[0]} = (0,0,0)\n"
    ggbscript += f"{object_name[1]} = ({width},0,0)\n"
    ggbscript += f"{object_name[2]} = ({width},{depth},0)\n"
    ggbscript += f"{object_name[3]} = (0,{depth},0)\n"
    ggbscript += f"{object_name[5]} = (0,0,{height})\n"
    ggbscript += f"{object_name[6]} = ({width},0,{height})\n"
    ggbscript += f"{object_name[7]} = ({width},{depth},{height})\n"
    ggbscript += f"{object_name[8]} = (0,{depth},{height})\n"
    
    ggbscript += f"{object_name[0]}{object_name[1]} = Segment({object_name[0]},{object_name[1]})\n"
    ggbscript += f"{object_name[1]}{object_name[2]} = Segment({object_name[1]},{object_name[2]})\n"
    ggbscript += f"{object_name[2]}{object_name[3]} = Segment({object_name[2]},{object_name[3]})\n"
    ggbscript += f"{object_name[3]}{object_name[0]} = Segment({object_name[3]},{object_name[0]})\n"
    ggbscript += f"{object_name[0]}{object_name[5]} = Segment({object_name[0]},{object_name[5]})\n"
    ggbscript += f"{object_name[1]}{object_name[6]} = Segment({object_name[1]},{object_name[6]})\n"
    ggbscript += f"{object_name[2]}{object_name[7]} = Segment({object_name[2]},{object_name[7]})\n"
    ggbscript += f"{object_name[3]}{object_name[8]} = Segment({object_name[3]},{object_name[8]})\n"
    ggbscript += f"{object_name[5]}{object_name[6]} = Segment({object_name[5]},{object_name[6]})\n"
    ggbscript += f"{object_name[6]}{object_name[7]} = Segment({object_name[6]},{object_name[7]})\n"
    ggbscript += f"{object_name[7]}{object_name[8]} = Segment({object_name[7]},{object_name[8]})\n"
    ggbscript += f"{object_name[8]}{object_name[5]} = Segment({object_name[8]},{object_name[5]})\n"

    return ggbscript

# %%
def Cube(part_object: dict[str,str,dict]):
    object_name = part_object["object_name"]
    parameters = part_object["parameters"]

    ggbscript = f"{object_name[0]} = (0,0,0)\n"
    ggbscript += f"{object_name[1]} = ({parameters['side_length']},0,0)\n"
    ggbscript += f"{object_name[3]} = (0,{parameters['side_length']},0)\n"
    ggbscript += f"{object_name[5]} = (0,0,{parameters['side_length']})\n"

    ggbscript = f"{object_name} = Cube({object_name[0]},{object_name[1]},{object_name[3]})\n"
    return ggbscript

# %%
def Segment(part_object: dict[str,str,dict]):
    object_name = part_object["object_name"]
    parameters = part_object["parameters"]

    ggbscript = f"{object_name} = Segment({parameters['point_1']},{parameters['point_2']})\n"
    return ggbscript

# %%
def Intersect(part_object: dict[str,str,dict]):
    object_name = part_object["object_name"]
    parameters = part_object["parameters"]

    ggbscript = f"{object_name} = Intersect({parameters['part_object_1']},{parameters['part_object_2']})\n"
    return ggbscript

# %%
def Midpoint(part_object: dict[str,str,dict]):
    object_name = part_object["object_name"]
    parameters = part_object["parameters"]
    
    ggbscript = f"{object_name} = Midpoint({parameters['point_1']},{parameters['point_2']})\n"
    return ggbscript

# %%
def PerpendicularLine(part_object: dict[str,str,dict]):
    object_name = part_object["object_name"]
    parameters = part_object["parameters"]

    ggbscript = f"{object_name} = PerpendicularLine({parameters['point']},{parameters['part_object']})\n"
    return ggbscript

# %%
"""
def tetrahedron(part_object: dict[str,str,dict]):
    # Define the variables
    x, y, z = symbols('x y z')
    a, b, c, d, e, f = symbols('a b c d e f')
    
    # Coordinates for A, B
    A = (0, 0, 0)
    B = (a_val, 0, 0)
    
    # Coordinate for C using the cosine rule
    xC = (a_val**2 + c_val**2 - b_val**2) / (2*a_val)
    yC = sqrt(c_val**2 - xC**2)
    C = (xC, yC, 0)
    
    # Spherical equations based on distances from A, B, C to P
    eq1 = Eq((x - A[0])**2 + (y - A[1])**2 + (z - A[2])**2, d**2)
    eq2 = Eq((x - B[0])**2 + (y - B[1])**2 + (z - B[2])**2, e**2)
    eq3 = Eq((x - C[0])**2 + (y - C[1])**2 + (z - C[2])**2, f**2)

    # Solve the system of equations
    solutions = solve((eq1, eq2, eq3), (x, y, z))
    
    # Select the solution with positive z-coordinate
    P_solution = None
    subs = {a: a_val, b: b_val, c: c_val, d: d_val, e: e_val, f: f_val}
    for sol in solutions:
        if sol[2].subs(subs) > 0:
            P_solution = sol
            break
            
    P = tuple([coord.subs(subs) for coord in P_solution])
    
    return {name[0]: P, name[1]: A, name[2]: B, name[3]: C}
    return parameter_extracter
"""

# %%
# スクリプト生成機 文字列→関数 の変換用
script_maker_functs = {
    "rectangular": rectangular,
    "Cube": Cube,
    "Segment": Segment,
    "Intersect": Intersect,
    "Midpoint": Midpoint,
    "PerpendicularLine": PerpendicularLine,
    # "tetrahedron": tetrahedron,
}

# %%
def main():
    print("TEST")
    
    part_objects = [
        {'object_name': 'ABCD-EFGH',
        'object_type': 'rectangular',
        'parameters': {
            'length_depth': 30,
            'length_height': 50,
            'length_width': 40,
            'side_name_depth': 'AD',
            'side_name_height': 'AE',
            'side_name_width': 'AB'}},
        {'object_name': 'DF',
        'object_type': 'Segment',
        'parameters': {'point_1': 'B', 'point_2': 'I'}},
        {'object_name': 'BI',
        'object_type': 'PerpendicularLine',
        'parameters': {'part_object': 'line BI', 'point': 'I'}},
        {'object_name': 'I',
        'object_type': 'Intersect',
        'parameters': {'part_object_1': 'BI', 'part_object_2': 'DF'}}
    ]

    output = ""
    for part_object in part_objects:
        # GGBScriptを生成する
        # スクリプト生成機を作成する関数を選定
        script_maker_func = script_maker_functs[part_object["object_type"]]
        # スクリプト生成関数を実行し辞書に保存
        GGBscript = script_maker_func(part_object)
        part_object["GGBscript"] = GGBscript
        # 最終的なアウトプットを作る
        output += GGBscript

    print("スクリプト生成機の最終結果")
    print(output)

if __name__ == '__main__':
    main()