import spacy
import ginza
import codecs

class DependencyAnalysis:

    def __init__(self, document=None, model="ja_ginza_electra"):
        """
        コンストラクタ
        """
        self.nlp = spacy.load(model)
        self.document = document

    def read_file(self,filename,encoding='utf-8'):
        '''
        ファイルの読み込み

        Parameters:
        --------
            filename : str   分析対象のファイル名 
        '''
        with codecs.open(filename,'r',encoding,'ignore') as f:
            self.read_text(f.read())

    def read_text(self,text):
        '''
        テキストの読み込み

        Parameters:
        --------
            text : str  分析対象のテキスト
        '''
        self.document = text

    def analyze(self,text = None,mode = 0,get_span = False):
        '''
        係り受け結果を主辞（文節で一番重要な単語）で出力

        Parameters:
        --------
            mode : int  0=通常の係り受け 1:係り受けされる側（左）のみに主辞を適用 2: 両方に主辞を適用  
        '''
        dep_list = []
        dep_blist = []
        span_list = []

        # mode が 1以下の場合、通常の係り受け関数、2の場合は主辞の関数を使用する
        func = ginza.bunsetu_spans if mode <= 1 else ginza.bunsetu_phrase_spans 
        
        # 引数があればそれを、Noneの場合はインスタンス変数の self.textを使う
        self.doc = self.nlp(self.document if (text == None) else text)
        
        # 文書から一文を取り出す
        for sentence in self.doc.sents:
            span_list_per_sentence = []
            # 係り受けの関数を適用
            for i_1, span in enumerate(func(sentence)):
                span_list.append(span)
                span_list_per_sentence.append(span)
                # 係り受け解析結果を取り出す
                for token in span.lefts:
                    # modeが 1 の場合のみ、係り受け元を文節として取り出す。（例 mode=0 or 2：交流を mode=1：交流)
                    key = token if mode == 1 else ginza.bunsetu_span(token) 

                    i_2 = span_list_per_sentence.index(key, 0, i_1)

                    # 結果を辞書に登録
                    dep_blist.append((i_2, i_1))
                    dep_list.append((str(key),str(span)))
        
        self.dep_list = dep_list
        self.dep_blist = dep_blist
        self.span_list = span_list

        return (dep_list, span_list) if get_span else dep_list
