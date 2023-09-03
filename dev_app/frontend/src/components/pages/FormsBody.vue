<script setup>
    import { ref, defineEmits } from 'vue';

    import QuestionForm from './QuestionForm.vue';
    import ScriptForm from './ScriptForm.vue';
    
    // ScriptFormタグのバインド用
    const scriptText = ref('');
    // GPT動作中の状態を保持
    const completionState = ref("")

    // バックエンドにリクエストを投げる関数．第1引数はbodyに入れるデータ．pathは第2引数で指定する．
    const SendString2Backend = function(data, path=""){
        // 入力が空白だったら無視
        if(data == ""){
            completionState.value = "問題文を入力してください．"
            return
        }
        // 入力をバックエンドに送信
        completionState.value = "GPT completion cretating is in execution... wait..."
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
    <QuestionForm @input-submitted="data => SendString2Backend(data, '/push2gpt')"/>
    <div>Completion Create State: {{ completionState }}</div>
    <ScriptForm :script_props="scriptText" @input-submitted="handleSubmit"/>
</template>
  