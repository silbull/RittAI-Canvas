<script setup>
    import { ref, defineEmits } from 'vue';

    import QuestionForm from './QuestionForm.vue';
    import ScriptForm from './ScriptForm.vue';
    
    // ScriptFormタグのバインド用
    const scriptText = ref('');
    // GPT動作中の状態を保持
    const completionState = ref("問題文を入力してください")

    const buttonText = ref("Create GGB Script")
    const gptLoading = ref(false)

    // バックエンドにリクエストを投げる関数．第1引数はbodyに入れるデータ．pathは第2引数で指定する．
    const SendString2Backend = (data, path="") => {
        // 入力が空白だったら無視
        if(data == ""){
            buttonText.value = "問題文が入力されていません"
            return
        }
        // 入力をバックエンドに送信
        buttonText.value = "生成中..."
        gptLoading.value = true
        console.log(`in SendString2Backend(${path}) data: ` + data);
        fetch(
            path, // flask APIのパスを指定
            {
                method: 'POST',
                body: JSON.stringify({"input": data}), //dataをjsonに変換して送信
                headers:{
                    "Content-type": "application/json; charset=UTF-8" // jsonかつUTF-8で送信
                }
            } // postのボディ
        ).then(res => res.json()).then( 
            // 同期処理．レスポンス取得後に実行．
            function(jdata){
                var output = jdata["output"];
                console.log(`in SendString2Backend(${path}) output: ` + output);

                buttonText.value = "Completed!"
                gptLoading.value = false

                scriptText.value = output; // scriptTextに出力を代入
                console.log(`in SendString2Backend(${path}) scriptText.value: ` + scriptText.value);
                setTimeout(() => {
                    buttonText.value = "Create GGB Script"
                }, 2000);
            }
        ).catch(error => console.error('Error:', error)); // エラー処理
    }

    // 子コンポーネントでの動作を親コンポーネントに伝達させて，親コンポーネントでイベント発火させるためのemit
    const emit = defineEmits(['notify']);
    // 親コンポーネントに動作を伝達させる関数，'ggbscript-to-model'は親コンポーネントでのイベントトリガー名
    function handleSubmit(data) {
        emit('ggbscript-to-model', data);
        console.log(`in FormsBody.vue in handleSubmit(data) data: ` + data);
    }
</script>

<template>
    <div class="container-002">
        <QuestionForm 
        class="question_form-001" 
        @input-submitted="data => SendString2Backend(data, '/push2gpt')" 
        :buttonText="buttonText" 
        :gptLoading="gptLoading"
        />
        <ScriptForm class="script_form" :script_props="scriptText" @script-submitted="handleSubmit"/>
    </div>
</template>

<style scoped>
.container-002 {
    display: flex;
    flex-direction: column;
}
.question_form-001 {
    margin-bottom: 10px;    /* 下側の余白 */
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
    font-weight: 600;
    font-size: 1em;
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

.script_form {
    margin-top: 10px;
}
</style>
  