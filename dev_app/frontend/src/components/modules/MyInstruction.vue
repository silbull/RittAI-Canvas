<script setup>
	/* eslint-disable */
	import { ref } from 'vue';
	import GGBBodys from '../pages/GGBBodys.vue';
    import FormsBody from '../pages/FormsBody.vue';

	

	// 子コンポーネントへ送信用の変数
	const scriptModifiedText = ref('');
	// 子へデータを送るためのpropsに値を代入する関数
	function testFunct(data) {
		scriptModifiedText.value = data
		console.log(`in MyInstruction.vue in testFunct(data) scriptModifiedText.value: ` + scriptModifiedText.value);
	}


</script>

<template>
	<div class="ground-001">
		<div class="container-001">
			<FormsBody class="formsbody" @ggbscript-to-model="testFunct"/>
			<GGBBodys class="ggbbodys" :ggb_script_props="scriptModifiedText"/>
		</div>
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