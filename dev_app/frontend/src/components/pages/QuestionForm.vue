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
    <textarea class="textarea-01" placeholder="空間図形の問題を入力してください" v-model="question_text" @keydown.ctrl.enter="handleSubmit()"></textarea>
    <button class="button-send_to_GPT" @click="handleSubmit()">Create GGB Script</button>
</template>



<style scoped>
.textarea-01 {
    height: 30%;
    padding: 8px 10px;
    border: 1px solid #969da3;
    border-radius: 3px;
    color: #333;
    font-size: 1em;
    line-height: 1.5;
    margin-bottom: 4px;    /* 下側の余白 */
    resize:none;
}

.textarea-01::placeholder {
    color: #999;
}

.button-send_to_GPT {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 250px;
    margin:0 auto;
    padding: .9em 2em;
    border: none;
    border-radius: 5px;
    background-color: #2589d0;
    color: #fff;
    font-weight: 600;
    font-size: 1em;
}

.button-send_to_GPT:hover {
    background-color: #0f5688;
}
</style>