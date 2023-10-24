<script>
export default {
    emits: ['click'], // Vue 3でのカスタムイベントの宣言
    methods: {
        handleClick() {
            this.$emit('click'); // ボタンがクリックされたときにclickイベントを親コンポーネントに伝播させる
        }
    }
}
</script>

<template>
<button @click="handleClick">
    <slot></slot> <!-- スロットを利用してボタンのラベルを動的に指定する -->
</button>
</template>


<style scoped>
/* ボタンのデザインをここに定義 */
</style>
  