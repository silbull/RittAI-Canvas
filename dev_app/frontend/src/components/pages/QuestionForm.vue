<script setup >
    import { defineEmits, ref } from 'vue'
    import VueCropper from 'vue-cropperjs';
    import 'cropperjs/dist/cropper.css';
    import heic2any from 'heic2any';

    const cropperRef = ref('');
    const imageSrc = ref('');
    const showCropper = ref(false);

    let width = 0;
    let height = 0;

    const onFileChange = async (e) => {
        width = 0;
        height = 0;
        imageSrc.value = null;
        showCropper.value = false;
        let file = e.target.files[0];
        console.log("file: " + file + " file.type: " + file.type)
        // file typeがheicの場合はheic2anyで変換
        if (file.type === "image/heic" || file.type === "image/heif") {
        const convertedBlob = await heic2any({
            blob: file,
            toType: "image/jpeg",
        });
        file = new File([convertedBlob], "converted.jpg", { type: "image/jpeg" });
        console.log("file: " + file + " file.type: " + file.type)
    }

        const reader = new FileReader();
        reader.onload = (e) => {
            console.log(e.target.result)
            const img = new Image();
            img.src = e.target.result;
            img.onload = () => {
                console.log("画像data" + img.src)
                
                // 画像をリサイズ，最大1000x1000
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                const maxWidth = 800;
                const maxHeight = 600;
                width = img.naturalWidth;
                height = img.naturalHeight;
                if (width > height) {
                    if (width > maxWidth) {
                        height *= maxWidth / width;
                        width = maxWidth;
                    }
                } else {
                    if (height > maxHeight) {
                        width *= maxHeight / height;
                        height = maxHeight;
                    }
                }
                console.log("width: " + width + " height: " + height)
                canvas.width = width;
                canvas.height = height;
                ctx.drawImage(img, 0, 0, width, height);
                const resizeImageSrc = canvas.toDataURL(); // リサイズ後の画像データ
                imageSrc.value = resizeImageSrc; // cropperのsrcに代入
                showCropper.value = true;
            };
            

        };
        reader.readAsDataURL(file);

    };

    const handleOCR = async () => {
        console.log("in cropImage() width: " + width + " height: " + height)
        const cropperImage = cropperRef.value;
        const croppedCanvas = cropperImage.getCroppedCanvas();

        croppedCanvas.toBlob(async (blob) => {
            const formData = new FormData()
            formData.append('image', blob)

            fetch(
                // flask APIのパスを指定
                "/run_ocr", 
                {
                    method: 'POST',
                    body: formData, //dataをjsonに変換して送信
                } // postのボディ
            ).then(res => res.json()).then( 
                // 同期処理．レスポンス取得後に実行．
                function(jdata){
                    var output = jdata["text"];
                    console.log(`in handleOCR() output: ` + output);

                    question_text.value = output; // scriptTextに出力を代入
                    console.log(`in handleOCR() question_text.value: ` + question_text.value);
                    showCropper.value = false;
                }
            ).catch(error => console.error('Error:', error)); // エラー処理
        });
    };

    // textareaの代入先
    const question_text = ref("");

    // 子コンポーネントでの動作を親コンポーネントに伝達させて，親コンポーネントでイベント発火させるためのemit
    const emit = defineEmits(['input-submitted']);
    // 'input-submitted'というカスタムイベントを親コンポーネントに伝達し，親コンポーネント(FormsBody)でイベント発火させる関数
    function QuestionSubmit() {
        emit('input-submitted', question_text.value);
    }

</script>



<template>
    
<div >
    <input type="file" @change="onFileChange" />
    <div v-if="showCropper" class = "cropper-popup">
      <vue-cropper
        ref="cropperRef"
        :src="imageSrc"
        :movable="false"
        :zoomable="false"
        :zoomOnTouch="false"
        :autoCrop="true"
        :autoCropArea="0.99"
        :toggleDragModeOnDblclick="false"
        :dragMode="crop"
        :minCropBoxWidth="20"
        :minCropBoxHeight="20"
      ></vue-cropper>
      <button class="button-ocr" @click="handleOCR">画像から読み取る</button>
      <button class="close-popup" @click="showCropper = false">戻る</button>
    </div>
    <!-- <input type="file" id="imageUpload" />
    <button class="button-ocr" @click="handleOCR()">画像から読み取る</button> -->
</div>
    <textarea class="textarea-01" placeholder="空間図形の問題を入力してください" v-model="question_text" @keydown.ctrl.enter="QuestionSubmit()"></textarea>
    <button class="button-send_to_GPT" @click="QuestionSubmit()">Create GGB Script</button>
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
.button-ocr {
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
    margin-top: 5px;
    margin-bottom: 5px;    /* 下側の余白 */
}
.button-ocr:hover {
    background-color: #0f5688;
}

.close-popup {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 250px;
    margin:0 auto;
    padding: .9em 2em;
    border: 1px solid #2589d0;
    border-radius: 5px;
    background-color: #fff;
    color: #2589d0;
    font-size: 1em;
    margin-top: 5px;
    margin-bottom: 5px;    /* 下側の余白 */
}
.close-popup:hover {
    background-color: #dee0e1;
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

.cropper-popup {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(39, 38, 38, 0.5);
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

/* .cropper-popup img {
  width: 50%;
  height: 50%;
  object-fit: contain;
} */

</style>