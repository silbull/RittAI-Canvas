import json, pprint

JSON_OUTPUT_PATH = "test_data/test_data_questions.json"

questions = """立体ABCD-EFGHは，AB=40cm，AD=30cm，AE=50cmの直方体である．頂点Dと頂点Fを結び，頂点Bから線分DFに引いた垂線と線分DFとの交点をIとする．線分BIの長さは何cmか．
AB = √3，AC=AD=BC=DB=4の四面体ABCDがある．また，辺CDの中点をMとする．頂点Aから三角形BCDに垂線AHを下ろしたとき，AHの長さを求めよ．
四面体ABCDにおいて，AB=3, BC=√13, CA=4, DA=DB=DC=3とし，頂点Dから △ABCに垂線DHを下ろす．
直方体ABCD-EFGHにおいて，辺AB，AD，AEの長さをそれぞれa，b，cとする．また，頂点Aから直線FHにおろした垂線をALとする．
AB=5 cm，BC=6 cm，AD=3 cm，∠C=∠D=90°の台形 ABCD を，辺 DC を軸として 1回転させてできる立体の体積を求めなさい．
底面の半径が 3 cm の円すいの中に，底面の半径が 1 cm，高さが 4 cm の円柱がある。円柱の上面は円すいの側面に接し，底面は円すいの底面に固定されている.
AB=3 cm，BC=4 cm，BF=5 cm の直方体 ABCDEFGH がある。線分 FH の中点を M とし，線分 DM と線分 BH との交点を N とする．
AB=30 cm，AD=20 cm，AE=5 cm の直方体 ABCD-EFGH がある。辺 AB，HG の中点をそれぞれ M，N とし，頂点 A から線分 DM に引いた垂線と線分 DM の交点を P とする。
１辺の長さが 6 cm の立方体がある。正方形 AEFB の対角線 AF 上に AP=PQ=QF となるように2点P，Q をとる。
1辺が6cmの立方体ABCD-EFGHがあります．この立方体の対角線AG上に，角AIF=90°となる点Iをとります．
三角形ABCDがあり、AB = √3、AC = AD = BC = DB = 4です。また、辺CDの中点をMとします。頂点Aから三角形BCDに垂線AHを下ろしたとき、AHの長さを求めてください。
四面体ABCDにおいて、AB=3、BC=√13、CA=4、DA=DB=DC=3とし、頂点Dから△ABCに垂線DHを下ろすことを考えます。DHの長さを求めてください。
直方体ABCDEFGHにおいて、辺AB、AD、AEの長さをそれぞれa、b、cとします。頂点Aから直線FHにおろした垂線ALの長さを求めてください。
AB=5 cm、BC=6 cm、AD=3 cm、∠C=∠D=90°の台形ABCDを、辺DCを軸として1回転させてできる立体の体積を求めてください。
底面の半径が3 cmの円すいの中に、底面の半径が1 cmで高さが4 cmの円柱があります。円柱の上面は円すいの側面に接し、底面は円すいの底面に固定されています。円柱の体積を求めてください。
AB=3 cm、BC=4 cm、BF=5 cmの直方体ABCDEFGHがあります。線分FHの中点をMとし、線分DMと線分BHとの交点をNとします。三角形DMNの面積を求めてください。
AB=30 cm、AD=20 cm、AE=5 cmの直方体ABCD-EFGHがあります。辺ABとHGの中点をそれぞれM、Nとし、頂点Aから線分DMに引いた垂線と線分DMの交点をPとします。三角形AMPの面積を求めてください。
1辺の長さが6 cmの立方体ABCD-EFGHがあります。正方形AEFBの対角線AF上にAP=PQ=QFとなるように2点P、Qをとることを考えます。APの長さを求めてください。
1辺が6 cmの立方体ABCD-EFGHがあります。この立方体の対角線AG上に、角AIF=90°となる点Iをとります。点Iから点Aまでの距離を求めてください。
1辺が8 cmの立方体ABCD-EFGHがあります。頂点Eから立方体の対角線HGに垂直に伸びる直線を引き、立方体の表面と交わる点をPとします。EPの長さを求めてください。
直方体ABCD-EFGHがあり、AB=7 cm、BC=5 cm、AD=12 cmです。対角線BD上に点Pをとり、BP=9 cm、CP=4 cmの条件を満たす点Pを求めてください。
AB=6 cm、BC=8 cm、AC=10 cmの直角三角形ABCがあります。この三角形を含む直方体ABCD-EFGHを考えます。直方体の体積を求めてください。
1辺が10 cmの立方体ABCD-EFGHがあります。立方体の頂点Aから対角線CGに垂直に伸びる直線を引き、直線と立方体の表面との交点を求めてください。
AB=5 cm、BC=7 cm、CA=9 cmの直角三角形ABCがあります。この三角形を底面とし、高さが6 cmの直方体ABCD-EFGHを考えます。直方体の体積を求めてください。
AB=4 cm、BC=3 cm、CA=5 cmの直角三角形ABCがあります。この三角形を底面とし、高さが8 cmの直方体ABCD-EFGHを考えます。直方体の体積を求めてください。
1辺が10 cmの立方体ABCD-EFGHがあります。直方体の頂点Aから面DFEH上に垂直に伸びる直線を引き、この直線と面DFEHの交点を求めてください。
AB=12 cm、BC=5 cm、CA=13 cmの三角形ABCがあります。この三角形を底面とし、高さが9 cmの直方体ABCD-EFGHを考えます。直方体の体積を求めてください。
1辺が15 cmの立方体ABCD-EFGHがあります。直方体の頂点Aから面DEFG上に垂直に伸びる直線を引き、この直線と面DEFGの交点を求めてください。
AB=8 cm、BC=15 cm、CA=17 cmの三角形ABCがあります。この三角形を底面とし、高さが10 cmの直方体ABCD-EFGHを考えます。直方体の体積を求めてください。
1辺が18 cmの立方体ABCD-EFGHがあります。立方体の頂点Aから対角線CGに垂直に伸びる直線を引き、直線と立方体の表面との交点を求めてください。"""

if __name__ == "__main__":
    test_data_json = []
    questions_list = questions.split("\n")
    for num_q, sentence in enumerate(questions_list):
        test_data_json.append(
            {
                "id": num_q,
                "normaized": sentence
            }
        )
    # jsonに書き込み&新規作成
    with open(JSON_OUTPUT_PATH, 'w', encoding="utf-8") as f:
        json.dump(test_data_json, f, sort_keys=False, indent=4, ensure_ascii=False)