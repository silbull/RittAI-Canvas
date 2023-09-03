<script setup>
    import { defineEmits, ref } from 'vue'

    // textareaの代入先
    const question_text = ref("");

    // 子コンポーネントでの動作を親コンポーネントに伝達させて，親コンポーネントでイベント発火させるためのemit
    const emit = defineEmits(['notify']);
    // 親コンポーネントに動作を伝達させる関数，'input-submitted'は親コンポーネントでのイベントトリガー名
    function handleSubmit() {
        emit('input-submitted', question_text.value);
    }
</script>



<template>
    <textarea class="textarea-01" placeholder="数学問題を入力" v-model="question_text" @keydown.ctrl.enter="handleSubmit()"></textarea>
    <button @click="handleSubmit()">Send to GPT</button>
</template>



<style scoped>
        .textarea-01 {
        width: 100vw;
        height: 50px;
        padding: 8px 10px;
        border: 1px solid #969da3;
        border-radius: 3px;
        color: #333;
        font-size: 1em;
        line-height: 1.5;
    }

    .textarea-01::placeholder {
        color: #999;
    }
</style>