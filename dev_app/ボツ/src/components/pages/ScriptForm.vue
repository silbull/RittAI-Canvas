<script setup>
    import { computed, ref } from 'vue'

    let input = ref("");

    const sendMessage = function(){
        // 入力が空白だったら無視
        if(input.value == "") return;
        // 入力をバックエンドに送信
        console.log("in sendMessage() input.value: " + input.value);
        // push2py(String(input.value));
        input.value += "clicked";
        
    }
</script>

<template>
    <textarea class="textarea-01" placeholder="数学問題を入力" v-model="input" @keydown.ctrl.enter="sendMessage"></textarea>
    <button @click="sendMessage">Send to GPT</button>
</template>

<style scoped>

</style>