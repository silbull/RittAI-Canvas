<script setup>
    import { ref, defineEmits } from 'vue';

    import QuestionForm from './QuestionForm.vue';
    import ScriptForm from './ScriptForm.vue';
    
    // ScriptFormタグのバインド用
    const scriptText = ref('');
    // GPT動作中の状態を保持
    const completionState = ref("問題文を入力してください")

    // バックエンドにリクエストを投げる関数．第1引数はbodyに入れるデータ．pathは第2引数で指定する．
    const SendString2Backend = function(data, path=""){
        // 入力が空白だったら無視
        if(data == ""){
            completionState.value = "問題文が入力されていません"
            return
        }
        // 入力をバックエンドに送信
        completionState.value = "生成中です..."
        console.log(`in SendString2Backend(${path}) data: ` + data);
        fetch(
            path, // flask APIのパスを指定
            {
                method: 'POST',
                body: JSON.stringify({"input": data}),
                headers:{
                    "Content-type": "application/json; charset=UTF-8"
                }
            } // postのボディ
        ).then(res => res.json()).then( 
            // 同期処理．レスポンス取得後に実行．
            function(jdata){
                var output = jdata["output"];
                console.log(`in SendString2Backend(${path}) output: ` + output);

                completionState.value = "Completed"

                scriptText.value = output;
                console.log(`in SendString2Backend(${path}) scriptText.value: ` + scriptText.value);
            }
        )
    }

    // 子コンポーネントでの動作を親コンポーネントに伝達させて，親コンポーネントでイベント発火させるためのemit
    const emit = defineEmits(['notify']);
    // 親コンポーネントに動作を伝達させる関数，'input-submitted'は親コンポーネントでのイベントトリガー名
    function handleSubmit(data) {
        emit('input-submitted', data);
        console.log(`in FormsBody.vue in handleSubmit(data) data: ` + data);
    }
</script>

<template>
    <div class="container-002">
        <QuestionForm class="question_form-001" @input-submitted="data => SendString2Backend(data, '/push2gpt')"/>
            <div class="balloon-002">{{ completionState }}</div>
        <ScriptForm class="script_form" :script_props="scriptText" @input-submitted="handleSubmit"/>
    </div>
</template>

<style scoped>
.container-002 {
    display: flex;
    flex-direction: column;
}
.question_form-001 {
    margin-bottom: 5px;    /* 下側の余白 */
}

.balloon-002 {
    display: flex;
    justify-content: center;
    position: relative;
    max-width: 300px;
    margin-top: 15px;
    padding: .8em 1.2em;
    border-radius: 5px;
    background-color: #d2e6fc;
    color: #333333;
    margin-bottom: 5px;
}
.balloon-002::before {
    position: absolute;
    top: -15px;
    width: 30px;
    height: 15px;
    background-color: #d2e6fc;
    clip-path: polygon(50% 0, 0 100%, 100% 100%);
    content: '';
}
</style>
  