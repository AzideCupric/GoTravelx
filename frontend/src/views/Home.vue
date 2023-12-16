
import TravelPicVue from '../components/TravelPic.vue';
<script setup lang="ts">
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';
import NewYork from '../assets/image/NewYork.jpg';
import Beijing from '../assets/image/Beijing.jpg';
import Shanghai from '../assets/image/Shanghai.jpg';
import Tokyo from '../assets/image/Tokyo.jpg';
import London from '../assets/image/London.jpg';
import Dusanbe from '../assets/image/Dusanbe.jpg';
</script>

<template>
  <Header />

  <section>
    <div id="map"></div>
  </section>

  <section>
    <h1 class="display-5 text-center heading-2">美景一览</h1>
    <p class="text-center text-2"><br>愿你的旅途充满阳光和微风，愿每一步都是一首优美的诗篇。</p><br>
    <div class="container">
      <div class="owl-carousel owl-theme owl-loaded">
        <div>
          <img :src="NewYork" alt="NewYork">
          <h3>Times Square</h3>
          <i class="fas fa-map-marker-alt map"></i><span class="text-3"> 纽约 </span> <i class="fas fa-star star"></i>
          4.8<br>
        </div>
        <div>
          <img :src="Beijing" alt="Beijing">
          <h3>The Great Wall</h3>
          <i class="fas fa-map-marker-alt map"></i><span class="text-3"> 北京</span> <i class="fas fa-star star"></i>
          4.9<br>

        </div>
        <div>
          <img :src="Shanghai" alt="Shanghai">
          <h3>The Bund</h3>
          <i class="fas fa-map-marker-alt map"></i><span class="text-3"> 上海</span> <i class="fas fa-star star"></i>
          4.8<br>

        </div>
        <div>
          <img :src="Tokyo" alt="Tokyo">
          <h3>Mount Fuji</h3>
          <i class="fas fa-map-marker-alt map"></i><span class="text-3"> 东京</span> <i class="fas fa-star star"></i>
          4.7<br>

        </div>
        <div>
          <img :src="London" alt="London">
          <h3>St. Paul's Cathedral</h3>
          <i class="fas fa-map-marker-alt map"></i><span class="text-3"> 伦敦</span> <i class="fas fa-star star"></i>
          4.7<br>
        </div>
        <div>
          <img :src="Dusanbe" alt="Dusanbe">
          <h3>Iskandarkul</h3>
          <i class="fas fa-map-marker-alt map"></i><span class="text-3"> 杜尚别</span> <i class="fas fa-star star"></i>
          4.8<br>
          <br>
        </div>
      </div>
    </div>
  </section>
  <Footer />
</template>

<style scoped>
header {
  background-image: url(../image/Rectangle31.png);
  height: 700px;
  background-position: top right;
  background-size: cover;
  padding: 0;
  margin: 0;
}

.logo {
  font-family: 'Ribeye', cursive;
  margin-left: 100px;
}

li {
  display: inline-block;
  font-weight: 500;
  font-size: 16px;
}

li[class="nav-item menu"]:hover {
  transform: scale(1.2);
  transition: 0.5s;
}

.button-1 {
  margin-right: 100px;
}

.heading-1 {
  margin-top: 150px;
  margin-left: 100px;
  color: #fff;
  font-family: 'Gelasio', serif;
  font-size: 50px;
  font-weight: 700;
}

.text-1 {
  margin-left: 110px;
  color: #fff;
  font-size: 18px;
  opacity: 60%;
}

.button-2 {
  margin-left: 100px;
}

.heading-2 {
  margin-top: 100px;
  font-family: 'Gelasio', serif;
  font-size: 43px;
}

.text-2 {
  color: #000;
  font-size: 18px;
  opacity: 60%;
}

.card:hover {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.card-1 {
  margin-left: 20%;
}

.card-2 {
  margin-left: 10%;
  margin-right: 10%;
}

.card-3 {
  margin-right: 20%;
}

.card-title {
  font-family: 'Gelasio', serif;
}

.card-text {
  opacity: 60%;
}

.map {
  color: #fc1200;
}

.text-3 {
  opacity: 60%;
  margin-top: 20px;
}

.star {
  color: #ffc700;
  margin-left: 20%;
}

h3 {
  font-family: 'Gelasio', serif;
  padding-top: 20px;
}

.num {
  font-size: 18px;
  font-weight: 600;
}

.owl-dots {
  text-align: center;
  margin-top: 10px;
}

.owl-carousel button.owl-dot {
  width: 20px;
  border-radius: 180%;
  background: blue;
  margin: 0 3px;
}

.owl-next,
.owl-prev {
  position: absolute;
}

.owl-prev {
  right: 60%;
  top: 90%;
}

.owl-next {
  left: 60%;
  top: 90%;
}

h4 {
  font-family: 'Gelasio', serif;
  font-size: 20px;
}

span {
  font-weight: 500;
}

.row {
  padding-left: 5%;
  padding-right: 5%;
}

footer {
  background-color: #f6fbfb;
}

a {
  color: black;
}

ul.footer {
  padding-top: 10%;
}

a[class="nav-link text-body"]:hover {
  text-decoration: underline;
}

form {
  padding-top: 20%;
}

.facebook,
.twitter,
.instagram,
.google {
  color: black;
  font-size: 25px;
  margin-right: 5%;
}

/* 设置地图容器的高度 */
#map {
  height: 600px;
  width: 1000px;
  margin: auto;
  /* 使用 auto 将地图容器水平居中 */
}

/* 设置图片弹出框的样式 */
.popup-image {
  max-width: 150px;
  max-height: 150px;
  /* opacity: 60%; */
}

@media (max-width: 767px) {
  .heading-1 {
    font-size: 150%;
  }

  .text-1 {
    font-size: 80%
  }

  .card-1 {
    margin-left: 10%;
    margin-bottom: 20px;
  }

  .card-2 {
    margin-left: 10%;
    margin-right: 0;
    margin-bottom: 20px;
  }

  .card-3 {
    margin-left: 10%;
    margin-right: 0;
  }

  .owl-prev {
    right: 60%;
    top: 94%;
  }

  .owl-next {
    left: 60%;
    top: 94%;
  }

}</style>
