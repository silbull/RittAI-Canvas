<script setup>
	/* eslint-disable */
	import { ref } from 'vue';
	import GGBBody from './components/pages/GGBBody.vue'
	import FormsBody from './components/pages/FormsBody.vue';

	// 子コンポーネントへ送信用の変数
	const scriptModifiedText = ref('');
	// 親コンポーネントに動作を伝達させる関数，'input-submitted'は親コンポーネントでのイベントトリガー名
	function testFunct(data) {
		scriptModifiedText.value = data
		console.log(`in App.vue in testFunct(data) scriptModifiedText.value: ` + scriptModifiedText.value);
	}
</script>

<template>
	<FormsBody @input-submitted="testFunct"/>
	<br>
	<GGBBody :script_modified_props="scriptModifiedText"/>
</template>

<style scoped>

</style>
