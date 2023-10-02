<script>
export default {
    props: {
        placeholderText: {
            type: String,
            default: 'デフォルトのプレースホルダーテキスト'
        }
    },

    emits: ['click'], // Vue 3でのカスタムイベントの宣言
    methods: {
        handleEnter() {
            this.$emit('click'); // ボタンがクリックされたときにclickイベントを親コンポーネントに伝播させる
        }
    }
}
</script>

<template>
<textarea class="textarea-01" :placeholder="placeholderText" v-model="input" @keydown.ctrl.enter="handleEnter()"></textarea>
</template>


<style scoped>
/* テキストエリアのデザインをここに定義 */
</style>
  