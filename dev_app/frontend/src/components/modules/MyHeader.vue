<template>
    <header class="app_header-1" style="display: flex;">
        <h2 class="heading-026">Texto<span class="heading-026-1">3D</span></h2>
    </header>
    <div class="flex-container">
    <button class= "btn" v-on:click="goToHomePage">
        <span class="text">通常モード</span>
    </button>
    <button class="btn" v-on:click="goToAnotherPage" >
        <span class="text">stepモード</span>
    </button>
    </div>

</template>

<script setup type="ts">

import { useRouter } from 'vue-router';

const router = useRouter();


const goToAnotherPage = () => {
    router.push('/routing')
}

const goToHomePage = () => {
    router.push('/')
}
</script>


<style scoped>
.app_header-1 {
    background-color: #2589d0;
    height: 7vh;
    position: relative;         /* 位置指定の基準点にする */
    margin-bottom: 10px;    /* 下側の余白 */
}

/* 1文字目だけ大きい見出し */
.heading-026 {
    color: #eeeeee;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 2.5vh;
    font-weight: bold;
    position: absolute;          /* 位置指定 */
    top: 25%;                    /* 親要素の半分下にずらす */
    left: 50%;                   /* 親要素の半分右にずらす */
    transform: translateY(-50%) translateX(-50%);    /* 要素自体の半分、上と左にずらす */
    padding: 20px;               /* 余白指定 */
}

.heading-026-1 {
    color: #eeeeee;
    font-size: 1.8em;
}

.flex-container {
    display: flex;
    justify-content: right;
    align-items: center;
    height: 50%;
}
.btn {
    border: none;
    width: 10em;
    height: 3em;
    border-radius: 3em;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    background: #2589d0;
    cursor: pointer;
    transition: all 450ms ease-in-out;
    margin-right: 10px;
    
}
.btn:hover {
  background-color: #1c5d8c;
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