<template>
    <header class="app_header-1">
        <h2 class="heading-026">Texto<span class="heading-026-1">3D</span></h2>
    </header>

</template>

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
</style>