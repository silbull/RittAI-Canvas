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
	<div id="app">
		<MyHeader/>
    <router-view></router-view>
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

.flex-container {
    display: flex;
    justify-content: right;
    align-items: center;
    height: 50%;
}
.btn {
    border: none;
    width: 15em;
    height: 3em;
    border-radius: 3em;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    background: #2589d0;
    cursor: pointer;
    transition: all 450ms ease-in-out;
}

.sparkle {
    fill: #eeeeee;
    transition: all 800ms ease;
}

.text {
    font-weight: 600;
    color: #eeeeee;
    font-size: medium;
}
</style>
