<script setup>
    import { computed, ref } from 'vue'

    let question_text = ref("");

    const SendString2Backend = function(path=""){
        // 入力が空白だったら無視
        if(question_text.value == "") return;
        // 入力をバックエンドに送信
        console.log("in SendString2Backend() question_text.value: " + question_text.value);
        let promise = fetch(
            path,
            {
                method: 'POST',
                body: JSON.stringify({"input": question_text.value}),
                headers:{
                    "Content-type": "application/json; charset=UTF-8"
                }
            }
        ).then(res => res.json()).then( 
            function(jdata){
                console.log("ここはthenの後");
                console.log(jdata);
                var output = jdata["output"];
                console.log("output: " + output);

                message_log_list.value.push(output);
                question_text.value = "";
            }
        )

        question_text.value += "SendString2Backendが起動しました";
        
    }
</script>



<template>
    <textarea class="textarea-01" placeholder="数学問題を入力" v-model="question_text" @keydown.ctrl.enter="SendString2Backend('/push2gpt')"></textarea>
    <button @click="SendString2Backend('/push2gpt')">Send to GPT</button>
</template>



<style scoped>

</style>