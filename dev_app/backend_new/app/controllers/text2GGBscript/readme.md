# 抽出機の実装 (中間発表以降)

## 【1】全体像
これまでの方法では，GPT4.0に`「GeoGebra Script知ってるでしょ．問題文渡すからScript作ってね．」`という雑な指示を与えていた．今回はこのタスクを2つに分割して実行させる．

具体的には，
1. オブジェクト抽出機
2. パラメータ抽出機
3. GGB Script 生成機  

の3つを実装し，タスクを分割した．

> ココに良い感じの図を貼りたいね

## 【2】オブジェクト抽出機

問題文からパーツオブジェクトの種類と名前を抽出する．inputと期待されるoutputは以下のとおり．

#### input 数学問題文
```question.txt:txt
立体ABCD-EFGHは，AB=40cm，AD=30cm，AE=50cmの直方体である．頂点Dと頂点Fを結び，頂点Bから線分DFに引いた垂線と線分DFとの交点をIとする．線分BIの長さは何cmか．
```

#### output パーツオブジェクトの種類と名前
```part_objects.json:json
[
    {
        "object_name": "ABCD-EFGH", 
        "object_type": "rectangular"
    },
    {
        "object_name": "DF", 
        "object_type": "Segment"
    },
    {
        "object_name": "p_BI", 
        "object_type": "PerpendicularLine"
    },
    {
        "object_name": "I", 
        "object_type": "Intersect"
    }
]
```

`GPT3.5`に対して，`function calling`を用いて実装した．  `new_version/main.py`ファイル内の `object_extracter` インスタンスを参照のこと．

## 【3】パラメータ抽出機

**【2】オブジェクト抽出機**の出力と問題文をもとにして，パーツオブジェクトを生成するために必要なパラメータを抽出します．inputと期待されるoutputは以下のとおり．


#### input1 オブジェクトの種類と名前
```part_objects.json:json
{
    "object_name": "ABCD-EFGH", 
    "object_type": "rectangular"
},
```

#### input2 数学問題文
```question.txt:txt
立体ABCD-EFGHは，AB=40cm，AD=30cm，AE=50cmの直方体である．
```


#### output パーツオブジェクトのパラメータ
```part_objects.json:json
{
    'side_name_width': 'AB', 
    'length_width': 40, 
    'side_name_depth': 'AD', 
    'length_depth': 30, 
    'side_name_height': 'AE', 
    'length_height': 50
}
```

`GPT3.5`に対して，`function calling`を用いて実装した．  `new_version/parameter_extracter.py`ファイル内に各図形に対応した関数を実装．現在は以下の図形に対する関数を実装済み．

> ("立方体" → "Cube"),  
("直方体" → "rectangular"),  
("線分" → "Segment"),  
("交点" → "Intersect"),  
("中点" → "Midpoint"),  
("垂線" → "PerpendicularLine"),  
("四面体" → "tetrahedron"),  

## 【4】GGB Script生成機

未実装です．完全にルールベースで実装できると考えています．