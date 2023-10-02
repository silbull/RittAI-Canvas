<script setup>
	/* eslint-disable */
	import { ref } from 'vue';
	import GGBBody from './components/pages/GGBBody.vue';
	import FormsBody from './components/pages/FormsBody.vue';

	import MyHeader from './components/modules/MyHeader.vue';
	import MyFooter from './components/modules/MyFooter.vue';

	// 子コンポーネントへ送信用の変数
	const scriptModifiedText = ref('');
	// 親コンポーネントに動作を伝達させる関数，'input-submitted'は親コンポーネントでのイベントトリガー名
	function testFunct(data) {
		scriptModifiedText.value = data
		console.log(`in App.vue in testFunct(data) scriptModifiedText.value: ` + scriptModifiedText.value);
	}
</script>

<template>
	<div class="ground-001">
		<MyHeader/>
		<div class="container-001">
			<FormsBody class="formsbody" @input-submitted="testFunct"/>
			<GGBBody class="ggbbody" :script_modified_props="scriptModifiedText"/>
		</div>

		<MyFooter/>
	</div>
</template>

<style scoped>
.ground-001 {
	background-color: #4193ce0f;
}

.container-001 {
    display: flex;
}

.formsbody {
	margin-right: 10px;
}
</style>
